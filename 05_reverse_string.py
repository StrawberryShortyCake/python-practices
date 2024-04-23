def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    reversed_result = ""
    letter_index = len(phrase)-1
    while letter_index > -1:
        reversed_result += phrase[letter_index]
        letter_index -= 1

    return reversed_result
