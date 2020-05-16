from amazoncaptcha import AmazonCaptcha
from maliarov import webdriver
import unittest

class TestAmazonCaptcha(unittest.TestCase):

    def test_notcorrupted(self):
        solution = AmazonCaptcha('tests/captchas/notcorrupted.jpg').solve()
        self.assertEqual(solution, 'KRJNBY')

    def test_corrupted(self):
        solution = AmazonCaptcha('tests/captchas/corrupted.png').solve()
        self.assertEqual(solution, 'UGXGMM')

    def test_error(self):
        solution = AmazonCaptcha('tests/captchas/error.png').solve()
        self.assertEqual(solution, 'Error')

    def test_error_1(self):
        solution = AmazonCaptcha('tests/captchas/error_1.png').solve()
        self.assertEqual(solution, 'Error')

    def test_notsolved(self):
        solution = AmazonCaptcha('tests/captchas/notsolved.jpg').solve()
        self.assertEqual(solution, 'Not solved')

    def test_output_dict(self):
        solution = AmazonCaptcha('tests/captchas/notcorrupted.jpg', onreturn = 'dict').solve()
        self.assertEqual(solution, {'1': 'K', '2': 'R', '3': 'J', '4': 'N', '5': 'B', '6': 'Y'})

    def test_output_raw_dict(self):
        solution = AmazonCaptcha('tests/captchas/notcorrupted.jpg', onreturn = 'raw_dict').solve()
        self.assertEqual(solution, {'1': 'K', '2': 'R', '3': 'J', '4': 'N', '5': 'B', '6': 'Y'})

    def test_from_webdriver(self):
        capabilities = webdriver.ChromeCapabilities()
        capabilities.add_argument('--headless')
        capabilities.add_argument('--no-sandbox')
        driver = webdriver.ChromeDriver('/usr/local/bin/chromedriver', desired_capabilities = capabilities.desired)

        solutions = list()
        for i in range(5):
            driver.get('https://www.amazon.com/errors/validateCaptcha')

            captcha = AmazonCaptcha.from_webdriver(driver)
            solutions.append(len(captcha.solve()))

        driver.quit()

        self.assertIn(6, solutions)

if __name__ == '__main__':
    unittest.main()
