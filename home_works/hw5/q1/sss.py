def foo():
    """
    >>> foo()
    None
    """
    return None

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())