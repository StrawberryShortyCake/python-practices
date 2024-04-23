def list_manipulation(lst, command, location, value=None):
    """Mutate lst to add/remove from beginning or end.

    - lst: list of values
    - command: command, either "remove" or "add"
    - location: location to remove/add, either "beginning" or "end"
    - value: when adding, value to add

    remove: remove item at beginning or end, and return item removed

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'remove', 'end')
        3

        >>> list_manipulation(lst, 'remove', 'beginning')
        1

        >>> lst
        [2]

    add: add item at beginning/end, and return list

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'add', 'beginning', 20)
        [20, 1, 2, 3]

        >>> list_manipulation(lst, 'add', 'end', 30)
        [20, 1, 2, 3, 30]

        >>> lst
        [20, 1, 2, 3, 30]

    Invalid commands or locations should return None:

        >>> list_manipulation(lst, 'foo', 'end') is None
        True

        >>> list_manipulation(lst, 'add', 'dunno') is None
        True
    """
    def add_beginning():
        lst[:0] = [value]
        return lst

    def add_end():
        lst.append(value)
        return lst

    def remove_beginning():
        return lst.pop(0)

    def remove_end():
        return lst.pop(len(lst)-1)

    locations = {
        "beginning":
            {
                "add": add_beginning,
                "remove": remove_beginning
            },
        "end": {
                "add": add_end,
                "remove": remove_end
        }
    }

    if (locations.get(location) == None or
            locations[location].get(command) == None):
        return None

    return locations[location][command]()
