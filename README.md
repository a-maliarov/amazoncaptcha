# Amazon Captcha Solver
Pure Python, non-OCR, lightweight, [Pillow](https://github.com/python-pillow/Pillow)-based solver for the [Amazon image captcha](https://www.amazon.com/errors/validateCaptcha).

![Accuracy](https://img.shields.io/badge/accuracy-93.8%25-success)
![Timing](https://img.shields.io/badge/execution%20time-0.4s-success)
![Size](https://img.shields.io/badge/size-2%20MB-informational)
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

## For whom?
+ **Data extraction** and **web scraping** specialists could use this tool, obviously, to bypass the Amazon captcha.
+ **Machine learning** developers could use *captchas* folder (currently contains **10000 solved captchas**) based on a demand.

## Happy Captcha Solving!

![Gif](https://github.com/a-maliarov/amazon-captcha-solver/blob/master/captchas.gif)

## Logs
+ **Version 0.0.10**:
  1. Reached 10000 training samples.
  2. Reached 90%+ accuracy.
