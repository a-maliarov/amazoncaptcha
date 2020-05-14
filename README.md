# Amazon Captcha Solver
Pure Python, non-OCR, lightweight, [Pillow](https://github.com/python-pillow/Pillow)-based solver for the [Amazon image captcha](https://www.amazon.com/errors/validateCaptcha).

![Accuracy](https://img.shields.io/badge/accuracy-98.5%25-success)
![Timing](https://img.shields.io/badge/execution%20time-0.22s-success)
![Size](https://img.shields.io/badge/wheel%20size-1%20MB-informational)
![Version](https://img.shields.io/pypi/v/amazoncaptcha?color=informational)
![Python version](https://img.shields.io/pypi/pyversions/amazoncaptcha)
![Downloads](https://img.shields.io/pypi/dm/amazoncaptcha?color=success)

## Installation
```bash
pip install amazoncaptcha
```

## Quick Snippet
```python
from amazoncaptcha import AmazonCaptcha

solution = AmazonCaptcha('captcha.jpg').solve()
```

## Popular Usage
```python
from amazoncaptcha import AmazonCaptcha
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.amazon.com/errors/validateCaptcha')

captcha = AmazonCaptcha.from_webdriver(driver) # Just make sure zoom level is standard
solution = captcha.solve()
```

## For Whom?
+ **Data extraction** and **web scraping** specialists could use this tool, obviously, to bypass the Amazon captcha.
+ **Machine learning** developers could use [captchas](https://github.com/a-maliarov/amazon-captcha-solver/tree/master/captchas) folder (currently contains **12000 solved captchas**) based on a demand.

## Contribution
+ If you checked the code and you know the way or have any ideas, how to make it better, feel free to fork-n-pull or contact me. Thank you!
+ If you want to help with current problems, please check this [file](https://github.com/a-maliarov/amazon-captcha-solver/blob/master/errors/HELPME.md).

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
