# -*- coding: utf-8 -*-
from selenium.webdriver.chrome.service import Service

from amazoncaptcha import AmazonCaptcha, AmazonCaptchaCollector, ContentTypeError, NotFolderError, __version__
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import unittest
import os

#--------------------------------------------------------------------------------------------------------------

here = os.path.abspath(os.path.dirname(__file__))
captchas_folder = os.path.join(here, 'captchas')
test_folder = os.path.join(here, 'test_folder')

class TestAmazonCaptcha(unittest.TestCase):

    def test_not_corrupted_image(self):
        solution = AmazonCaptcha(os.path.join(captchas_folder, 'notcorrupted.jpg')).solve()
        self.assertEqual(solution, 'KRJNBY')

    def test_image_link_property_warning(self):
        captcha = AmazonCaptcha(os.path.join(captchas_folder, 'notcorrupted.jpg'))
        self.assertEqual(captcha.image_link, None)

    def test_corrupted_image_with_last_letter_ending_at_the_beginning(self):
        solution = AmazonCaptcha(os.path.join(captchas_folder, 'corrupted.png')).solve()
        self.assertEqual(solution, 'UGXGMM')

    def test_corrupted_image_with_letters_overlapping(self):
        solution = AmazonCaptcha(os.path.join(captchas_folder, 'corrupted_1.png')).solve()
        self.assertEqual(solution, 'BPXHGH')

    def test_corrupted_image_with_both_overlap_and_separated_letter(self):
        solution = AmazonCaptcha(os.path.join(captchas_folder, 'corrupted_2.png')).solve()
        self.assertEqual(solution, 'KMGMXE')

    def test_image_with_6_unrecognizable_letters(self):
        solution = AmazonCaptcha(os.path.join(captchas_folder, 'notsolved.jpg')).solve()
        self.assertEqual(solution, 'Not solved')

    def test_totally_broken_image(self):
        solution = AmazonCaptcha(os.path.join(captchas_folder, 'notsolved_1.jpg')).solve()
        self.assertEqual(solution, 'Not solved')

    def test_fromlink_with_predefined_undolvable_captcha(self):
        link = 'https://i.ibb.co/Cn2J1mS/notsolved.jpg'
        captcha = AmazonCaptcha.fromlink(link)
        solution = captcha.solve()
        self.assertEqual(solution, 'Not solved')

    def test_fromlink_with_predefined_undolvable_captcha_and_keep_logs(self):
        link = 'https://i.ibb.co/Cn2J1mS/notsolved.jpg'
        captcha = AmazonCaptcha.fromlink(link)
        solution = captcha.solve(keep_logs=True)
        self.assertIn('not-solved-captcha.log', os.listdir())

    def test_content_type_error(self):
        link = 'https://ibb.co/kh13H5P'

        with self.assertRaises(ContentTypeError) as context:
            AmazonCaptcha.fromlink(link)

        self.assertTrue('is not supported as a Content-Type' in str(context.exception))

    def test_fromdriver(self):
        options = webdriver.ChromeOptions()
        options.add_argument('no-sandbox')
        options.add_argument('headless')
        driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()), options=options)

        solutions = list()
        for i in range(5):
            driver.get('https://www.amazon.com/errors/validateCaptcha')

            captcha = AmazonCaptcha.fromdriver(driver)
            solutions.append(len(captcha.solve()))

        driver.quit()

        self.assertIn(6, solutions)

    def test_collector(self):
        collector = AmazonCaptchaCollector(output_folder_path = test_folder)
        collector.get_captcha_image()
        collector._distribute_collecting(range(4))

        self.assertGreaterEqual(len(os.listdir(test_folder)), 4)

    def test_collector_in_multiprocessing(self):
        collector = AmazonCaptchaCollector(output_folder_path = test_folder)
        collector.start(target = 13, processes = 2)

        self.assertGreaterEqual(len(os.listdir(test_folder)), 16)

    def test_not_folder_error(self):

        with self.assertRaises(NotFolderError) as context:
            collector = AmazonCaptchaCollector(output_folder_path = os.path.join(captchas_folder, 'notcorrupted.jpg'))

        self.assertTrue('is not a folder. Cannot store images there.' in str(context.exception))

    def test_accuracy_test(self):
        collector = AmazonCaptchaCollector(output_folder_path = test_folder, accuracy_test=True)
        collector.get_captcha_image()
        collector._distribute_collecting(range(4))

        self.assertIn(f'collector-logs-{__version__.__version__.replace(".", "")}.log', os.listdir(test_folder))

    def test_accuracy_test_in_multiprocessing(self):
        collector = AmazonCaptchaCollector(output_folder_path = test_folder, accuracy_test=True)
        collector.start(target = 12, processes = 2)

        self.assertIn('test-results.log', os.listdir(test_folder))

#--------------------------------------------------------------------------------------------------------------
