import sys, os
sys.stdin=open(os.path.dirname(__file__) + "/in.txt","r")
sys.stdout=open(os.path.dirname(__file__) + "/out.txt","w")

T = int(input())
for _ in range(T):
    k, d0, d1 = map(int, input().split())
    result = 'NO'
    sums = d0 + d1
    for i in range(2, k):
        di = sums % 10
        sums += di
    if sums % 3 == 0:
        result = 'YES'
    print(result)
