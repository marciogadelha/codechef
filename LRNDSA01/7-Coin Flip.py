import sys, os
sys.stdin=open(os.path.dirname(__file__) + "/in.txt","r")
sys.stdout=open(os.path.dirname(__file__) + "/out.txt","w")

T = int(input())
for _ in range(T):
    g = int(input())
    for _ in range(g):
        i, n, q = map(int, input().split())
        result = 0
        if n % 2 == 0:
            result = int(n/2)
        else:
            result = int((n+1)/2)
        if i == 1:
            totalT = result
            totalH = n - result
        else:
            totalH = result
            totalT = n - result
        if q == 1:
            result = totalH
        else:
            result = totalT
        print(result)
