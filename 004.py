ans = 0
for i in range(100,1000):
    for j in range(100,1000):
        tmp = str(i*j)
        if tmp[:3] == tmp[::-1][:3]:
            ans = max(ans,i*j)
            #print(tmp,tmp[:3],tmp[::-1][:3])
print(ans)