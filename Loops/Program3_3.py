#While loop demo
#Input sequence: 54,20,24,0,1,0,1
baggage_count=100
no_of_baggage_picked=0
while(baggage_count>0):
    no_of_baggage_picked = (int)(input ("number of baggage:"))
    baggage_count = baggage_count - no_of_baggage_picked
print("No. of baggage remaining:",baggage_count)