import sys, os
sys.stdin=open(os.path.dirname(__file__) + "/in.txt","r")
sys.stdout=open(os.path.dirname(__file__) + "/out.txt","w")

a = []
n = int(input())
for _ in range(n):
    a.append(int(input()))
a.sort()
result = a[0] * n
for i in range(1, n):
    revenue = a[i] * (n-i)
    if revenue > result:
        result = revenue
print(result)
