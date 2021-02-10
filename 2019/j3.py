n = int(input())
block = []
for _ in range(n):
    block.append(input())

out = []
for elem in block:
    counter = 1
    code = ''
    for i in range(len(elem) - 1):
        if elem[i] == elem[i+1]:
            counter += 1
        elif elem[i] != elem[i+1] or i == (len(elem) - 1):
            code += (str(counter) + ' ' + elem[i] + ' ')
            counter = 1
    code += (str(counter) + ' ' + elem[-1])
    out.append(code)
for elem in out:
    print(elem)