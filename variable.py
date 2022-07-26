# Global and Local Variables in Python
# Difficulty Level : Easy
# Last Updated : 09 Nov, 2021
 
# Global variables are those which are not defined inside any function and
#  have a global scope whereas local variables are those which are defined 
# inside a function and its scope is limited to that function only. In other
# words, we can say that local variables are accessible only inside the function
# in which it was initialized whereas the global variables are accessible 
# throughout the program and inside every function. 

# Local Variables
# Local variables are those which are initialized inside a function and belongs
#  only to that particular function. It cannot be accessed anywhere outside the
#  function. Let’s see how to create a local variable.

# Example: Creating local variables
# def f():
     
#     # local variable
#     s = "I love Geeksforgeeks"
#     print(s)
 
# # Driver code
# f()

# if we will try to use this local variable outside the function then let’s see what will happen.

# Example:
# def f():
     
#     # local variable
#     s = "I love Geeksforgeeks"
#     print("Inside Function:", s)
 
# # Driver code
# f()
# print(s)

# Global Variables
# The global variables are those which are defined outside any function and which are accessible throughout the program i.e. inside and outside of every function Let’s see how to create a global variable.

# Example: Defining and accessing global variables

# def f():
#     print("Inside Function", s)
 
# # Global scope
# s = "I love Geeksforgeeks"
# f()
# print("Outside Function", s)


# The variable s is defined as the global variable and is used both inside the function as well as outside the function.

# Note: As there are no locals, the value from the globals will be used.

# Now, what if there is a variable with the same name initialized inside a function as well as globally. Now the question arises, will the local variable will have some effect on the global variable or vice versa, and what will happen if we change the value of variable inside of the function f()? Will it affect the globals as well? We test it in the following piece of code: 


# def f():
#     s = "Me too."
#     print(s)
 
# # Global scope
# s = "I love Geeksforgeeks"
# f()
# print(s)


