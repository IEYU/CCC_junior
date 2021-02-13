duration = int(input())
hrs, mins = 12, 0
counter = 0

rounds = duration//720
left = duration % 720

for _ in range(left):
    mins += 1
    if mins >= 60:
        mins -= 60
        if hrs < 12:
            hrs += 1
        else:
            hrs = (hrs + 1) % 12
    if mins < 10:
        time = hrs * 1000 + mins
    else:
        time = hrs * 100 + mins

    if time // 1000 == 0:
        #111
        if (time%100%10 - time//10%10) == (time//10%10 - time//100):
            counter += 1
    else:
        #1111
        if (time%1000%100%10 - time//10%100%10) == (time//10%100%10 - time//100%10) and (time//10%100%10 - time//100%10) == (time//100%10 - time//1000):
            counter += 1
print(rounds * 31 + counter)
