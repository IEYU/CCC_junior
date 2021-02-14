M = int(input())

time = 0
final = [0] * 101
sent = [0] * 101
received = [0] * 101

for _ in range(M):
    time += 1
    
    msg = input().split()
    status, sender = msg[0], int(msg[1])
    
    if status == 'R':#waiting for a reply
        received[sender] = -1
        sent[sender] = time

    elif status == 'S':#received a reply
        received[sender] = 1
        final[sender] += (time - sent[sender])
    
    else:
        time += (sender - 2)

for i in range(101):
    if received[i] != 0:
        if received[i] > 0:
            print(i, final[i])
        else:
            print(i, received[i])