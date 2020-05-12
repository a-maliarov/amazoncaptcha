# Amazon Captcha Solver
Pure Python, non-OCR, lightweight, [Pillow](https://github.com/python-pillow/Pillow) based solver for the [Amazon text captcha](https://www.amazon.com/errors/validateCaptcha).

![Accuracy](https://img.shields.io/badge/accuracy-87.9%25-success)
![Timing](https://img.shields.io/badge/execution%20time-0.4s-red)
![Size](https://img.shields.io/badge/package%20size-2%20MB-informational)
![Version](https://img.shields.io/pypi/v/amazoncaptcha?color=information)
![Python version](https://img.shields.io/pypi/pyversions/amazoncaptcha)

## Installation
```bash
pip install amazoncaptcha
```

## Quick Snippet
```python
from amazoncaptcha import AmazonCaptcha

solution = AmazonCaptcha('captcha.jpg').solve()
```

## For who?
+ **Data extraction** and **web scraping** specialists could use this tool, obviously, to bypass the Amazon captcha.
+ **Machine learning** developers could use *captchas* folder (currently contains **6000 solved captchas**) based on a demand.
