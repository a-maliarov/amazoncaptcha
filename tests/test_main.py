from amazoncaptcha import AmazonCaptcha
import unittest
import os

class TestAmazonCaptcha(unittest.TestCase):

    current_location = os.path.abspath(os.path.dirname(os.path.abspath(__file__))) + os.sep

    def test_solve(self):
        solutions = list()

        for file in os.listdir(self.current_location + 'captchas' + os.sep):
            captcha = AmazonCaptcha(self.current_location + 'captchas' + os.sep + file)
            solutions.append(captcha.solve())

        self.assertEqual(solutions, ['UGXGMM', 'KRJNBY'])

if __name__ == '__main__':
    unittest.main()
