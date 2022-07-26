# Question 4
# This question is in 2 parts. Submit the code of both the parts by writing them in the same file.

# Question (Part 1)
# Write a function named add_numbers which takes two numbers as arguments and then prints their sum. The name of the arguments should be number1 and number2.


# Question (Part 2)
# Write a function named add_numbers_list which takes 2 lists of two integers and then prints the sum of the integers with the same position.

# Use the add_numbers function given in Part 1 to count 2 integers that have the same position.

# If we give [50, 60, 10] and [10, 20, 13] to this function it will print this

# 60
# 80
# 23
def add_number(number1,number2):
    print(number1+number2)
add_number(45,7)
def add_number_list(a,b):
    i=0
    a1=0
    b1=0
    while i<len(a):
        a1=a1+a[i]
        b1=b1+b[i]
        i+=1
    print(a1)
    print(b1)
add_number_list([4,6,3,1],[8,5,4,3])

