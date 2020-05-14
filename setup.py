import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="amazoncaptcha",
    version="0.1.0",
    description="Solving captchas never ends...",
    packages=['amazoncaptcha'],
    py_modules=['objects'],
    include_package_data = True,
    package_data = {
        '': ['*.json'],
        'amazoncaptcha': ['data/*.*'],
    },
    classifiers=[
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires = [
        "pillow ~= 7.1.2"
    ],
    author="Anatolii Maliarov",
    author_email="tly.mov@gmail.com",
    url="https://github.com/a-maliarov/Amazon-Captcha-Solver",
)
