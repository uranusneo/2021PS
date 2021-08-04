n=int(input())
score_c = score_s = 100

for _ in range(n):
    c,s= map(int, input().split(' '))
    if c<s:
        score_c-=s
    elif c>s:
        score_s-=c
    else: continue
    

print(score_c)
print(score_s)
