def min_two(a,b):
    if a<b:
        return a
    return b
def min_three(a,b,c):
    return min_two(a,min_two(b,c))
print(min_three(45,65,7))