a, d = 100, 100

rounds = int(input())
for i in range(rounds):
    roll = [int(elem) for elem in input().split()]
    a_roll = roll[0]
    d_roll = roll[-1]
    
    if a_roll < d_roll:
        a -= d_roll
    elif a_roll > d_roll:
        d -= a_roll

print(a)
print(d)