# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    # instantiate a results array
    result = []
    # instantiate a dictionary
    dictionary = {}
    # loop though the files
    for f in files:
        # split string according to "/"
        uncouple = f.split('/')
        # print(uncouple)
        # name of file is last element
        name_of_file = uncouple[-1]
        # if file name is not in dictionary set as empty array 
        if name_of_file not in dictionary:
            dictionary[name_of_file] = []
        # else append dict values
        dictionary[name_of_file].append(f)

    # loop thorugh queries
    for query in queries:
        # if query in dictionary
        if query in dictionary:
            # extend to results dictionary[q]
            result.extend(dictionary[query])
    
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
