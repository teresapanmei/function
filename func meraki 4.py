# Question 5
# This question is in 2 parts. Submit the code of both the parts by writing them in the same file.

# Question (Part 1)
# Write a function named check_numbers which takes two numbers and then print "both are even" if both numbers are even (divide by 2) otherwise print "both numbers are not even".

# Question (Part 2)
# Now write a function named check_numbers_list Which takes the list of an integer as a argument and then checks whether both the integers with the same index are even or not.

# To check this, use the check_numbers function written in the previous Part 1.

# If you call your function [2, 6, 18, 10, 3, 75] and [6, 19, 24, 12, 3, 87] then it should give this output:

# both are even
# both are not even
# both are even
# both are even
# both are not even

# def check_number(a,b):
#     if a%2==0 and b%2==0:
#         print("even")
#     else:
#         print("both are not the same")
# check_number(4,6)



def check_number_list(c,d):
    i=0
    while i<len(c):
        a=c[i]+d[i]
        if a%2==0:
            print("both are even")
        elif a%2!=0:
            print ("Both are odd")
        i+=1
        
check_number_list([4,7,8,7],[9,5,4,6])

