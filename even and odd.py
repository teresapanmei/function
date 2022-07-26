# num=[1,2,3,6,8,7,9,4,5,0,4]
# i=0
# even=0
# odd=0
# while i<len(num):
#     if num[i]%2==0:
#         even+=1
#     else:
#         odd+=1  
#     i+=1
# print("count of even=",even)
# print("count of odd=",odd)

num=[1,2,3,6,8,7,9,4,5,0,4]
i=0
count=0
count1=0
even=0
sum=0
odd=0
sum1=0
while i<len(num):
    if num[i]%2==0:
        count=count+num[i]
        sum=sum+num[i]
        even+=1
    else:
        count1=count1+num[i]
        sum1=sum1+num[i]
        odd+=1  
    i+=1
print("count of even=",even)
print("sum of even is=",sum)
print("count of odd=",odd)
print("sum of odd is=",sum1)


# a=[]
# def create():
#     i=1
#     while i<=6:
#        user=int(input("enter any number:"))
#        a.append(user)
#        i+=1
#     print(a)
# create()
# def user():
#     i=0
#     even=0
#     odd=0
#     while i<len(a):
#         if a[i]%2==0:
#             even+=1
#         else:
#             odd+=1
#         i+=1
#     print(even)
#     print(odd)
# user()
