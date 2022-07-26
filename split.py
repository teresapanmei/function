def my(name):
    i=0
    a=" "
    b=[]
    while i<len(name):
        if name[i]==" ":
            b.append(a)
            a=" "
        else: 
            a=a+name[i]
        i+=1
    if a:
        b.append(a)
    print(b)
my("teresa")

