import regex
from typing import List, Union

def str_split_one(string: str, pattern: Union[str, regex.Pattern], n: int = -1) -> List[str]:
    """
    Split a string into a list using the 'regex' package.

    Parameters:
        string (str): A string to split.
        pattern (str or regex.Pattern): The pattern to split by.
        n (int, optional): Maximum number of splits. Default is -1 (no limit).

    Returns:
        List[str]: A list of split substrings.
    
    Examples:
        >>> str_split_one("alfa,bravo,charlie,delta", ",")
        ['alfa', 'bravo', 'charlie', 'delta']
        
        >>> str_split_one("alfa,bravo,charlie,delta", ",", n=2)
        ['alfa', 'bravo', 'charlie,delta']
        
        >>> str_split_one("192.168.0.1", regex.escape("."))
        ['192', '168', '0', '1']
    """
    if not isinstance(string, str):
        raise ValueError("Input must be a string.")
    
    if n == -1:
        return regex.split(pattern, string)
    return regex.split(pattern, string, maxsplit=n)

if __name__ == "__main__":
    # Example tests
    print(str_split_one("alfa,bravo,charlie,delta", ","))  
    print(str_split_one("alfa,bravo,charlie,delta", ",", n=2))  
    print(str_split_one("192.168.0.1", regex.escape(".")))
