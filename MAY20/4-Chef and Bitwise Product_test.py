import sys, os
sys.stdin=open(os.path.dirname(__file__) + "/in.txt","r")
sys.stdout=open(os.path.dirname(__file__) + "/out_teste.txt","w")

T = int(input())
for _ in range(T):
    x, y, l, r = map(int, input().split())
    result = z = l
    f = (x & z)*(y & z)
    for z in range(l, r+1):
        f1 = (x & z)*(y & z)
        if f1 > f:
            f = f1
            result = z
    print(result, f)
