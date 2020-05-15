#-----------------------------------------------------------------------------------------------------------------------------------------------------------
# Modules
from PIL import Image
from PIL import ImageChops
from io import BytesIO
import os
import json
import zlib

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

def cut_the_white(letter):
    """
    Cuts white spaces/borders to get a clear letter.

    Implemented through PIL.ImageChops.difference
    :src: https://pillow.readthedocs.io/en/stable/reference/ImageChops.html#PIL.ImageChops.difference

    We do not trim the whole image at the start, because all the letters
    have different position by Y, which means that cutting white spaces
    from the beginning won't lead to anything, until letters are separated.

    :param letter: A PIL.Image instance of found letter.
    :returns: A PIL.Image instance of found letter with removed white spaces.
    """

    background = Image.new(letter.mode, letter.size, 255)
    diff = ImageChops.difference(letter, background)
    bbox = diff.getbbox()
    return letter.crop(bbox)

def merge_horizontally(img1, img2):
    """
    Merges two letters horizontally.

    Created in case image is corrupted and last letter ends at the beginning,
    causing letter to be unreadable.

    :param img1: A PIL.Image instance of first letter.
    :param img2: A PIL.Image instance of second letter.
    :returns: A PIL.Image instance of two merged letters.
    """

    merged = Image.new('L', (img1.width + img2.width, img1.height))
    merged.paste(img1, (0, 0))
    merged.paste(img2, (img1.width, 0))
    return merged

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

