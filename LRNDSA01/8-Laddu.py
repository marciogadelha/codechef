import sys, os
sys.stdin=open(os.path.dirname(__file__) + "/in.txt","r")
sys.stdout=open(os.path.dirname(__file__) + "/out.txt","w")

T = int(input())
for _ in range(T):
    n, indian = input().split()
    laddus = 0
    for _ in range(int(n)):
        line = input().split()
        if line[0] == 'TOP_CONTRIBUTOR':
            laddus += 300
        elif line[0] == 'CONTEST_HOSTED':
            laddus += 50
        elif line[0] == 'BUG_FOUND':
            laddus += int(line[1])
        else:
            laddus += 300
            rank = int(line[1])
            if rank <= 20:
                laddus += 20 - rank
    result = 0
    if indian == 'INDIAN':
        result = laddus//200
    else:
        result = laddus//400
    print(result)
