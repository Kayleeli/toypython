# toypython

Python version of toy.R, to make some common tasks with string manipulation and regular expressions a bit easier. 

## Installation

```bash
$ pip install toypython
```

## Usage

The str_split_one function splits a string into a list of substrings using a specified delimiter or regular expression pattern, with an optional limit on the number of splits.

```python
from toypython.toypython import str_split_one

result = str_split_one("alfa,bravo,charlie,delta", ",")
print(result)
```

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`toypython` was created by Kaylee Li. It is licensed under the terms of the MIT license.

## Credits

`toypython` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
