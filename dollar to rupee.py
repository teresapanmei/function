user=int(input("enter any amount:"))
def indian():
    rupees=user*72
    print("indian rupees =",rupees)
def us():
    dollar=user/72
    print("$=",dollar)
def choice():
    a=input("enter any choice:")
    if a=="$":
        us()
    else:
        indian()
choice()
