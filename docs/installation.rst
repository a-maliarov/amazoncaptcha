Installation
============

Warnings
--------

.. warning:: AmazonCaptcha uses Pillow library to operate with images. Pillow and PIL cannot co-exist in the same environment. Before installing AmazonCaptcha (which will automatically install Pillow), please uninstall PIL.

Python Support
--------------

AmazonCaptcha supports all the versions of Python after 3.5

+-----------------------------+-------+-------+-------+-------+-------+-------+
| **Python**                  |**3.9**|**3.8**|**3.7**|**3.6**|**3.5**|**3.4**|
+-----------------------------+-------+-------+-------+-------+-------+-------+
| AmazonCaptcha >= 0.5.0      |  Yes  |  Yes  |  Yes  |  Yes  |  No   |  No   |
+-----------------------------+-------+-------+-------+-------+-------+-------+
| AmazonCaptcha 0.4.0 - 0.4.9 |  Yes  |  Yes  |  Yes  |  Yes  |  No   |  No   |
+-----------------------------+-------+-------+-------+-------+-------+-------+

Basic Installation
------------------

Install AmazonCaptcha from PyPi with :command:`pip`::

    pip install amazoncaptcha

Install AmazonCaptcha from GitHub with :command:`git`: and :command:`pip`::

    pip install git+https://github.com/a-maliarov/amazon-captcha-solver.git

Install AmazonCaptcha from GitHub with :command:`git`::

    git clone https://github.com/a-maliarov/amazon-captcha-solver.git
    python setup.py install
