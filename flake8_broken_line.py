# -*- coding: utf-8 -*-

import re
from typing import Optional, Tuple

import pkg_resources

pkg_name = 'flake8-broken-line'

#: We store the version number inside the `pyproject.toml`:
pkg_version: str = pkg_resources.get_distribution(pkg_name).version

INVALID_LINE_BREAK = re.compile(r'(?<!\\)\\$', re.M)

N400 = 'N400: Found backslash that is used for line breaking'


def check_line_breaks(physical_line: str) -> Optional[Tuple[int, str]]:
    """Functional ``flake8`` plugin to check for backslashes."""
    if INVALID_LINE_BREAK.search(physical_line.rstrip()):
        return 0, N400
    return None


# Flake8 API definition:
check_line_breaks.name = pkg_name  # type: ignore
check_line_breaks.version = pkg_version  # type: ignore
