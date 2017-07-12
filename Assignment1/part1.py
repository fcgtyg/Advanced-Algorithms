def bag_switch(outcomes):
    def search(array, first=0):  # Inner function to handle variable exchange between recursion steps.
        bag = ["W", "R", "O"]  # Searching values
        i = 0
        if array[first + i] in bag:  # I feel lucky today :D
            return 0
        else:
            while i >= 0:  # Lookup process that lasts theoretically forever.
                try:
                    if array[first + (2 ** i)] in bag:
                        if i == 0:  # If our sublist's length equals to 1, we found the target.
                            return first+(2**i)
                        last = first + (2**i)  # Last index of sub
                        return search(array, first + (2**(i-1)))
                except IndexError:  # Just in case if the list has index limit.
                    return None
                i += 1

    return search(outcomes)