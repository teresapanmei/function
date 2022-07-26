# Task
# Given the a list of numbers, return a fixed list so that the values increment by 1 for each index from the minimum value up to the maximum value (both included).

# Example
# Input: 1,3,5,6,7,8 Output: 1,2,3,4,5,6,7,8

# l=[ 1,3,5,6,7,8]
# i=0
# a=[]
# while i<len(l):
#     j=l[i]
#     while j<=l[-1]:
#         a.append(j)
#         j+=1
#         i+=1
# print(a)


# Given an array of integers.

# Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.

# If the input is an empty array or is null, return an empty array.

# Example
# For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].


def count_positives_sum_negatives(arr):
    if len(arr)>0:
        posi_count=0
        sum=0
        i=0
        while i<len(arr):
            if arr[i]>0:
                posi_count+=1
            if arr[i]<0:
                sum=sum+arr[i]
            i+=1
            a=[posi_count,sum]
    else:
        a=[]    
    return a
arr=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
count_positives_sum_negatives(arr)

# Implement a function which multiplies two numbers.


# def multiply (a,b):
#     b=a*b
#     return b
# print(multiply(6,2))


# Given a number n, return the number of positive odd numbers below n, EASY!

# Examples (Input -> Output)
# * 7  -> 3 (because odd numbers below 7 are [1, 3, 5])
# * 15 -> 7 (because odd numbers below 15 are [1, 3, 5, 7, 9, 11, 13])
# num=int(input("enter any num:"))
# i=1
# a=[]
# while i<num:
#     a.append(i)
#     j=0
#     b=[]
#     count=0
#     while j<len(a):
#         if a[j]%2!=0:
#             count+=1
#             x=a[j]
#             b.append(x)
#         j+=1
#     i+=1
# print(a)
# print("odd",b)
# print("no. of odd",count)

# 11
# you are given two sorted arrays that both only contain integers. Your task is to find a way to merge them into a single one, sorted in asc order. Complete the function mergeArrays(arr1, arr2), where arr1 and arr2 are the original sorted arrays.

# You don't need to worry about validation, since arr1 and arr2 must be arrays with 0 or more Integers. If both arr1 and arr2 are empty, then just return an empty array.

# Note: arr1 and arr2 may be sorted in different orders. Also arr1 and arr2 may have same integers. Remove duplicated in the returned result.

# Examples (input -> output)
# * [1, 2, 3, 4, 5], [6, 7, 8, 9, 10] -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# * [1, 3, 5, 7, 9], [10, 8, 6, 4, 2] -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# * [1, 3, 5, 7, 9, 11, 12], [1, 2, 3, 4, 5, 10, 12] -> [1, 2, 3, 4, 5, 7, 9, 10, 11, 12]

# Q.12
# Given an array of integers, return a new array with each value doubled.

# For example:

# [1, 2, 3] --> [2, 4, 6]
# def maps(a):
#     i=0
#     c=[]
#     while i<len(a):
#         b=a[i]*2
#         c.append(b)
#         i+=1
#     return c
# print(maps([1,2,3]))
    
    
# Write a function to split a string and convert it into an array of words.

# Examples (Input -> Output):
# * "Robin Singh" ==> ["Robin", "Singh"]

# * "I love arrays they are my favorite" ==> ["I", "love", "arrays", "they", "are", "my", "favorite"]
# def string_to_array(s):
#     a=[]
#     if s=="":
#         a.append(s)
#     else:
#         a=s.split()
#     return a

# Timmy & Sarah think they are in love, but around where they live, they will only know once they pick a flower each. If one of the flowers has an even number of petals and the other has an odd number of petals it means they are in love.

# Write a function that will take the number of petals of each flower and return true if they are in love and false if they aren't.

# def lovefunc( flower1, flower2 ):
#     if flower1%2==0 and flower2%2!=0:
#         return True
#     elif flower2%2==0  and flower1%2!=0:
#         return True 
#     else:
#         return False