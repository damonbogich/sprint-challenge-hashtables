#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """

    ticket_dict = {}

    for ticket in tickets:
        if ticket.source not in ticket_dict:
            ticket_dict[ticket.source] = ticket.destination
    
    route = [ticket_dict['NONE']]

    for i in range(len(tickets) - 1):
        #location = destination of ticket in route list
        location = route[i]
        next_trip = ticket_dict[location]

        route.append(next_trip)

    return route
