# -*- coding: utf-8 -*-

from amazoncaptcha import AmazonCaptcha, AmazonCaptchaCollector, ContentTypeError, NotFolderError
from amazoncaptcha.__version__ import __version__
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from tempfile import TemporaryDirectory
import unittest
import os


# --------------------------------------------------------------------------------------------------------------

here = os.path.abspath(os.path.dirname(__file__))
base_examples_folder = os.path.join(here, 'examples/base')
accuracy_examples_folder = os.path.join(here, 'examples/accuracy')
test_folder = TemporaryDirectory().name

print(f'using temp directory {test_folder} as test folder\n')


class TestAmazonCaptcha(unittest.TestCase):

    def test_not_corrupted_image(self):
        solution = AmazonCaptcha(os.path.join(base_examples_folder, 'notcorrupted_1.jpg')).solve()
        self.assertEqual(solution, 'KRJNBY')

    def test_image_link_property_warning(self):
        captcha = AmazonCaptcha(os.path.join(base_examples_folder, 'notcorrupted_1.jpg'))
        self.assertEqual(captcha.image_link, None)

    def test_corrupted_image_with_last_letter_ending_at_the_beginning(self):
        solution = AmazonCaptcha(os.path.join(base_examples_folder, 'corrupted_1.png')).solve()
        self.assertEqual(solution, 'UGXGMM')

    def test_corrupted_image_with_letters_overlapping(self):
        solution = AmazonCaptcha(os.path.join(base_examples_folder, 'corrupted_2.png')).solve()
        self.assertEqual(solution, 'BPXHGH')

    def test_corrupted_image_with_both_overlap_and_separated_letter(self):
        solution = AmazonCaptcha(os.path.join(base_examples_folder, 'corrupted_3.png')).solve()
        self.assertEqual(solution, 'KMGMXE')

    def test_image_with_6_unrecognizable_letters(self):
        solution = AmazonCaptcha(os.path.join(base_examples_folder, 'notsolved_1.jpg')).solve()
        self.assertEqual(solution, 'Not solved')

    def test_totally_broken_image(self):
        solution = AmazonCaptcha(os.path.join(base_examples_folder, 'notsolved_2.jpg')).solve()
        self.assertEqual(solution, 'Not solved')

    def test_fromlink_with_predefined_undolvable_captcha(self):
        link = 'https://i.ibb.co/Cn2J1mS/notsolved.jpg'
        captcha = AmazonCaptcha.fromlink(link)
        solution = captcha.solve()
        self.assertEqual(solution, 'Not solved')

    def test_fromlink_with_predefined_unsolvable_captcha_and_keep_logs(self):
        unique_test_folder = os.path.join(test_folder, 'test_fromlink_with_predefined_unsolvable_captcha_and_keep_logs')
        logs_path = os.path.join(unique_test_folder, 'not-solved-captcha.log')

        link = 'https://i.ibb.co/Cn2J1mS/notsolved.jpg'
        captcha = AmazonCaptcha.fromlink(link)
        captcha.solve(keep_logs=True, logs_path=logs_path)
        self.assertIn('not-solved-captcha.log', os.listdir(unique_test_folder))

    def test_content_type_error(self):
        link = 'https://ibb.co/kh13H5P'

        with self.assertRaises(ContentTypeError) as context:
            AmazonCaptcha.fromlink(link)

        self.assertTrue('is not supported as a Content-Type' in str(context.exception))

    def test_fromdriver(self):
        options = webdriver.ChromeOptions()
        options.add_argument('no-sandbox')
        options.add_argument('headless')
        driver = webdriver.Chrome(service=ChromeService(), options=options)

        solutions = list()
        for i in range(5):
            driver.get('https://www.amazon.com/errors/validateCaptcha')

            captcha = AmazonCaptcha.fromdriver(driver)
            solutions.append(len(captcha.solve()))

        driver.quit()

        self.assertIn(6, solutions)

    def test_collector(self):
        target = 4
        unique_test_folder = os.path.join(test_folder, 'test_collector')
        collector = AmazonCaptchaCollector(output_folder_path=unique_test_folder)
        collector._distribute_collecting(range(target))

        self.assertEqual(len(os.listdir(unique_test_folder)), target)

    def test_collector_in_multiprocessing(self):
        target = 16
        processes = 2
        unique_test_folder = os.path.join(test_folder, 'test_collector_in_multiprocessing')
        collector = AmazonCaptchaCollector(output_folder_path=unique_test_folder)
        collector.start(target=target, processes=processes)

        self.assertEqual(len(os.listdir(unique_test_folder)), target)

    def test_not_folder_error(self):
        with self.assertRaises(NotFolderError) as context:
            AmazonCaptchaCollector(output_folder_path=os.path.join(base_examples_folder, 'notcorrupted_1.jpg'))

        self.assertTrue('is not a folder. Cannot store images there.' in str(context.exception))

    def test_solve_rate_test(self):
        target = 8
        processes = 1
        unique_test_folder = os.path.join(test_folder, 'test_solve_rate_test')
        collector = AmazonCaptchaCollector(output_folder_path=unique_test_folder, solve_rate_test=True)
        collector.start(target=target, processes=processes)

        self.assertIn('test-results.log', os.listdir(unique_test_folder))

    def test_solve_rate_test_in_multiprocessing(self):
        target = 16
        processes = 2
        unique_test_folder = os.path.join(test_folder, 'test_solve_rate_test_in_multiprocessing')
        collector = AmazonCaptchaCollector(output_folder_path=unique_test_folder, solve_rate_test=True)
        collector.start(target=target, processes=processes)

        self.assertIn('test-results.log', os.listdir(unique_test_folder))

    def test_accuracy_rate_test(self):
        target = None
        examples_filenames = os.listdir(accuracy_examples_folder)
        if target is None:
            target = len(examples_filenames)

        example_index_padding = len(str(target)) + 2
        examples_solved_correctly = 0
        examples_count = 0
        for idx, example_filename in enumerate(examples_filenames):
            examples_count += 1
            expected_solution = os.path.splitext(example_filename)[0]
            example_full_path = os.path.join(accuracy_examples_folder, example_filename)
            solution = AmazonCaptcha(example_full_path).solve()
            is_correct = solution != 'Not solved' and solution == expected_solution
            example_index_string = f'{idx + 1}.'.ljust(example_index_padding, ' ')
            log_message = f'{example_index_string}{example_full_path}::{expected_solution}::{solution}::' + ('V:' if is_correct else 'X:')
            print(log_message)

            if is_correct:
                examples_solved_correctly += 1

            if idx > target:
                break

        success_percentage = round((examples_solved_correctly / examples_count) * 100, 5)
        result = f'::Test::Ver{__version__}::Cap{examples_count}::Per{success_percentage}::'
        print(result)

# --------------------------------------------------------------------------------------------------------------
