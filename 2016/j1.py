counter = 0
for _ in range(6):
    result = input()
    if result == 'W':
        counter += 1

if 5<=counter<=6:
    print(1)
elif 3<= counter <=4:
    print(2)
elif 1<=counter<=2:
    print(3)
else:
    print(-1)