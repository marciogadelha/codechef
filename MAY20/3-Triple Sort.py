import sys, os
sys.stdin=open(os.path.dirname(__file__) + "/in.txt","r")
sys.stdout=open(os.path.dirname(__file__) + "/out.txt","w")

p = [0] * 200001
stack = [0] * 200001

T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    pList = list(map(int, input().split()))
    count = 0
    size = 0
    for i in range(n):
        p[i+1] = pList[i]
        if i + 1 != pList[i]:
            count += 1
            size += 1
            stack[size] = i + 1
    ops = []
    op = 0
    i = 1
    while op <= k and count > 2 and i <= n:
        if p[i] == i:
            i += 1
        else:
            a = i
            b = p[a]
            c = p[b]
            if c != a:
                count -= 2
                if p[c] == a:
                    count -= 1
                p[a] = p[c]
                p[c] = p[b]
                p[b] = b
                ops.append([a, b, c])
                op += 1
            else:
                i += 1
    i = 1
    while op <= k and count > 2 and i <= n:
        if p[i] == i:
            i += 1
        else:
            a = i
            b = p[a]
            c = p[b]
            if c != a:
                count -= 2
                if p[c] == a:
                    count -= 1
            else:
                c = stack[size]
                aFound = False
                while size > 0 and (p[c] == c or c == b or c == a):
                    if c == a:
                        aFound = True
                    size -= 1
                    c = stack[size]
                if p[c] != c and c != b and c != a:
                    count -= 1
                if aFound:
                    size += 1
                    stack[size] = a
            if p[c] != c and c != b and c != a:
                p[a] = p[c]
                p[c] = p[b]
                p[b] = b
                ops.append([a, b, c])
                op += 1
            else:
                i += 1
    if op <= k and count == 0:
        print(op)
        for i in ops:
            print(i[0], i[1], i[2])
    else:
        print(-1)
