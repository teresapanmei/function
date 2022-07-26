# Python Inner Functions
# A function which is written or defined inside another function is called inner function or nested function. In inner functions, we can access the scope of variable of the outer function but we can't change those variables.

# EXAMPLE:-

# def f1():
#    s = "I Love Navgurukul"
#    def f2():
#     print(s)
#    f2()

# f1()
# Visualize
# Output :-

# I Love Navgurukul

# def f1():
#     s="I Love Navgurukul"
#     def f2():
#        print(s)

# f2()

def first_function(love):
    s =(love)
def second_function():
    print(second_function) 
second_function()
first_function("i love india")
# Visualize
# OUTPUT:-

# I love India

