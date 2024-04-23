def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    reduced_lst = []
    for item in lst:
        if (item):
            reduced_lst.append(item)
    return reduced_lst
