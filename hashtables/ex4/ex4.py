def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    # instantiate an array for results
    result = []
    # instantiate a dictionary
    dictionary = {}
    # loop though array of positive and neg numbers
    for i in a:
        # only works when i set dict value to something.
        dictionary[i] = None
        # if -i is in dictionary and it is i not = to zero
        if -i in dictionary and i != 0:
        # append to your results make sure the value is the absolute i.e. abs()
            result.append(abs(i))

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
