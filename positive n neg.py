# Given an array of integers.

# Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.

# If the input is an empty array or is null, return an empty array.

# Example
# For input Given an array of integers.


# For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].
def count_positive_sum_neg(l):
    posi_count=0
    sum=0
    a=[]
    i=0
    while i<len(l):
        if l[i]>=0:
            posi_count+=1
        if l[i]<0:
            sum=sum+l[i]
        if l[i]==[]:
            return []
        i+=1
    a.append(posi_count)
    a.append(sum)
    return a
print(count_positive_sum_neg([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))
print(count_positive_sum_neg([]))

