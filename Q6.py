# What will be the output of the code given below?

def checkKey():
    car={
        "brand": "ford",
        "model": "mustang",
        "year": "1964"
    }
    if "model"in car:
        print("yes,'model',is one of the key in the thisdict dictionary",)
    else:
        print("no,'model',is not one of the key in the thisdict dictionay",)
checkKey()
