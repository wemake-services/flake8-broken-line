# -*- coding: utf-8 -*-

"""Module with correct type annotations."""

multiline_string = (
    'one'
    'two'
    '\n'
    '\\'
)

# A remote path can be entered.  e.g.:  \\server\

raw_string = r'\\'

second_multiline = """
This is a text with \a and trailing backslash char: \\
"""

second_multiline = """
This is trailing backslash line break: \
and next line.
"""


third_multiline = """
This is trailing backslash line break with extra spaces: \
and next line.
"""

fourth_multiline = """\
This is a multiline block with no prepended newline
and next line.
"""

fifth_multiline = '''\
This is a multiline block with no prepended newline
and next line.
'''
