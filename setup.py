import setuptools

def readme(logo_end_line=14):
    """Drops the logo from README file before pushing to PyPi"""

    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = "".join(fh.readlines()[logo_end_line:])

    return long_description

setuptools.setup(
    name="amazoncaptcha",
    version="0.4.5",
    description="Pure Python, lightweight, Pillow-based solver for Amazon's text captcha.",
    packages=['amazoncaptcha'],
    py_modules=['devtools', 'exceptions', 'solver', 'utils'],
    include_package_data = True,
    package_data = {
        '': ['*.json'],
        'amazoncaptcha': ['training_data/*.*'],
    },
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Information Technology",
        "Topic :: Internet :: WWW/HTTP :: Browsers"
    ],
    long_description=readme(),
    long_description_content_type="text/markdown",
    install_requires = [
        "pillow ~= 7.2.0",
        "requests ~= 2.24.0",
        "selenium ~= 3.141.0"
    ],
    author="Anatolii Maliarov",
    author_email="tly.mov@gmail.com",
    url="https://github.com/a-maliarov/amazon-captcha-solver",
)

