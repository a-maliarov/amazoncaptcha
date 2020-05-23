import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="amazoncaptcha",
    version="0.3.9",
    description="Pure Python, lightweight, Pillow-based solver for the Amazon's text captcha.",
    packages=['amazoncaptcha'],
    py_modules=['objects'],
    include_package_data = True,
    package_data = {
        '': ['*.json'],
        'amazoncaptcha': ['data/*.*'],
    },
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable"
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires = [
        "pillow ~= 7.1.2",
        "requests ~= 2.23.0"
    ],
    author="Anatolii Maliarov",
    author_email="tly.mov@gmail.com",
    url="https://github.com/a-maliarov/amazon-captcha-solver",
)
