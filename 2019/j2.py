#number of lines in the message
L = int(input())
#int < 80, followed by one space
num, code = [], []

for i in range(L):
    data = input().split()
    num.append(int(data[0]))
    code.append(data[-1])
#print('number:', num, 'code:', code)

for i in range(L):
    print(num[i] * code[i])