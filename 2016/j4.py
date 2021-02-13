#rush hours: 7:00 - 10:00, 15:00 - 19:00 (half speed)
#no rush hour: 2 hrs
time = input().split(':')
hr = int(time[0])
mt = int(time[-1])
time = hr*60 + mt
#print('leaving time:',time)
#300min > 
travel = 240
while travel > 0:
    time += 1
    if 7*60 < time < 10*60 or 15*60<time<19*60:
        travel -= 1
    else:
        travel -= 2

print(str(time//60%24).zfill(2) + ':' + str(time%60).zfill(2))