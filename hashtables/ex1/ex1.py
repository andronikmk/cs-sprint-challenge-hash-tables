def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    dictionary = {}
    for i in range(length):
        dictionary[weights[i]] = i

    for i in range(length):
        limit_weights = limit - weights[i]
        if limit_weights in dictionary:
            zeros = max(i, dictionary[limit_weights])
            ones = min(i, dictionary[limit_weights])
            return (zeros, ones)
    return None

# weights = [4,6,10,15,16]
# length = 5
# limit = 21
# get_indices_of_item_weights(weights, length, limit)