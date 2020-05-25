import sys, os
sys.stdin=open(os.path.dirname(__file__) + "/in.txt","r")
sys.stdout=open(os.path.dirname(__file__) + "/out.txt","w")

T = int(input())
for _ in range(T):
    n, q = map(int, input().split())
    s = input()
    count = [0] * 26
    for d in s:
        count[ord(d)%26] += 1
    count.sort(reverse = True)
    for _ in range(q):
        c = int(input())
        result = 0
        i = 0
        while (i < 26 and count[i] > c):
            result += count[i] - c
            i += 1
        print(result)
