def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE

    UNDERSTAND: Find two values whose sum is equally the limit. Ex. limit = 21.
    """
    # Your code here
    # instantiate a dict
    dictionary = {}
    # loop through length
    for i in range(length):
        # set dict value to index
        dictionary[weights[i]] = i
    # loop through length
    for i in range(length):
        # get limit weights using formula in README.md
        limit_weights = limit - weights[i]
        # check if limit weight in dict
        if limit_weights in dictionary:
            # find max (look up how max/min method works...)
            # To find the largest item in an iterable, we use this syntax:
            # max(iterable, *iterables, key, default)
            zeros = max(i, dictionary[limit_weights])
            # find min
            ones = min(i, dictionary[limit_weights])
            # return tuple
            return (zeros, ones)
    # why was this here
    return None

# weights = [4,6,10,15,16]
# length = 5
# limit = 21
# get_indices_of_item_weights(weights, length, limit)