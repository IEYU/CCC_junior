votes = int(input())
singer = input()
a, b = 0, 0

for vote in singer:
    if vote == 'A':
        a += 1
    else:
        b += 1

if a > b:
    print('A')
elif b > a:
    print('B')
else:
    print('Tie')