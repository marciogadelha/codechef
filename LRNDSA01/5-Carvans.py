import sys, os
sys.stdin=open(os.path.dirname(__file__) + "/in.txt","r")
sys.stdout=open(os.path.dirname(__file__) + "/out.txt","w")

T = int(input())
for _ in range(T):
    n = int(input())
    c = list(map(int, input().split()))
    result = 1
    minor = c[0]
    for i in range(1,n):
        if c[i] <= minor:
            result += 1
            minor = c[i]
    print(result)
