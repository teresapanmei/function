# Question 2
# What will be the output of the code given below?
num=int(input("enter any number"))
def primeorNot(num): 
    if num > 1:
       for i in range(2,num):
            if (num % i) == 0:
                print(num,"is not a prime number")
                print(i,"times",num//i,"is",num)
                break
            else:
                print(num,"is a prime number")

    else:
        print(num,"is not a prime number")
primeorNot(406)
