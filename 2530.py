H, M, S = map(int, input().split())
timer = int(input()) 

# H += timer // 3600
# M += timer % 3600 // 60
# S += timer % 3600 % 60

ass = (S+timer) %60
bm = (S+timer)// 60

am = (M+bm) % 60
bh= (M+bm) // 60

ah = (H+bh) %24


print(ah, am, ass)