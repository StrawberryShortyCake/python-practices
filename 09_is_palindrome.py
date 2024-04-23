import math


def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """

    # reduce whitespace and rid caps with .lower()
    # math.ceil(len(str)/2)-1
    # while we haven't hit ^ compare the two ends

    clean_phrase = phrase.lower().replace(" ", "")
    index_left = 0

    # print(math.ceil(len(clean_phrase)/2))

    while index_left < math.ceil(len(clean_phrase)/2):
        if (clean_phrase[index_left] !=
                clean_phrase[len(clean_phrase) - 1 - index_left]):
            return False
        index_left += 1

    return True
