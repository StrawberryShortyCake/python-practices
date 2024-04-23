def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    letter_freq_dictionary = {}

    for letter in phrase:
        count = letter_freq_dictionary.get(letter, 0)
        letter_freq_dictionary[letter] = count+1

    return letter_freq_dictionary
