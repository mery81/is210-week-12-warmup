#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02 module"""


import datetime


class InvalidAgeError(Exception):
    """Age exception class."""
    pass


def get_age(birthyear):
    """Function that calculate the age up to date.

    Args:
        birthday (int): the year of birth.

    Return:
        The calculated age or the invalid error message.

    Examples:
        >>> get_age(2099)
        Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        __main__.InvalidAgeError

        >>> get_age(1998)
        18
    """
    age = datetime.datetime.now().year - birthyear
    if age >= 0:
        return age
    else:
        raise InvalidAgeError()
