n = int(input())
rstList = []
for _ in range(n):
    a, b, c = map(int,input().split())
    rst = 0
    if a == b == c:
        rst = 10000 + (a * 1000)
    elif a==b:
        rst = 1000 + (a *100)
    elif b==c:
        rst = 1000 + (b *100)
    elif a==c:
        rst = 1000 + (a *100)
    else:
        rst = max(a,b,c) * 100
    rstList.append(rst)
print(max(rstList))
