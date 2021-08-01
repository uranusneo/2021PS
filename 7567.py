d = list(str(input()))
pd=10
for i in range(1,len(d)):
    if d[i-1]!=d[i]:
        pd += 10
    else:
        pd+=5
  
print(pd)