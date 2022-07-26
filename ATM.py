

def atm_ques():
    print("WELCOME TO PUNJAB BANK")
    print("INSERT YOUR ATM")
    language=input("ENTER YOUR LANGUAGE:")
    if language=="english":
        PIN=12345
        balance=10000
        print("INSERT YOUR PIN")
        pin=int(input("enter your pin:"))
        if pin==PIN:
            print("1.WITHDRAW.","\n2.DEPOSIT.","\n3.BALANCE ENQUIRY:")
            user=input("enter your transection:")
            if user=="BALANCE ENQUIRY":
                print("your balance is",balance)
            if user=="WITHDRAW":
                num=int(input("enter the money:"))
                print("your transection is successful")
                print("your current balance is",num-balance)
            if  user=="DEPOSIT":
                depo=int(input("enter your money:"))
                print("Enter your money.","\n your money deposit is successful.")
                print("your balance is",depo+balance,"\n Thank you")
        else:
            print("wrong pin")
    else:
        print("Sorry,Not available")
atm_ques()

