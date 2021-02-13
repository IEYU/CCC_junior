starting_cord = [int(elem) for elem in input().split()]
destination_cord = [int(elem) for elem in input().split()]
charge = int(input())
#starting_cord = [10,2]
#destination_cord = [10,4]
#charge = 6
'''
3 4
3 3
3
Y

10 2
10 4
5
N
'''
x_move = abs(destination_cord[0] - starting_cord[0])
y_move = abs(destination_cord[-1] - starting_cord[-1])
total_move = x_move + y_move

if (charge - total_move) % 2 == 0 and total_move <= charge:
    print('Y')
else:
    print('N')