from amazoncaptcha import AmazonCaptcha, AmazonCaptchaCollector, ContentTypeError
from maliarov import webdriver
import unittest
import os

class TestAmazonCaptcha(unittest.TestCase):

    def test_not_corrupted_image(self):
        solution = AmazonCaptcha('tests/captchas/notcorrupted.jpg').solve()
        self.assertEqual(solution, 'KRJNBY')

    def test_corrupted_image_with_last_letter_ending_at_the_beginning(self):
        solution = AmazonCaptcha('tests/captchas/corrupted.png').solve()
        self.assertEqual(solution, 'UGXGMM')

    def test_corrupted_image_with_letters_overlapping(self):
        solution = AmazonCaptcha('tests/captchas/corrupted_1.png').solve()
        self.assertEqual(solution, 'BPXHGH')

    def test_corrupted_image_with_both_overlap_and_separated_letter(self):
        solution = AmazonCaptcha('tests/captchas/corrupted_2.png').solve()
        self.assertEqual(solution, 'KMGMXE')

    def test_image_with_6_unrecognizable_letters(self):
        solution = AmazonCaptcha('tests/captchas/notsolved.jpg').solve()
        self.assertEqual(solution, 'Not solved')

    def test_totally_broken_image(self):
        solution = AmazonCaptcha('tests/captchas/notsolved_1.jpg').solve()
        self.assertEqual(solution, 'Not solved')

    def test_fromlink_and_keep_logs(self):
        link = 'https://i.ibb.co/Cn2J1mS/notsolved.jpg'
        captcha = AmazonCaptcha.fromlink(link)
        solution = captcha.solve(keep_logs=True)
        self.assertEqual(solution, 'Not solved')

    def test_content_type_error(self):
        link = 'https://ibb.co/kh13H5P'

        with self.assertRaises(ContentTypeError) as context:
            AmazonCaptcha.fromlink(link)

        self.assertTrue('is not supported as a Content-Type' in str(context.exception))

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
