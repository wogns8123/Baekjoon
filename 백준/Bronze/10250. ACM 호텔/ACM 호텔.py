import sys

tc = int(input())
for test in range(tc):
    H,W,N = map(int,input().split())
    f = 0
    ho = 0
    if N%H == 0:
        f=H*100
        ho = N//H
    else:
        f = (N%H) *100
        ho = 1 + N//H
    print(f+ho)