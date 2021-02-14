M = int(input())

time = 0
final = [0] * 101
sent = [0] * 101
received = [0] * 101

for _ in range(M):
    msg = input().split()
    status, sender = msg[0], int(msg[1])
    
    if status == 'S':
        final[sender] += (time - sent[sender])
        received = 1
    elif status == 'R':
        received = -1
        sent[sender] = time
    else:
        time += (sender - 2)
    time += 1

for i in range(101):
    if received[i] != 0:
        if received[i] > 0:
            print(i, final[i])
        else:
            print(i, received[i])