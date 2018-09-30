# -*- coding: utf-8 -*-

"""Module with incorrect type annotations."""

multiline_sting = 'first line\
second line'

if multiline_sting == '' and \
    1 == 1:
    print('Error!'\
    )

multiline_sting\
    .rstrip()\
    .lstrip()


second_multiline = """
This is trailing backslash line break: \
and next line.
"""


third_multiline = """
This is trailing backslash line break with extra spaces: \   
and next line.
"""
