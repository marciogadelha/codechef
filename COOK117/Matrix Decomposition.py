import sys, os
sys.stdin=open(os.path.dirname(__file__) + "/in.txt","r")
sys.stdout=open(os.path.dirname(__file__) + "/out.txt","w")

T = int(input())
for _ in range(T):
    n, a = map(int, input().split())
    v = [0] * (200001)
    v[0] = 1
    for i in range(1, 200000):
        v[i] = v[i-1] * a
    result = 0
    exp = 1
    p = a**exp
    result += p % 1000000007
    base = a
    for i in range(2, n + 1):
        exp = (2*i-1)*(exp+i-1)
        #p = (a**exp) % 1000000007
        p = v[exp]
        result += p % 1000000007
    print(result)
