first = int(input())
second = int(input())
third = int(input())
total = first + second + third
if total != 180:
    print('Error')
else:
    if first == second == third == 60:
        print('Equilateral')
    elif first == second or second == third or third == first:
        print('Isosceles')
    else:
        print('Scalene')