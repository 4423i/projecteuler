def gcd(x,y):
    if y == 0:
        return x
    else:
        return gcd(y,x%y)

def lcm(x,y):
    return x*y//gcd(x,y)

a = [i for i in range(1,21)]
ans = a[0]
for i in a:
    ans = lcm(ans,i)
print(ans)