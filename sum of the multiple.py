def my():
    user1=int(input("enter the number"))
    user2=int(input("enter the number"))
    if user1<=0 or user2<=0:
        print("invalid")
    else:
        i=1
        sum=0
        while i<=user2:
            if i%user1==0:
                print(i,end=" ")
                sum+=i
            i+=1
        print("\n",sum)
my()


# def sum(a,b):
#     print("k")
# def add(a):
#     return("zoya")
# return(9,18)
# print(9,18)
# print(("kajol")