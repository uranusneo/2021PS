#왜 에러나지?
#a=b=0
#while a == 0 & b == 0:
    #a,b = map(int,input().split(' '))
    #print(a+b)

a=b=0
while True:
     a,b = map(int,input().split(' '))
     if a == b == 0:
         break
     else:print(a+b)
