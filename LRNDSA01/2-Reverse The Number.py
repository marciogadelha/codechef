import sys, os
sys.stdin=open(os.path.dirname(__file__) + "/in.txt","r")
sys.stdout=open(os.path.dirname(__file__) + "/out.txt","w")

t = int(input())
for _ in range(t):
    s = input()
    n = len(s)
    sr = ''
    for i in range(n):
        sr += s[n-1-i]
    i = 0
    while (i < n - 1 and sr[i] == '0'):
        i += 1
    print(sr[i:])
