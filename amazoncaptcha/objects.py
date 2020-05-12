#-----------------------------------------------------------------------------------------------------------------------------------------------------------
# Modules
from PIL import Image, ImageChops
import os, json, zlib

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

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

class AmazonCaptcha(object):
    """
    This class represents an AmazonCaptcha object.

    :usage: captcha = AmazonCaptcha('captcha.jpg')
            answer = captcha.solve()
    """

    def __init__(self, img, monoweight = 1, onreturn = 'string'):
        """
        :param img: Path to input image.
        :param monoweight: Stands to define the range of color codes while monochroming. Please, do not change.
        :param onreturn: 'string' = 'ABCDEF'
                         'dict' = {'1': 'A', '2': 'B', '3': 'C', '4': 'D', '5': 'E', '6': 'F'}
                         'raw_dict' = the same as 'dict', but it will be returned even if a captcha wasn't solved.
        """

        self.img = Image.open(img, 'r')
        self.size = self.img.size
        self.monoweight = monoweight
        self.onreturn = onreturn
        self.letters = dict()
        self.result = dict()
        # Creates abspath to 'data' folder, which contains training data for solving captchas.
        self.data_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__))) + os.sep + 'data' + os.sep

    def monochrome(self):
        """
        Makes a captcha pure monochrome.

        Implemented through PIL.Image.eval
        :src: https://pillow.readthedocs.io/en/stable/reference/Image.html?#PIL.Image.eval

        Literally says: "for each pixel of an image turn codes 0, 1 to a 0,
        while everything in range from 2 to 255 should be replaced with 255".
        *All the numbers stay for color codes.
        """

        self.img = Image.eval(self.img, lambda a: 0 if a <= self.monoweight else 255)

    def find_letters(self):
        """
        Finds and separates letters from a captcha image.

        Populates 'self.letters' with an extracted letters.

        :errors: If the number of extracted letters isn't 6, final result is 'Error'.
        """

        inletter = False
        foundletter = False
        start = 0
        end = 0

        letter_boxes = list()
        for x in range(self.size[0]):
            column = [self.img.getpixel((x, y)) for y in range(self.size[1])]

            if 0 in column:
                inletter = True

            if foundletter == False and inletter == True:
                foundletter = True
                start = x

            if foundletter == True and (inletter == False or x == self.size[0] - 1):
                foundletter = False
                end = x

                letter_boxes.append((start, end))

            inletter = False

        if len(letter_boxes) != 6:
            return None

        for place, letter_box in zip(range(1, 7), letter_boxes):
            letter = self.img.crop((letter_box[0], 0, letter_box[1], self.size[1]))
            letter = cut_the_white(letter)

            # Gets letter's color data.
            letter_data = list(letter.getdata())
            # Makes a string, where '1' represents a black pixel and '0' represents a white one.
            letter_data_string = ''.join(['1' if pix == 0 else '0' for pix in letter_data])
            # Compresses the Str to Bytes, then stores result Bytes as string. The only thing why we are doing
            # this -  is because it costs 3 times less storage space.
            pseudo_binary = str(zlib.compress(letter_data_string.encode('utf-8')))
            # Adds pseudo binary strings to according places (i.e. 1, 2, 3...).
            self.letters[str(place)] = pseudo_binary

    def translate(self):
        """
        Finds patterns to extracted pseudo binary strings from data folder.

        Literally says: "for each pseudo binary walk through every stored letter pattern
        and find a match. If there is no such letter stored, go to next letter. If all the
        letters checked and there is no result, fill this place as blank."

        :errors:ref:method:'find_letters': Check for more info.
        """

        alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        for place, pseudo_binary in self.letters.items():
            for letter in alpha:
                try:
                    with open(self.data_folder + letter + '.json', 'r', encoding = 'utf-8') as js:
                        data = json.loads(js.read())

                except:
                    continue

                if pseudo_binary in data:
                    self.result[place] = letter
                    break

            else:
                self.result[place] = ''

        # Returns any result
        if self.onreturn == 'raw_dict':
            pass
        # If there is no result at all, it means that :method:'find_letters': wasn't able to proceed.
        elif not list(self.result.values()):
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
        self.translate()
        return self.result

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
