def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    def upper_to_lower(letter):
        return letter.lower()

    def lower_to_upper(letter):
        return letter.upper()

    commands = {
        True: upper_to_lower,
        False: lower_to_upper
    }

    flipped_phrase = ""

    for idx, letter in enumerate(phrase):
        if letter == to_swap.upper() or letter == to_swap.lower():
            flipped_phrase += commands[letter.isupper()](letter)
        else:
            flipped_phrase += letter

    return flipped_phrase