class AmazonCaptcha(object):
    """
    This class represents an AmazonCaptcha object.
    """

    def __init__(self, img, monoweight = 1, onreturn = 'string'):
        """
        :param img: Path to an input image OR an instance of BytesIO representing this image.
        :param monoweight: Stands to define the range of color codes while monochroming. Please, do not change.
        :param onreturn: 'string' = 'ABCDEF'
                         'dict' = {'1': 'A', '2': 'B', '3': 'C', '4': 'D', '5': 'E', '6': 'F'}
                         'raw_dict' = the same as 'dict', but it will be returned even if a captcha wasn't solved.
        """

        self.img = Image.open(img, 'r')
        self.monoweight = monoweight
        self.onreturn = onreturn
        self.letters = dict()
        self.result = dict()

        # Creates abspath to 'data' folder, which contains training data for solving captchas.
        self.data_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__))) + os.sep + 'data' + os.sep
        self.alphabet = [i.split('.')[0] for i in os.listdir(self.data_folder)]

    def monochrome(self):
        """
        Makes a captcha pure monochrome.

        Implemented through PIL.Image.eval
        :src: https://pillow.readthedocs.io/en/stable/reference/Image.html?#PIL.Image.eval

        Literally says: "for each pixel of an image turn codes 0, 1 to a 0,
        while everything in range from 2 to 255 should be replaced with 255".
        *All the numbers stay for color codes.
        """

        # 0.0.11 Added ".convert('L')" to prevent Error if image was stored from BytesIO
        self.img = self.img.convert('L')
        self.img = Image.eval(self.img, lambda a: 0 if a <= self.monoweight else 255)

    def find_letters(self):
        """
        Finds and separates letters from a captcha image.

        Vertically iterates an image, column example is [255, 255, 255, 0, 0, 255, ...].
        If '0' (black) is present, then current column is a part of a letter.

        Populates 'self.letters' with extracted letters.
        """

        in_letter = False
        found_letter = False
        start = 0
        end = 0

        letter_boxes = list()
        for x in range(self.img.width):
            column = [self.img.getpixel((x, y)) for y in range(self.img.height)]

            if 0 in column:
                in_letter = True

            if not found_letter and in_letter:
                found_letter = True
                start = x

            if found_letter and (not in_letter or x == self.img.width - 1):
                found_letter = False
                end = x

                letter_boxes.append((start, end))

            in_letter = False

        letters = [self.img.crop((letter_box[0], 0, letter_box[1], self.img.height)) for letter_box in letter_boxes]

        if (len(letters) == 6 and letters[0].width < 7) or (len(letters) != 6 and len(letters) != 7):
            return 'Error'

        if len(letters) == 7:
            letters[6] = merge_horizontally(letters[6], letters[0])
            del letters[0]

        letters = [cut_the_white(letter) for letter in letters]
        self.letters = {str(k): v for k, v in zip(range(1, 7), letters)}

    def save_letters(self):
        """
        Transforms separated letters into pseudo binary.

        Populates 'self.letters' with pseudo binaries.
        """

        for place, letter in self.letters.items():

            # Gets letter's color data.
            letter_data = list(letter.getdata())

            # Makes a string, where '1' represents a black pixel and '0' represents a white one.
            letter_data_string = ''.join(['1' if pix == 0 else '0' for pix in letter_data])

            # Compresses the Str to Bytes, then stores result Bytes as string. The only thing why we are doing
            # this -  is because it costs 3 times less storage space.
            pseudo_binary = str(zlib.compress(letter_data_string.encode('utf-8')))

            # Adds pseudo binary strings to according places (i.e. 1, 2, 3...).
            self.letters[place] = pseudo_binary

    def translate(self):
        """
        Finds patterns to extracted pseudo binary strings from data folder.

        Literally says: "for each pseudo binary walk through every stored letter pattern
        and find a match. If there is no such letter stored, go to next letter. If all the
        letters checked and there is no result, fill this place as blank."

        :errors:ref:method:'find_letters': Check for more info.
        """

        for place, pseudo_binary in self.letters.items():
            for letter in self.alphabet:

                with open(self.data_folder + letter + '.json', 'r', encoding = 'utf-8') as js:
                    data = json.loads(js.read())

                if pseudo_binary in data:
                    self.result[place] = letter
                    break

            else:
                self.result[place] = ''

        # Returns any result
        if self.onreturn == 'raw_dict':
            pass

        # If there is no result at all, it means that :method:'find_letters': wasn't able to proceed.
        elif not self.result:
            self.result = 'Error'

        # If there are some blanks AND solved letters, there is no error, but a captcha wasn't solved.
        elif '' in self.result.values():
            self.result = 'Not solved'

        # If all the letters are present, captcha was solved correctly.
        else:

            # Returns Str instance solution
            if self.onreturn == 'string':
                self.result = ''.join(self.result.values())

            # Since data was stored into 'self.result' dict all the way, just a 'pass' will do.
            elif self.onreturn == 'dict':
                pass

    def solve(self):
        """
        Runs the sequence.

        :returns: Solved captcha.
        """

        self.monochrome()
        self.find_letters()
        self.save_letters()
        self.translate()
        return self.result

    @classmethod
    def from_webdriver(cls, driver, monoweight = 1, onreturn = 'string'):
        """
        :param driver: A selenium.webdriver.* instance.
        :param monoweight: Stands to define the range of color codes while monochroming. Please, do not change.
        :param onreturn: 'string' = 'ABCDEF'
                         'dict' = {'1': 'A', '2': 'B', '3': 'C', '4': 'D', '5': 'E', '6': 'F'}
                         'raw_dict' = the same as 'dict', but it will be returned even if a captcha wasn't solved.
        :returns: AmazonCaptcha instance.
        """

        # Takes a screenshot of whole page and finds a captcha.
        png = driver.get_screenshot_as_png()
        element = driver.find_element_by_tag_name('img')

        # Gets captcha's location on the screenshot and constructs bbox.
        location = element.location
        size = element.size
        left = location['x']
        top = location['y']
        right = location['x'] + size['width']
        bottom = location['y'] + size['height']

        # Crops the captcha.
        img = Image.open(BytesIO(png))
        img = img.crop((left, top, right, bottom))

        # Stores image into BytesIO.
        bytes_array = BytesIO()
        img.save(bytes_array, format='PNG')
        img_bytes_array = bytes_array.getvalue()

        return cls(BytesIO(img_bytes_array), monoweight = monoweight, onreturn = onreturn)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
