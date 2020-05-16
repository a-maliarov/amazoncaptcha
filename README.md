# Amazon Captcha Solver
Pure Python (3.6+), lightweight, [Pillow](https://github.com/python-pillow/Pillow)-based solver for the [Amazon's text captcha](https://www.amazon.com/errors/validateCaptcha).

[![Accuracy](https://img.shields.io/badge/accuracy-98.5%25-success)](https://github.com/a-maliarov/amazon-captcha-solver/blob/master/accuracy.log)
![Timing](https://img.shields.io/badge/execution%20time-0.22s-success)
![Size](https://img.shields.io/badge/wheel%20size-1%20MB-informational)
[![Version](https://img.shields.io/pypi/v/amazoncaptcha?color=informational)](https://pypi.org/project/amazoncaptcha/)
[![Python version](https://img.shields.io/pypi/pyversions/amazoncaptcha)](https://pypi.org/project/amazoncaptcha/)
[![Downloads](https://img.shields.io/pypi/dm/amazoncaptcha?color=success)](https://pypi.org/project/amazoncaptcha/)

## Installation
```bash
pip install amazoncaptcha
```

## Quick Snippet
```python
from amazoncaptcha import AmazonCaptcha

captcha = AmazonCaptcha('captcha.jpg')
solution = captcha.solve()

# Or: solution = AmazonCaptcha('captcha.jpg').solve()
```

## Status
[![Status](https://img.shields.io/pypi/status/amazoncaptcha)](https://pypi.org/project/amazoncaptcha/)
[![Build Status](https://travis-ci.com/a-maliarov/amazon-captcha-solver.svg?branch=master)](https://travis-ci.com/a-maliarov/amazon-captcha-solver)
[![codecov](https://codecov.io/gh/a-maliarov/amazon-captcha-solver/branch/master/graph/badge.svg)](https://codecov.io/gh/a-maliarov/amazon-captcha-solver)
[![Requirements Status](https://requires.io/github/a-maliarov/amazon-captcha-solver/requirements.svg?branch=master)](https://requires.io/github/a-maliarov/amazon-captcha-solver/requirements/?branch=master)
[![Known Vulnerabilities](https://snyk.io/test/github/a-maliarov/amazon-captcha-solver/badge.svg?targetFile=requirements.txt)](https://snyk.io/test/github/a-maliarov/amazon-captcha-solver?targetFile=requirements.txt)
[![CodeFactor Grade](https://img.shields.io/codefactor/grade/github/a-maliarov/amazon-captcha-solver/master)](https://www.codefactor.io/repository/github/a-maliarov/amazon-captcha-solver/overview/master)

## Popular Usage
```python
from amazoncaptcha import AmazonCaptcha
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.amazon.com/errors/validateCaptcha')

captcha = AmazonCaptcha.from_webdriver(driver)
solution = captcha.solve()
```

## For Whom?
+ **Data extraction** and **web scraping** specialists could use this tool, obviously, to bypass the Amazon captcha.
+ **Machine learning** developers could use [captchas](https://github.com/a-maliarov/amazon-captcha-solver/tree/master/captchas) folder (currently contains **15000 solved captchas**) based on a demand.

## Issues
+ If you constantly receive 'Error' output, feel free to create an issue and describe details.
+ If you received an output, different from solution itself, 'Error' or 'Not solved', please, create an issue or contact me.
+ If you've somehow met an Exception, which you don't understand - you know what to do :)

## Happy Captcha Solving!

![Gif](https://github.com/a-maliarov/amazon-captcha-solver/blob/master/captchas.gif)

## Changes
+ **Version 0.0.10**:
  1. Reached 10000 training samples.
  2. Reached 90%+ accuracy.
+ **Version 0.0.11**:
  1. Fixed error with captcha images that were taken from BytesIO.
+ **Version 0.0.12**:
  1. Code adjustments and improvements.
  2. Program can now solve images where [last letter is corrupted](https://github.com/a-maliarov/amazon-captcha-solver/blob/master/errors/solved/corrupted-image-recognition.png).
+ **Version 0.0.13**:
  1. Added and tested 'from_webdriver' classmethod.
+ **Version 0.1.0**:
  1. 100,000 captchas crash test, accuracy is 98.5%.
+ **Version 0.1.1**:
  1. Code adjustments and improvements.
  2. Added tests.
+ **Version 0.1.3**:
  1. Code adjustments and improvements.
  2. Added vulnerabilities tests.
+ **Version 0.1.4**:
  1. Code adjustments and improvements.
  2. Added more tests.
