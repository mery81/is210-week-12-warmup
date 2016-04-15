#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01 module"""


def simple_lookup(var1, var2):
    """Function that contain indexes.

    Args:
        var1 (mixed): index to be accessed and returned in warning message.
        var2 (mixed): secong index.

    Returns:
        var1: index will be returned with warning message.

    Examples:
        >>> simple_lookup([1,2], 4)
        Warning: Your index/key doesn't exist.
        {1,2}
    """
    try:
        return var1[var2]
    except:
        print "Warning: Your index/key doesn't exist. \n {0}".format(var1)
