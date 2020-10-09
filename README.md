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
  >>>solution                                             | ▓▓                            Response 0.24s
  "AmznCaptcha"                                            \▓▓                            Accuracy 99.9%
```
The motivation behind the creation of this library is taking its start from the genuinely simple idea: "**I don't want to use pytesseract or some other non-amazon-specific OCR services, nor do I want to install some executables to just solve a captcha. I desire to get a solution within 1-2 lines of code without any heavy add-ons, using a pure Python.**"

---
Pure Python, lightweight, [Pillow](https://github.com/python-pillow/Pillow)-based solver for [Amazon's text captcha](https://www.amazon.com/errors/validateCaptcha).

[![Accuracy](https://img.shields.io/badge/success%20rate-99.9%25-success)](https://github.com/a-maliarov/amazon-captcha-solver/blob/master/ext/accuracy.log)
![Timing](https://img.shields.io/badge/response%20time-0.2s-success)
[![Size](https://img.shields.io/badge/wheel%20size-0.9%20MB-informational)](https://pypi.org/project/amazoncaptcha/)
[![Version](https://img.shields.io/pypi/v/amazoncaptcha?color=informational)](https://pypi.org/project/amazoncaptcha/)
[![Python version](https://img.shields.io/badge/python-3.6%2B-informational)](https://pypi.org/project/amazoncaptcha/)
[![Downloads](https://img.shields.io/pypi/dm/amazoncaptcha?color=success)](https://pypi.org/project/amazoncaptcha/)

## Recent News
+ *October 8, 2020*: tested and approved compatibility with Chromedriver 86.0.4240.22
+ *October 7, 2020*: tested and approved compatibility with Python 3.9
+ *September 20, 2020*: dropped support for Python 3.5

## Installation
```bash
pip install amazoncaptcha
```

## Quick Snippet
An example of the constructor usage. Scroll a bit down to see some tasty class methods.
```python
from amazoncaptcha import AmazonCaptcha

captcha = AmazonCaptcha('captcha.jpg')
solution = captcha.solve()

# Or: solution = AmazonCaptcha('captcha.jpg').solve()
```

## Status
[![Status](https://img.shields.io/pypi/status/amazoncaptcha)](https://pypi.org/project/amazoncaptcha/)
[![Build Status](https://travis-ci.com/a-maliarov/amazon-captcha-solver.svg?branch=master)](https://travis-ci.com/a-maliarov/amazon-captcha-solver)
[![Documentation Status](https://readthedocs.org/projects/amazoncaptcha/badge/?version=latest)](https://amazoncaptcha.readthedocs.io/en/latest/)
[![Requirements Status](https://requires.io/github/a-maliarov/amazon-captcha-solver/requirements.svg?branch=master)](https://requires.io/github/a-maliarov/amazon-captcha-solver/requirements/?branch=master)
[![Code Coverage](https://img.shields.io/codecov/c/gh/a-maliarov/amazon-captcha-solver?label=code%20coverage)](https://codecov.io/gh/a-maliarov/amazon-captcha-solver)
[![CodeFactor Grade](https://img.shields.io/codefactor/grade/github/a-maliarov/amazon-captcha-solver/master)](https://www.codefactor.io/repository/github/a-maliarov/amazon-captcha-solver/overview/master)

## Usage and Class Methods
Browsing Amazon using `selenium` and stuck on captcha? The class method below will do all the "dirty" work of extracting an image from the webpage for you. Practically, it takes a screenshot from your webdriver, crops the captcha, and stores it into bytes array, which is then used to create an `AmazonCaptcha` instance. This also means avoiding any local savings.
```python
from amazoncaptcha import AmazonCaptcha
from selenium import webdriver

driver = webdriver.Chrome() # This is a simplified example
driver.get('https://www.amazon.com/errors/validateCaptcha')

captcha = AmazonCaptcha.fromdriver(driver)
solution = captcha.solve()
```

If you are not using `selenium` or the previous method is not just the case for you, it is possible to use a captcha link directly. This class method will request the url, check the content type and store the response content into bytes array to create an instance of `AmazonCaptcha`.
```python
from amazoncaptcha import AmazonCaptcha

link = 'https://images-na.ssl-images-amazon.com/captcha/usvmgloq/Captcha_kwrrnqwkph.jpg'

captcha = AmazonCaptcha.fromlink(link)
solution = captcha.solve()
```

In addition, if you are a machine learning or neural network developer and are looking for some training data, check [this](https://github.com/a-maliarov/amazon-captcha-database) repository, which was created to store images and other non-script data for the solver.

## Help the Development
If you are willing to help the development, consider setting `keep_logs` argument of the `solve` method to `True`. Here is the example, if you are using `fromdriver` class method. If set to `True`, all the links of the unsolved captcha will be stored, so later you can [open the issue and send the logs](https://github.com/a-maliarov/amazon-captcha-solver/issues/new?assignees=a-maliarov&labels=training+data&template=send_logs.md&title=Add+training+data).
```python
from amazoncaptcha import AmazonCaptcha
from selenium import webdriver

driver = webdriver.Chrome() # This is a simplified example
driver.get('https://www.amazon.com/errors/validateCaptcha')

captcha = AmazonCaptcha.fromdriver(driver)
solution = captcha.solve(keep_logs=True)
```

If you have any suggestions or ideas of additional instances and methods, which you would like to see in this library, please, feel free to contact the owner via email or fork'n'pull to repository. Any contribution is highly appreciated!

## Additional
+ If you want to see the [**History of Changes**](https://github.com/a-maliarov/amazon-captcha-solver/blob/master/HISTORY.md), [**Code of Conduct**](https://github.com/a-maliarov/amazon-captcha-solver/blob/master/.github/CODE_OF_CONDUCT.md), [**Contributing Policy**](https://github.com/a-maliarov/amazon-captcha-solver/blob/master/.github/CONTRIBUTING.md), or [**License**](https://github.com/a-maliarov/amazon-captcha-solver/blob/master/LICENSE), use these inline links to navigate based on your needs.
+ If you are facing any errors, please, report your situation via an issue.
+ This project is for educational and research purposes only. Any actions and/or activities related to the material contained on this GitHub Repository is solely your responsibility. The author will not be held responsible in the event any criminal charges be brought against any individuals misusing the information in this GitHub Repository to break the law.
