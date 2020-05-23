```python
  ______                                  ______                      __              __                
 /      \                                /      \                    |  \            |  \               
|  ▓▓▓▓▓▓\______ ____  ________ _______ |  ▓▓▓▓▓▓\ ______   ______  _| ▓▓_    _______| ▓▓____   ______  
| ▓▓__| ▓▓      \    \|        \       \| ▓▓   \▓▓|      \ /      \|   ▓▓ \  /       \ ▓▓    \ |      \ 
| ▓▓    ▓▓ ▓▓▓▓▓▓\▓▓▓▓\\▓▓▓▓▓▓▓▓ ▓▓▓▓▓▓▓\ ▓▓       \▓▓▓▓▓▓\  ▓▓▓▓▓▓\\▓▓▓▓▓▓ |  ▓▓▓▓▓▓▓ ▓▓▓▓▓▓▓\ \▓▓▓▓▓▓\
| ▓▓▓▓▓▓▓▓ ▓▓ | ▓▓ | ▓▓ /    ▓▓| ▓▓  | ▓▓ ▓▓   __ /      ▓▓ ▓▓  | ▓▓ | ▓▓ __| ▓▓     | ▓▓  | ▓▓/      ▓▓
| ▓▓  | ▓▓ ▓▓ | ▓▓ | ▓▓/  ▓▓▓▓_| ▓▓  | ▓▓ ▓▓__/  \  ▓▓▓▓▓▓▓ ▓▓__/ ▓▓ | ▓▓|  \ ▓▓_____| ▓▓  | ▓▓  ▓▓▓▓▓▓▓
| ▓▓  | ▓▓ ▓▓ | ▓▓ | ▓▓  ▓▓    \ ▓▓  | ▓▓\▓▓    ▓▓\▓▓    ▓▓ ▓▓    ▓▓  \▓▓  ▓▓\▓▓     \ ▓▓  | ▓▓\▓▓    ▓▓
 \▓▓   \▓▓\▓▓  \▓▓  \▓▓\▓▓▓▓▓▓▓▓\▓▓   \▓▓ \▓▓▓▓▓▓  \▓▓▓▓▓▓▓ ▓▓▓▓▓▓▓    \▓▓▓▓  \▓▓▓▓▓▓▓\▓▓   \▓▓ \▓▓▓▓▓▓▓
                                                          | ▓▓                                          
  >>>solution                                             | ▓▓                            Version  0.3.7
  "AmznCptch"                                              \▓▓                            Accuracy 99.9%
```
Motivation behind creation of this library is taking its start from the genuinely simple idea: "***I don't want to use pytesseract or some other non-amazon-specific OCR services, nor do I want to install some executables to just solve a captcha. My desire is to get a solution within 1-2 lines of code without any heavy add-ons. Using a pure Python.***"

---
Pure Python, lightweight, [Pillow](https://github.com/python-pillow/Pillow)-based solver for the [Amazon's text captcha](https://www.amazon.com/errors/validateCaptcha).

[![Accuracy](https://img.shields.io/badge/accuracy-99.9%25-success)](https://github.com/a-maliarov/amazon-captcha-solver/blob/master/accuracy.log)
![Timing](https://img.shields.io/badge/response%20time-0.2s-success)
[![Size](https://img.shields.io/badge/wheel%20size-0.9%20MB-informational)](https://github.com/a-maliarov/amazon-captcha-solver/releases/tag/v0.3.0)
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
[![codecov](https://img.shields.io/codecov/c/gh/a-maliarov/amazon-captcha-solver)](https://codecov.io/gh/a-maliarov/amazon-captcha-solver)
[![Requirements Status](https://requires.io/github/a-maliarov/amazon-captcha-solver/requirements.svg?branch=master)](https://requires.io/github/a-maliarov/amazon-captcha-solver/requirements/?branch=master)
[![CodeFactor Grade](https://img.shields.io/codefactor/grade/github/a-maliarov/amazon-captcha-solver/master)](https://www.codefactor.io/repository/github/a-maliarov/amazon-captcha-solver/overview/master)
![Implementation](https://img.shields.io/pypi/implementation/amazoncaptcha)

## Usage
If you are **data extraction** or **web scraping** specialist, who is crawling Amazon by using `selenium`, this classmethod will do all the "dirty" work of extracting an image from webpage for you. Practically, it takes a screenshot from your webdriver, crops the captcha and stores it into bytes array, which is then used to create an AmazonCaptcha instance. This also means avoiding any local savings.
```python
from amazoncaptcha import AmazonCaptcha
from selenium import webdriver

driver = webdriver.Chrome() # This is a simplified example
driver.get('https://www.amazon.com/errors/validateCaptcha')

captcha = AmazonCaptcha.from_webdriver(driver)
solution = captcha.solve()
```

## For Whom?
+ **Data extraction** and **web scraping** specialists could use this tool, obviously, to bypass the Amazon captcha.
+ **Machine learning** developers could use [captchas](https://github.com/a-maliarov/amazon-captcha-solver/tree/master/captchas) folder (currently contains **13000 unique solved captchas**) based on a demand.

## Issues
+ If you constantly receive 'Not solved' output, feel free to create an issue and describe details.
+ If you received an output, different from solution itself or 'Not solved', please, create an issue or contact me.
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
  2. Program can now solve images where last letter is corrupted.
+ **Version 0.0.13**:
  1. Added and tested 'from_webdriver' classmethod.
+ **Version 0.1.0**:
  1. 100,000 captchas crash test, accuracy is 98.5%.
+ **Version 0.1.1 - 0.1.5**:
  1. Code adjustments and improvements.
  2. Added tests.
+ **Version 0.2.0**:
  1. Second crash test through 120k+ captchas.
  2. Accuracy increased to 99.1%
  3. Code coverage is 100%
+ **Version 0.3.0**:
  1. Program can now solve images where letters are intercepted.
  2. Third crash test through 140k+ captchas.
  3. Accuracy increased to 99.998%
