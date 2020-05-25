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
    odds = []
    for i in range(len(quantity)):
        if quantity[i] % 2 != 0:
            odd += 1
            odds.append(i)
    if m == 1 or (m % 2 == 0 and odd == 0) or (m % 2 != 0 and odd <= n and (n - odd) % 2 == 0):
        k = 0
        if m % 2 != 0 and m != 1:
            p = int(m/2)
            i = 0
            for eOdd in odds:
                a[i][p] = elements[eOdd]
                quantity[eOdd] -= 1
                i += 1
            while i < n:
                while k < len(elements) and quantity[k] == 0:
                    k += 1
                if k < len(elements) and quantity[k] > 0:
                    a[i][p] = elements[k]
                    quantity[k] -= 1
                    i += 1
        for i in range(n):
            for j in range(int(m/2)):
                while k < len(elements) and quantity[k] < 2:
                    k += 1
                if k < len(elements) and quantity[k] >= 2:
                    a[i][j] = elements[k]
                    a[i][m-j-1] = elements[k]
                    quantity[k] -= 2
        for i in range(n):
            for j in range(m-1):
                print(a[i][j], end=' ')
            print(a[i][m-1])
    else:
        print(-1)
