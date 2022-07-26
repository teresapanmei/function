# Question 1
# Create a funciton named eligibleforvote which tell the user if he/she is eligible to vote or not.( Consider minimum age of voting to be 18. )

# Example:-

# If user's age is less than 18 , print “not eligible “,else if user's age is greater than or equal to 18, print “you are eligible”

# Input:-

# 18
# 16

# Output :-

# “you are eligible”
# “not eligible”

# Edit on Github


user=int(input("enter any number"))
def age(user):
    if user>=18:
        print("you are eligible")
    elif user<=16:
        print("not eligible")
age(user)