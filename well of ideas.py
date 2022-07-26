# wells of ideas(easy )
# For every good kata idea there seem to be quite a few bad ones!
# In this kata you need to check the provided array (x) for good ideas
#  'good' and bad ideas 'bad'. If there are one or two good ideas, return
#  'Publish!', if there are more than 2 return 'I smell a series!'.
#  If there are no good ideas, as is often the case, return 'Fail!'.
# Eg: well(["bad","bad","bad","bad","bad"])  -Fail
# well(["bad","bad","bad","bad","bad","good","good","good"])   -i smell a series
# well(["good","good","good","good","good"])  -i smell a series
# well(["bad","bad","good","good"])  -publish


def well(x):
    i=0
    count=0
    while i<len(x):
        if x[i]=="good":
            count+=1
        i+=1
    if count==0:
        return "fail"
    elif count==2 or count==1:
        return "publish"
    else:
        return "i smell a series"
print(well(["bad","bad","bad","bad","bad"]))  
print(well(["bad","bad","bad","bad","bad","good","good","good"]))  
print(well(["good","good","good","good","good"]))  
print(well(["bad","bad","good","good"])) 
