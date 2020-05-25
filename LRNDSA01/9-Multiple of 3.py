import sys, os
sys.stdin=open(os.path.dirname(__file__) + "/in.txt","r")
sys.stdout=open(os.path.dirname(__file__) + "/out.txt","w")

sequence = [2, 4, 8, 6]
mapd3 = [-1,0,-1,3,-1,-1,-1,1,-1,2]

T = int(input())
for _ in range(T):
    k, d0, d1 = map(int, input().split())
    result = 'NO'
    sums = d0 + d1
    if sums != 5 and sums != 10 and sums != 15:
        if k > 2:
            d2 = sums % 10
            sums += d2
            if k > 3:
                if d2 == 1 or d2 == 3 or d2 == 7 or d2 == 9:
                    d3 = sequence[mapd3[d2]]
                else:
                    d3 = sequence[(sequence.index(d2) + 1) % 4]
                sums += d3
                if k > 4:
                    kr = k - 4
                    loops = kr//4
                    sums += loops*(2 + 4 + 8 + 6)
                    rest = kr % 4
                    di = sequence[(sequence.index(d3) + 1) % 4]
                    for i in range(rest):
                        sums += di
                        di = sequence[(sequence.index(di) + 1) % 4]
        if sums % 3 == 0:
            result = 'YES'
    elif sums == 15 and k == 2:
        result = 'YES'
    print(result)
