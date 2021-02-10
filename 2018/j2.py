N = int(input())
y, t = input(), input()
yesterday,today = [], []
for char in y:
    yesterday.append(char)
for char in t:
    today.append(char)
i, count = 0, 0
for _ in range(N):
    if yesterday[i] == today[i] == 'C':
        count += 1
    i += 1
print(count)
