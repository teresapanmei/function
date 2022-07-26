# Question 2
# Perfect Number?
# A perfect number is the one which is equal to the sum of all it's factors(including 1 and excluding itself).

# Define a function named perfect() which takes one argument(integer) and
#  checks if it is a perfect number or not. Now use this code to write a 
# program that prints all the perfect numbers between 1-1000.

# Example:-

# 6 ek perfect number hai 6=1+2+3.

# Expected Output :-

# 6,28,496

def perfect(x):
    i=1
    while i<=x:
        sum=0
        j=1
        while j<i:
            if i%j==0:
                sum+=j
            j+=1
        if sum==i:
            print(i,end=",")
        i+=1
perfect(1000)