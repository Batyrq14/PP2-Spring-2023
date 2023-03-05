def Upper_Cnt(s):
    cnt = 0
    for i in s:
        if 'A' <= i <= 'Z':
            cnt += 1
    return cnt

def Lower_Cnt(s):
    cnt = 0
    for i in s:
        if 'a' <= i <= 'z':
            cnt += 1
    return cnt

s = input()
print('No. of Upper case characters : {}'.format(Upper_Cnt(s)))
print('No. of Lower case Characters : {}'.format(Lower_Cnt(s)))
