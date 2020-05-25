import sys, os
sys.stdin=open(os.path.dirname(__file__) + "/in.txt","r")
sys.stdout=open(os.path.dirname(__file__) + "/out.txt","w")

# def countEndZeros(n):
#     count = 0
#     while n > 10 and n % 10 == 0:
#         n /= 10
#         count += 1
#     return count

# def countEndZeros(s):
#     count = 0
#     i = len(s)-1
#     while i >= 0 and s[i] == '0':
#         count += 1
#         i -= 1
#     return count

T = int(input())
for t in range(T):
    n = int(input())
    count = 0
    i = 1
    power5 = 5**i
    while power5 <= n:
        count += int(n / power5)
        i += 1
        power5 = 5**i
    print(count)
