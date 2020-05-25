import sys, os
sys.stdin=open(os.path.dirname(__file__) + "/in.txt","r")
sys.stdout=open(os.path.dirname(__file__) + "/out.txt","w")

T = int(input())
for _ in range(T):
    n = int(input())
    x = list(map(int, input().split()))
    best = n
    worth = 1
    count = 1
    for i in range(1, n):
        if x[i] - x[i-1] > 2:
            if count > worth:
                worth = count
            if count < best:
                best = count
            count = 1
        else:
            count += 1
    if count > worth:
        worth = count
    if count < best:
        best = count
    print(best, worth)
