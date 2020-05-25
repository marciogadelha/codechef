import sys, os
sys.stdin=open(os.path.dirname(__file__) + "/in.txt","r")
sys.stdout=open(os.path.dirname(__file__) + "/out.txt","w")

# Problem Code: CHEFRECP

T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    ingredients = [False] * 1001
    ingredientByQuantity = [0] * 1001
    i = 0
    result = 'YES'
    while i < n:
        if ingredients[a[i]] == False:
            ingredients[a[i]] = True
            ingredient = a[i]
            quantity = 1
            i += 1
            while i < n and a[i] == ingredient:
                quantity += 1
                i += 1
            if ingredientByQuantity[quantity] == 0:
                ingredientByQuantity[quantity] = ingredient
            else:
                result = 'NO'
                break
        else:
            result = 'NO'
            break
    print(result)
