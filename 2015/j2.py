emoji = input()
happy, sad = 0,0

for i in range(len(emoji) + 3):
    if emoji[i:i + 3] == ':-)':
        happy += 1
    elif emoji[i:i+3] == ':-(':
        sad += 1

if happy > sad:
    print('happy')
elif happy < sad:
    print('sad')
elif happy == sad and happy != 0:
    print('unsure')
else:
    print('none')