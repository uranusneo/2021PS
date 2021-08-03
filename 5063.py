n = int(input())

for i in range (n): #range 안에 (1,n) 넣었더니 튜플은 넣을 수 없다고 안됐던건가?
    r,e,c= map(int, input().split(' '))

    if e>r+c:
        print("advertise")
    elif e<r+c:
        print("do not advertise")
    else: print("does not matter")

#TypeError: 'tuple' object cannot be interpreted as an integer