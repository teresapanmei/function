num=[6, 8, 4, 3, 9, 56, 0, 34, 7, 15]
def unorder_list(num): 
    i=0
    while i<len(num):
        j=0
        while j<len(num):
            if num[i]>num[j]:
                num[i],num[j]=num[j],num[i]
            j+=1
        i+=1
    print(num)
unorder_list(num)