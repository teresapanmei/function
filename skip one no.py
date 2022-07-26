# [1:04 AM, 4/9/2022] Grace: take an array and remove every second element from the array. Always keep the 
# first element and start removing with the next element.
# Example:
# ["Keep", "Remove", "Keep", "Remove", "Keep", ...] --> ["Keep", "Keep", "Keep", ...]
# None of the arrays will be empty, so you don't have to worry about that!
# eg:-[1,2,3,4,5,6,7,8,9,10]----------[1,3,5,7,9]


def func(a):
    i=0
    b=[]
    while i<(len(a)):
        b.append(a[i])
        i+=2
    print(b)
a=[1,2,3,4,5,6,7,8,9,10]
# a=["Keep", "Remove", "Keep", "Remove", "Keep"]
func(a)


