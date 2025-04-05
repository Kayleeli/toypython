from ia5_kli_toypython.ia5_kli_toypython import str_split_one

import regex

def test_str_split_one_basic():
    """Test basic comma split."""
    result = str_split_one("alfa,bravo,charlie,delta", ",")
    expected = ["alfa", "bravo", "charlie", "delta"]
    assert result == expected
    print("test passed: Test basic comma split")

def test_str_split_one_maxsplit():
    """Test split with max number of splits."""
    result = str_split_one("a|b|c|d", r"\|", n=2)
    expected = ["a", "b", "c|d"]
    assert result == expected
    print("test passed: Test split with max number of splits")


def test_str_split_one_regex_escape():
    """Test splitting with escaped dot character."""
    result = str_split_one("192.168.0.1", regex.escape("."))
    expected = ["192", "168", "0", "1"]
    assert result == expected
    print("test passed: Test splitting with escaped dot character")

def test_str_split_one_non_string_input():
    """Test ValueError when input is not string."""
    try:
        str_split_one(123, ",")
        assert False, "Expected ValueError for non-string input"
    except ValueError:
        pass
    print("test passed: Test ValueError when input is not string.")
