from amazoncaptcha import AmazonCaptcha
from amazoncaptcha import AmazonCaptchaCollector
from maliarov import webdriver
import unittest
import os

class TestAmazonCaptcha(unittest.TestCase):

    def test_notcorrupted(self):
        solution = AmazonCaptcha('tests/captchas/notcorrupted.jpg').solve()
        self.assertEqual(solution, 'KRJNBY')

    def test_corrupted(self):
        solution = AmazonCaptcha('tests/captchas/corrupted.png').solve()
        self.assertEqual(solution, 'UGXGMM')

    def test_corrupted_1(self):
        solution = AmazonCaptcha('tests/captchas/corrupted_1.png').solve()
        self.assertEqual(solution, 'BPXHGH')

    def test_corrupted_2(self):
        solution = AmazonCaptcha('tests/captchas/corrupted_2.png').solve()
        self.assertEqual(solution, 'KMGMXE')

    def test_notsolved(self):
        solution = AmazonCaptcha('tests/captchas/notsolved.jpg').solve()
        self.assertEqual(solution, 'Not solved')

    def test_notsolved_1(self):
        solution = AmazonCaptcha('tests/captchas/notsolved_1.jpg').solve()
        self.assertEqual(solution, 'Not solved')

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

    def test_collector(self):
        collector = AmazonCaptchaCollector(output_folder = 'tests/captchas')
        collector.get_captcha_image()
        collector.distribute_collecting(range(4))

        self.assertGreaterEqual(len(os.listdir('tests/captchas')), 10)

    def test_collector_in_multiprocessing(self):
        collector = AmazonCaptchaCollector(output_folder = 'tests/captchas')
        collector.start(target = 12, processes = 2)

        self.assertGreaterEqual(len(os.listdir('tests/captchas')), 20)

if __name__ == '__main__':
    unittest.main()
