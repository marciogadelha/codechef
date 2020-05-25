import sys, os
sys.stdin=open(os.path.dirname(__file__) + "/in.txt","r")
sys.stdout=open(os.path.dirname(__file__) + "/out.txt","w")

T = int(input())
for _ in range(T):
    n, q = map(int, input().split())
    result = 0
    pos = 0
    for i in range(q):
        f, d = map(int, input().split())
        result += abs(f - pos)
        result += abs(d - f)
        pos = d
    print(result)
