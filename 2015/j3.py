#'a'bc d'e'fg h'i'jkl mn'o'pqr st'u'vwxyz
consonant = 'bcdfghjklmnpqrstvwxyz'
vowel = 'aeiou'
group = ['bc','efg','hjkl','mnpqr','stvwxyz']

word = str(input())
newword = ''

for i in range(len(word)):
    x = 0
    if not word[i] in vowel:
        newword += word[i]
        for elem in group:
            if not word[i] in elem:
                x += 1
            else:
                break
        newword += vowel[x]
        if not word[i] == 'z':
            newword += consonant[consonant.index(word[i]) + 1]
        else:
            newword += 'z'
    else:
        newword += word[i]
print(newword)