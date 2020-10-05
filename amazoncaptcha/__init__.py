# -*- coding: utf-8 -*-

"""Solver for Amazon's image captcha.

The motivation behind the creation of this library is taking its start from
the genuinely simple idea: "I don't want to use pytesseract or some other
non-amazon-specific OCR services, nor do I want to install some executables to
just solve a captcha. I desire to get a solution within 1-2 lines of code
without any heavy add-ons. Using a pure Python."

Examples:
    For data extraction or web scraping specialists, who is crawling Amazon by
    using selenium, the class method below will do all the "dirty" work of
    extracting an image from the webpage for you:

        from amazoncaptcha import AmazonCaptcha
        from selenium import webdriver

        driver = webdriver.Chrome()
        driver.get('https://www.amazon.com/errors/validateCaptcha')

        captcha = AmazonCaptcha.from_webdriver(driver)
        solution = captcha.solve()

"""

from .objects import *

#--------------------------------------------------------------------------------------------------------------

