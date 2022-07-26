num=[50,40,23,70,56,12,5,10, 7]
i=0
while i<len(num):
    j=0
    while j<len(num):
        if num[i]>num[j]:
            num[i],num[j]=num[j],num[i]
        j+=1
    i+=1
print(num)

