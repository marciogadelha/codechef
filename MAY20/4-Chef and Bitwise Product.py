import sys, os
sys.stdin=open(os.path.dirname(__file__) + "/in.txt","r")
sys.stdout=open(os.path.dirname(__file__) + "/out.txt","w")

def f(zp):
    global x, y
    return ((x & zp) * (y & zp))

def check(zp):
    global fMax, z, r
    if zp > l and zp <= r:
        fp = f(zp)
        if fp > fMax:
            fMax = fp
            z = zp

T = int(input())
for _ in range(T):
    x, y, l, r = map(int, input().split())
    z = l
    fMax = f(z)
    zfull = x | y

    if zfull < l:
        zbits = zfull
        zp = 0
        zl = 0
        while zp < l:
            zp = zl
            bitl = 1
            zl = zl | bitl
            while zl < l:
                bitl = bitl << 1
                zl = zl | bitl
            zp = zp | bitl
            zl = zp
            check(zp)
            power = 1
            bit = zbits & power
            zp = zp | bit
            while zp < r and power < bitl:
                check(zp)
                power = power << 1
                bit = zbits & power
                zp = zp | bit
        check(r)

    elif zfull > r:

        bitmax = 1
        ones = bitmax
        zp = zfull & ones
        check(zp)
        while ones < r:
            bitmax = bitmax << 1
            ones = ones | bitmax
            zp = zfull & ones
            check(zp)
        zbits = zfull & ones

        zp = 0
        zl = 0
        while zp < l:
            zp = zl
            bitl = 1
            zl = zl | bitl
            while zl < l:
                bitl = bitl << 1
                zl = zl | bitl
            zp = zp | bitl
            zl = zp
            check(zp)
            power = 1
            bit = zbits & power
            zp = zp | bit
            while zp < r and power < bitl:
                check(zp)
                power = power << 1
                bit = zbits & power
                zp = zp | bit

        zp = zbits
        while zp > r and bitmax < r:
            zp = bitmax
            power = 1
            while zp < r:
                check(zp)
                bit = zbits & power
                zp = zp | bit
                power = power << 1
            power = power >> 1
            while power & zbits == 0 and power > 0:
                power = power >> 1
            if power == 0:
                break
            bitmax = bitmax | power

        check(r)

    else:
        check(zfull)
    
    print(z)
