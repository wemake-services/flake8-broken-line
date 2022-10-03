# flake8-broken-line

[![wemake.services](https://img.shields.io/badge/-wemake.services-green.svg?label=%20&logo=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAABGdBTUEAALGPC%2FxhBQAAAAFzUkdCAK7OHOkAAAAbUExURQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP%2F%2F%2F5TvxDIAAAAIdFJOUwAjRA8xXANAL%2Bv0SAAAADNJREFUGNNjYCAIOJjRBdBFWMkVQeGzcHAwksJnAPPZGOGAASzPzAEHEGVsLExQwE7YswCb7AFZSF3bbAAAAABJRU5ErkJggg%3D%3D)](https://wemake-services.github.io)
[![Build Status](https://github.com/wemake-services/flake8-broken-line/workflows/test/badge.svg?branch=master&event=push)](https://github.com/wemake-services/flake8-broken-line/actions?query=workflow%3Atest)
[![codecov](https://codecov.io/gh/wemake-services/flake8-broken-line/branch/master/graph/badge.svg)](https://codecov.io/gh/wemake-services/flake8-broken-line)
[![Python Version](https://img.shields.io/pypi/pyversions/flake8-broken-line.svg)](https://pypi.org/project/flake8-broken-line/)
[![PyPI version](https://badge.fury.io/py/flake8-broken-line.svg)](https://pypi.org/project/flake8-broken-line/)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)

Do not break the line! 🚨


## Installation

```bash
pip install flake8-broken-line
```

It is also a valuable part of [`wemake-python-styleguide`](https://github.com/wemake-services/wemake-python-styleguide).


## Code example

Things we check with this plugin:

```python
# String line breaks, use `()` or `"""` instead:

some_string = 'first line\
second line'

# Use a single line, `()`, or new variables instead:

if 1 == 1 and \
    2 == 2:
    print('Do not do that!')

# Do not use for method chaining:
some_object \
  .call_method(param1, param2) \
  .call_other(keyword=value) \
  .finalize()

# Instead use:
some_objects.call_method(
    param1, param2,
).call_other(
    keyword=value
).finalize()

```


## Error codes

| Error code |                   Description                  |
|:----------:|:----------------------------------------------:|
|    N400    | Found backslash that is used for line breaking |


## License

MIT.
