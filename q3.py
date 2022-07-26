# Question 3
# 3

# Create a function which takes 3 arguments(all integers) and prints their sum and average as shown below.

# Input:-

# Enter first number :-3

# Enter second number :-4

# Enter third number:-5

# Output :-

# Sum of three numbers :-12
# Average of three numbers :-4

# elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
# i=0
# sum=0
# avg=0
# while i<len(elements):
#     a=elements[i]
#     sum=sum+a
#     avg=sum/a
#     i+=1
# print(sum)
# print("avg=",avg)

user=int(input("enter any number"))
user1=int(input("enter any number"))
user2=int(input("enter any number"))
def add_number(b,c,d):
    i=0
    sum=0
    avg=0
    a=b,c,d
    while i>a:
        # a=b,c,d
        sum=sum+a
        avg=sum/a
        i+=1
    print(sum)
    print("avg=",avg)
add_number(user,user1,user2)






