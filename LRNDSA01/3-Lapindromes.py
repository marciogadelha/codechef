import sys, os
sys.stdin=open(os.path.dirname(__file__) + "/in.txt","r")
sys.stdout=open(os.path.dirname(__file__) + "/out.txt","w")

t = int(input())
for _ in range(t):
    s = input()
    n = len(s)
    alphabet = [0] * 27
    for i in range(int(n/2)):
        alphabet[ord(s[i]) % 26] += 1
        alphabet[ord(s[n-1-i]) % 26] -= 1
    result = 'YES'
    for a in alphabet:
        if a != 0:
            result = 'NO'
            break
    print(result)
