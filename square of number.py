# Q9.Write a Python program to generate and print a list of first and last 5 elements where
# the values are square of numbers between 1 and 30 (both included).
# Output :-([1, 4, 9, 16, 25], [676, 729, 784, 841, 900]).

def func(num):
    i=0
    a=[]
    while i<=num:
        x=i*i
        a.append(x)
        i+=1
    print(a[0:5],a[26:])
func(30)
