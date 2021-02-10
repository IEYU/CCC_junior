team_A = []
team_B = []
x = 3
for i in range(x):
    team_A.append((x-i)*int(input()))
for i in range(x):
    team_B.append((x-i)*int(input()))
a,b = sum(team_A), sum(team_B)
if a < b:
    print('B')
elif a > b:
    print('A')
else:
    print('T')