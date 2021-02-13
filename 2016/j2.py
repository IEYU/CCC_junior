matrix = []
for _ in range(4):
    subset = [int(elem) for elem in input().split()]
    matrix.append(subset)

s = sum(matrix[0])
is_magic_row = False
is_magic_col = False
#rows
for elem in matrix:
    if sum(elem) != s:
        is_magic_row = False
        break
    else:
        is_magic_row = True

for i in range(4):
    rol_s = 0
    for j in matrix:
        rol_s += j[i]
    if rol_s != s:
        is_magic_col = False
        break
    else:
        is_magic_col = True
if is_magic_col and is_magic_row:
    print('magic')
else:
    print('not magic')
