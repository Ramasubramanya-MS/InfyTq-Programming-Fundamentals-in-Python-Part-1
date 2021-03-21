#Flight rate problem(multiple passengers)
#Rate per adult: Rs37550.0
#Rate per child: 1/3rd of Adult
#Service tax: 7% for all passengers
#Final discount after the service tax: 10%
def calculate_total_ticket_cost(no_of_adults, no_of_children):
    total_ticket_cost=0
    #Write your logic here
    ticket_perperson=37550.0
    ticket_perminor=((1/3)*37550.0)
    ticket_price_before_tax=(no_of_adults*ticket_perperson)+(no_of_children*ticket_perminor)
    ticket_price_after_tax=(ticket_price_before_tax)+(0.07*ticket_price_before_tax)
    total_ticket_cost=ticket_price_after_tax-(0.1*ticket_price_after_tax)
    return total_ticket_cost


#Provide different values for no_of_adults, no_of_children and test your program
total_ticket_cost=calculate_total_ticket_cost(5,2)
print("Total Ticket Cost:",total_ticket_cost)