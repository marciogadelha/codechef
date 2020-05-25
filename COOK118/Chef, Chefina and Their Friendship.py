import sys, os
sys.stdin=open(os.path.dirname(__file__) + "/in.txt","r")
sys.stdout=open(os.path.dirname(__file__) + "/out.txt","w")

# Problem Code: CHEFSHIP

T = int(input())
for _ in range(T):
    s = input()
    n = len(s)
    i = 1
    result = 0
    while i < n:
        t1 = s[0:i]
        if i+len(t1) <= n - 2 and t1 == s[i:i+len(t1)]:
            j = i+len(t1)
            t2t2 = s[j:]
            if len(t2t2) % 2 == 0:
                t2 = s[j:j+int(len(t2t2)/2)]
                if t2 == s[j+int(len(t2t2)/2):]:
                    result += 1
        i += 1
    print(result)
