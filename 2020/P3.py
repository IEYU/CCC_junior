N = int(input())

assert 2 <= N
assert N <= 100

x_cor, y_cor = [], []
while N > 0:
    cord = input()
    X = int(cord.split(',')[0])
    Y = int(cord.split(',')[-1])

    N -= 1
    x_cor.append(X)
    y_cor.append(Y)

print(str(min(x_cor) - 1) + ',' + str(min(y_cor)-1))
print(str(max(x_cor) + 1) + ',' + str(max(y_cor)+1))