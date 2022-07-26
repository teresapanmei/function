# Q4. By using reverse function print the reverse order of the list.

# Input:-

# reverse_list = ["Z", "A", "A", "B", "E", "M", "A", "R", "D"]
# Visualize
# Output :-

# num = ["Z", "A", "A", "B", "E", "M", "A", "R", "D"]
# def reverse_list(num):
#     i=0
#     while i<len(num):
#         num.reverse()
#         i+=1
#     print(num)
# reverse_list(num)



# places=["delhi", "gujrat", "rajasthan", "punjab", "kerala"]
# a=[]
# i=-1
# while i>=-(len(places)):
#     a1=places[i]
#     a.append(a1)
#     i-=1
# print(a)

places=["delhi", "gujrat", "rajasthan", "punjab", "kerala"]
def reverse_style(b):
    i=-1
    a=[]
    while i>=-(len(places)):
        a.append(b[i])
        i-=1
    print(a)
reverse_style(places)

