def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

# print("\n\nRecursion Example Results")
tri_recursion(6)

# NavGurukul
# Hello!
# How are you?
# Python is awesome
# Hello!
# How are you?
# Hello…
# Hello!
# How are you?
 
 
