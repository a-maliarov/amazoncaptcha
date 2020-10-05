# -*- coding: utf-8 -*-

"""
amazoncaptcha.exceptions
~~~~~~~~~~~~~~~~~~~

This module contains the set of amazoncaptcha's exceptions.
"""

#--------------------------------------------------------------------------------------------------------------

class ContentTypeError(Exception):
    """
    Requested url, which was supposed to be the url to the captcha image
    contains unsupported content type within response headers.
    """

    def __init__(self, content_type):
        self.content_type = content_type

    def __str__(self):
        return f'"{self.content_type}" is not supported as a Content-Type. Cannot extract the image.'

#--------------------------------------------------------------------------------------------------------------
