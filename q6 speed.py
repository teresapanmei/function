# Question 6
# Define a function that checks the speed of drivers. This function will take a parameter named speed, and will satisfy the following conditions:
# 1.If speed if less than 70, print 70.
# 2.If speed is more than 70, give 1 point per 5km.(NOTE:This won't count 70).
# 3. If points are more than 12, print “License suspended”

# Input:-

# 85
# 135

# Output :-

# 3
# “License suspended”
def checkKey():
    car={
        "brand": "ford",
        "model": "mustang",
        "year": "1964"
    }
    if "model"in car:
        print("yes,'model',is one of the key in the thisdict dictionary",)
    else:
        print("no,'model',is not one of the key in the thisdict dictionay",)
checkKey()
