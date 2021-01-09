import math 
def c(n,m):
    return(math.factorial(n)//math.factorial(n-m)//math.factorial(m))
print(c(40,20))