# Andy Theriault
# ISS - 212
# Week 4 Assignment 3
#
#Code is adapted from the walkthrough
#

#query the user for packet size data.
packet_size=int(input("Enter the packet size in bytes"))
#print comparison statement result.
# is packet greater than 100 bytes?
# True or False?
print(packet_size>=2600) or ()

#protocol analysis logic
protocol_name=input("Enter the protocol name: ")
if protocol_name=="Cyphersec":
    print("Cyphersec is the only supported protocol!")
elif protocol_name=="cybersec":
    print("DENIED. Cyphersec protocol ONLY!")
else:
    print(f"Cyphersec! No {protocol_name} allowed!")


