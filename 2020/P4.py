T = str(input())
S = str(input())

count = len(S)

while count >= 0:
    count -= 1
    if S in T:
        print('yes')
        break
    elif count == 0:
        print ('no')
        break
    else:
        S = S[1:] + S[0]
        