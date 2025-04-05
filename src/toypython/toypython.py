import regex
from typing import List, Union

def str_split_one(string: str, pattern: Union[str, regex.Pattern], n: int = -1) -> List[str]:
    """
    Split a string into a list using the 'regex' package.

    Parameters
    ----------
    string : str
        The string to split.
    pattern : str or regex.Pattern
        The pattern to split by.
    n : int, optional, default: -1
        Maximum number of splits. If -1 (default), there is no limit.

    Returns
    -------
    List[str]
        A list of split substrings.

    Examples
    --------
    >>> str_split_one("alfa,bravo,charlie,delta", ",")
    """
    if not isinstance(string, str):
        raise ValueError("Input must be a string.")
    
    if n == -1:
        return regex.split(pattern, string)
    return regex.split(pattern, string, maxsplit=n)