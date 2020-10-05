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
  >>>solution                                             | ▓▓                            Version  0.4.2
  "AmznCaptcha"                                            \▓▓                            Accuracy 99.9%
```
The motivation behind the creation of this library is taking its start from the genuinely simple idea: "**I don't want to use pytesseract or some other non-amazon-specific OCR services, nor do I want to install some executables to just solve a captcha. I desire to get a solution within 1-2 lines of code without any heavy add-ons, using a pure Python.**"

---
Pure Python, lightweight, [Pillow](https://github.com/python-pillow/Pillow)-based solver for [Amazon's text captcha](https://www.amazon.com/errors/validateCaptcha).

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

In addition, if you are a machine learning or neural network developer and are looking for some training data, firstly check the [captchas](https://github.com/a-maliarov/amazon-captcha-solver/tree/master/captchas) folder. It currently contains **13000 solved captchas with unique patterns**. For more solved images, consider using `AmazonCaptchaCollector` instance with a really simple API sampled below. An image will be stored, only if there is a 100% answer. However, if you've noticed a wrong solution, please, create an issue using the corresponding template.
```python
from amazoncaptcha import AmazonCaptchaCollector

output_folder = '/path/to/output/folder' # where you want to store captchas
target = 100000 # final number of solved captchas you want to get
processes = 10 # number of simultaneous processes

if __name__ == '__main__':
    collector = AmazonCaptchaCollector(output_folder)
    collector.start(target, processes)
```

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
+ Just FYI, `pip` will install only the module itself. However, if you are using `git clone`, be aware that you will also clone 50 MB of captchas currently located in the repository.
+ If you want to see the [**History of Changes**](https://github.com/a-maliarov/amazon-captcha-solver/blob/master/HISTORY.md), [**Code of Conduct**](https://github.com/a-maliarov/amazon-captcha-solver/blob/master/.github/CODE_OF_CONDUCT.md), [**Contributing Policy**](https://github.com/a-maliarov/amazon-captcha-solver/blob/master/.github/CONTRIBUTING.md), or [**License**](https://github.com/a-maliarov/amazon-captcha-solver/blob/master/LICENSE), use these inline links to navigate based on your needs.
+ If you are facing any errors, please, report your situation via an issue.
+ This project is for educational and research purposes only. Any actions and/or activities related to the material contained on this GitHub Repository is solely your responsibility. The author will not be held responsible in the event any criminal charges be brought against any individuals misusing the information in this GitHub Repository to break the law.
---

## Happy Captcha Solving!

![Gif](https://github.com/a-maliarov/amazon-captcha-solver/blob/master/ext/captchas.gif)
