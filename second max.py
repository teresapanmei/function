

num=[50,40,23,70,99,12,5,10, 7]
def check():
    l=num[0]
    s=num[0]
    i=0
    while i<len(num):
        if num[i]>l:
            l=num[i]
        i+=1
    i=0
    while i<len(num):
        if num[i]>s and num[i]!=l:
            s=num[i]
        i+=1
    print(s)
check()

