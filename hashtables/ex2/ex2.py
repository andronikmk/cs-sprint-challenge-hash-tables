#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # becuase first and last flight has a destination of None therefore you
    # instantiate with None 
    route = [None] * length
    # presumably we need a hash table at some point
    dictionary = {}
    # let's check for ticket in tickets
    for tic in tickets:
        # inside the dictionary let's set the key as source and value as destination
        # for every iteration of the for loop
        dictionary[tic.source] = tic.destination
    pass


    return route