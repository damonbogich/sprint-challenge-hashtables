class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

ticket_1 = Ticket("PIT", "ORD")
ticket_2 = Ticket("XNA", "SAP")
ticket_3 = Ticket("SFO", "BHM")
ticket_4 = Ticket("FLG", "XNA")
ticket_5 = Ticket("NONE", "LAX")
ticket_6 = Ticket("LAX", "SFO")
ticket_7 = Ticket("SAP", "SLC")
ticket_8 = Ticket("ORD", "NONE")
ticket_9 = Ticket("SLC", "PIT")
ticket_10 = Ticket("BHM", "FLG")

tickets = [ticket_1, ticket_2, ticket_3, ticket_4, ticket_5, ticket_6, ticket_7, ticket_8, ticket_9, ticket_10]
print(tickets[0].source)
#should be list of airports in order: LAX, SFO, BHM, ETC...

ticket_dict = {}

for ticket in tickets:
    if ticket.source not in ticket_dict:
        ticket_dict[ticket.source] = ticket.destination


result_list = [ticket_dict['NONE']]
#now we need to add the rest of the airports to this list 
#access ticket_dict['None'] value and append it until NONE COMES BACK UP AGAIN

for i in range(len(tickets) - 1):
    #location starts as LAX
    location = result_list[i]
    next_trip = ticket_dict[location]

    result_list.append(next_trip)
print(result_list)






