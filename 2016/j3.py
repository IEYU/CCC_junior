word = str(input())

counter = []

for i in range(len(word) + 1):#0-6
    #[0:1], [0:2],[0:3]...
    #[1:1],[1:2],[1:3]...
    for j in range(i):
        if word[j:i] == word[j:i][::-1]:
            counter.append(len(word[j:i]))
print(max(counter))