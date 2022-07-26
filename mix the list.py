def colour():
    num1=["0","1","2","3","4"]
    num2=["red","green","black","blue","white"]
    num3=["100","200","300","400","500"]
    a=[]
    i=0
    while i<len(num1):
        if len(num1)==len(num2)==len(num3):
            a.append(num1[i]+num2[i]+num3[i])
        else:
            print("not")
        i+=1
    print(a)
colour()
