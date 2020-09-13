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
  >>>solution                                             | ▓▓                            Version 0.3.10
  "AmznCaptcha"                                            \▓▓                            Accuracy 99.9%
```
Motivation behind creation of this library is taking its start from the genuinely simple idea: "***I don't want to use pytesseract or some other non-amazon-specific OCR services, nor do I want to install some executables to just solve a captcha. My desire is to get a solution within 1-2 lines of code without any heavy add-ons. Using a pure Python.***"

---
Pure Python, lightweight, [Pillow](https://github.com/python-pillow/Pillow)-based solver for the [Amazon's text captcha](https://www.amazon.com/errors/validateCaptcha).

[![Accuracy](https://img.shields.io/badge/accuracy-99.9%25-success)](https://github.com/a-maliarov/amazon-captcha-solver/blob/master/ext/accuracy.log)
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
For **data extraction** or **web scraping** specialists, who is crawling Amazon by using `selenium`, the classmethod below will do all the "dirty" work of extracting an image from webpage for you. Practically, it takes a screenshot from your webdriver, crops the captcha and stores it into bytes array, which is then used to create an `AmazonCaptcha` instance. This also means avoiding any local savings.
```python
from amazoncaptcha import AmazonCaptcha
from selenium import webdriver

driver = webdriver.Chrome() # This is a simplified example
driver.get('https://www.amazon.com/errors/validateCaptcha')

captcha = AmazonCaptcha.from_webdriver(driver)
solution = captcha.solve()
```

On the other hand, if you are **machine learning** or **neural networks** developer and are looking for some training data, firstly check the [captchas](https://github.com/a-maliarov/amazon-captcha-solver/tree/master/captchas) folder. It currently contains **13000 solved captchas with unique patterns**. For more solved images, consider using `AmazonCaptchaCollector` instance with a really simple API sampled below. An image will be stored, only if there is a 100% answer. However, if you've noticed a wrong solution, please, create an issue using corresponding template.
```python
from amazoncaptcha import AmazonCaptchaCollector

output_folder = '/path/to/output/folder' # where you want to store captchas
target = 100000 # final number of solved captchas you want to get
processes = 10 # number of simultaneous processes

if __name__ == '__main__':
    collector = AmazonCaptchaCollector(output_folder = output_folder)
    collector.start(target = target, processes = processes)
```
If you have any suggestions or ideas of additional instances and methods, which you would like to see in this library, please, feel free to contact the owner via email or fork'n'pull to repository. Any contribution is highly appreciated!

## Additional
+ Just FYI, `pip` will install only module itself. However, if you are using `git clone`, be aware that you will also clone 50 MB of captchas, currently located in the repository.
+ If you want to see the [**History of Changes**](https://github.com/a-maliarov/amazon-captcha-solver/blob/master/HISTORY.md), [**Code of Conduct**](https://github.com/a-maliarov/amazon-captcha-solver/blob/master/.github/CODE_OF_CONDUCT.md), [**Contributing Policy**](https://github.com/a-maliarov/amazon-captcha-solver/blob/master/.github/CONTRIBUTING.md) or [**License**](https://github.com/a-maliarov/amazon-captcha-solver/blob/master/LICENSE), use these inline links to navigate based on your need.
+ If you are facing any errors, please, report your situation via an issue.
