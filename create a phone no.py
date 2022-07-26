list=[0,2,0,2,3,4,6,8,9]
def number():
    num=""
    num1=""
    num2="-"
    i=0
    while i<len(list):
        if i<3:
            num=num+str(str(list[i]))
        if i>=3 and i<=5:
            num1=num1+str(list[i])
        if i>=6:
            num2=num2+str(list[i])
        i+=1
    func="("+num+")"
    print(func+num1+num2)
number()