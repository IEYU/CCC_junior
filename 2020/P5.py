'''
13/17
NEED OPTIMIZATION
TIME LIMIT EXCEEDED
'''
#creating the 2D array
M = int(input())    #rows
N = int(input())    #columns
rows, cols = M, N

grid = []
for _ in range(M):
    col = []
    for x in input().split(" "):
        x = int(x)
        col.append(x)
    grid.append(col)

#start at cell cur_node
#find all cells == target
#check
#if not target, go back
target = rows * cols
searched = []
searched.append([rows,cols])
#from back to beginning

#find all the coordinate of a number in a list
def cord(n,lst=[]):
    index = []
    x_cor = 0
    for elem in range(len(lst)):
        y_cor = 0
        for i in lst[elem]:
            if i == n:
                index.append([x_cor, y_cor])
            y_cor += 1
        x_cor += 1
    return index

def trace(pos):
    location = cord(pos, grid)
    for x,y in location:    #reaches the top left node
        if x == 0 and y == 0:
            return True
        else:
            #repeat this process for new values
            if [x,y] not in searched:
                searched.append([x,y])
                #print('searched:', searched)
                if trace((x+1)*(y+1)):
                    return True
    return False
if trace(target):
    print('yes')
else:
    print('no')