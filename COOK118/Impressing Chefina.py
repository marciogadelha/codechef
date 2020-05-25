import sys, os
sys.stdin=open(os.path.dirname(__file__) + "/in.txt","r")
sys.stdout=open(os.path.dirname(__file__) + "/out.txt","w")

# Problem Code: CHFIMPRS

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    quantity = []
    elements = []
    a = []
    for _ in range(n):
        line = list(map(int, input().split()))
        a.append(line)
        for e in line:
            if e in elements:
                quantity[elements.index(e)] += 1
            else:
                elements.append(e)
                quantity.append(1)
    odd = 0
    for q in quantity:
        if q % 2 != 0:
            odd += 1
    if m == 1 or (m % 2 == 0 and odd == 0) or (m % 2 != 0 and odd <= n and (n - odd) % 2 == 0):
        for i in range(n):
            for j in range(m-1):
                print(a[i][j], end=' ')
            print(a[i][m-1])
    else:
        print(-1)
