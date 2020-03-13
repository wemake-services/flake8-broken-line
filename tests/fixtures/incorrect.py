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

1 + some \
    .call()
