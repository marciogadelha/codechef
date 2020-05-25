import sys, os
sys.stdin=open(os.path.dirname(__file__) + "/in.txt","r")
sys.stdout=open(os.path.dirname(__file__) + "/out.txt","w")

p = [0] * 19

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    pList = list(map(int, input().split()))
    count = 0
    size = 0
    for i in range(n):
        p[i + 1] = pList[i]
        if i + 1 != pList[i]:
            count += 1
    for i in range(m):
        x, y = map(int, input().split())
    result = 0
    i = 0
    while (count > 0 and i <= n):
        if i == p[i]:
            i += 1
        else:
            p[p[i]], p[i] = p[i], p[p[i]]
            result += 1
    print(result)
