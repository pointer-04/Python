def upper(word: str) -> str:
    """
    Will convert the entire string to uppercase letters

    >>> upper("wow")
    'WOW'
    >>> upper("Hello")
    'HELLO'
    >>> upper("WHAT")
    'WHAT'
    >>> upper("wh[]32")
    'WH[]32'
    """

    # converting to ascii value int value and checking to see if char is a lower letter
    # if it is a capital letter it is getting shift by 32 which makes it a capital case
    # letter
    return "".join(chr(ord(char) - 32) if "a" <= char <= "z" else char for char in word)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    
''' 
alternate way of converting all letters to upper in a string 
using str.upper() builtin method of python
upper() takes in no parameters. 
The general syntax is : string.upper()

stringToConvert = 'king'
then, stringToConvert.upper() >>> 'KING'

strinToConvert = 'KiNg'
then, stringToConvert.upper() >>> 'KING'
'''
stringToConvert=input()
print(stringToConvert.upper())
