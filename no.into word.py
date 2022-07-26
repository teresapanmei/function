a=input("enter any number:-")
b=""
c=['zero','one','two','three','four','five','six','seven','eight','nine']
i=0
while i<len(a):
    j=0
    while j<len(c):
        if a[i]==str(j):
            b+=" "+c[j]
        j+=1
    i+=1
print(b)


# [1:04 AM, 4/9/2022] Grace: take an array and remove every second element from the array. Always keep the 
# first element and start removing with the next element.
# Example:
# ["Keep", "Remove", "Keep", "Remove", "Keep", ...] --> ["Keep", "Keep", "Keep", ...]
# None of the arrays will be empty, so you don't have to worry about that!
# eg:-[1,2,3,4,5,6,7,8,9,10]----------[1,3,5,7,9]

# Given the a list of numbers, return the list so that the values increment by 1
# for each index up to the maximum value.
# ([1, 2, 3, 5, 6, 8, 9]), [1, 2, 3, 4, 5, 6, 7, 8, 9])
# ([1, 2, 3, 12]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
#  ([6, 9]), [6, 7, 8, 9])
#  ([-1, 4]), [-1, 0, 1, 2, 3, 4])
#  ([1, 2, 3]), [1, 2, 3]) 