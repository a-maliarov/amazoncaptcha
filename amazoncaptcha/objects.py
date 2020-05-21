#-----------------------------------------------------------------------------------------------------------------------------------------------------------
# Modules
from PIL import Image, ImageChops
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

def find_letter_boxes(img, maxlength):
    """
    Finds and separates letters from a captcha image.

    :param img: A PIL.Image instance of a monochrome captcha.
    :param maxlength: maximum length of a letter, an integer.
    :returns: A list with X coordinates of letters (letter boxes).
    """

    image_columns = [[img.getpixel((x, y)) for y in range(img.height)] for x in range(img.width)]
    image_code = [1 if 0 in column else 0 for column in image_columns]
    xpoints = [d for d, s in zip(range(len(image_code)), image_code) if s]
    xcoords = [x for x in xpoints if x - 1 not in xpoints or x + 1 not in xpoints]
    xcoords.insert(1, xcoords[0]) if len(xcoords) % 2 else None

    letter_boxes = list()
    for s, e in zip(xcoords[0::2], xcoords[1::2]):
        start, end = s, min(e + 1, img.width - 1)

        if end - start <= maxlength:
            letter_boxes.append((start, end))

        else:
            two_letters = {k: v.count(0) for k, v in enumerate(image_columns[start + 5:end - 5])}
            divider = min(two_letters, key = two_letters.get) + 5
            letter_boxes.extend([(start, start + divider), (start + divider + 1, end)])

    return letter_boxes

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

class AmazonCaptcha(object):
    """
    This class represents an AmazonCaptcha object.
    """

    monoweight = 1
    maximum_letter_length = 33
    minimum_letter_length = 14

    def __init__(self, img):
        """
        :param img: Path to an input image OR an instance of BytesIO representing this image.
        """

        self.img = Image.open(img, 'r')
        self.letters = dict()
        self.result = dict()
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

        self.img = self.img.convert('L')
        self.img = Image.eval(self.img, lambda a: 0 if a <= self.monoweight else 255)

    def find_letters(self):
        """
        Extracts letters from an image using letter boxes.

        Populates 'self.letters' with extracted letters.
        """

        letter_boxes = find_letter_boxes(self.img, self.maximum_letter_length)
        letters = [self.img.crop((letter_box[0], 0, letter_box[1], self.img.height)) for letter_box in letter_boxes]

        if (len(letters) == 6 and letters[0].width < self.minimum_letter_length) or (len(letters) != 6 and len(letters) != 7):
            return None

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
            letter_data = list(letter.getdata())
            letter_data_string = ''.join(['1' if pix == 0 else '0' for pix in letter_data])

            pseudo_binary = str(zlib.compress(letter_data_string.encode('utf-8')))
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

        if (not self.result) or ('' in self.result.values()):
            self.result = 'Not solved'

        else:
            self.result = ''.join(self.result.values())

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
    def from_webdriver(cls, driver):
        """
        :param driver: A selenium.webdriver.* instance.
        :returns: AmazonCaptcha instance.
        """

        png = driver.get_screenshot_as_png()
        element = driver.find_element_by_tag_name('img')

        location = element.location
        size = element.size
        left = location['x']
        top = location['y']
        right = location['x'] + size['width']
        bottom = location['y'] + size['height']

        img = Image.open(BytesIO(png))
        img = img.crop((left, top, right, bottom))

        bytes_array = BytesIO()
        img.save(bytes_array, format='PNG')
        img_bytes_array = bytes_array.getvalue()

        return cls(BytesIO(img_bytes_array))

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
