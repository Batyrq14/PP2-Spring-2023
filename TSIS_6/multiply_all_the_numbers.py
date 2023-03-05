def Mult_Find(v):
    ans = 1
    for i in v:
        ans *= i
    return ans
    
v = list(map(int, input().split()))
print(Mult_Find(v))