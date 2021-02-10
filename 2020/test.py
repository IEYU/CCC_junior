M = 3
N = 4
grid = [[3, 10, 8, 14],[1, 11, 12, 12],[6, 2, 3, 10]]
rows, cols = 3, 4


list1 = []
visited = []
curlist = []
vcur = []
stacklist = []

for i in range(cols):
    curlist.append(0)
    vcur.append(True)
list1.append(curlist)
visited.append(vcur)

for i in range(rows-1):
    curlist1 = [0]
    vcur1 = [True]
    S = input().split()
    for j in range(M-1):
        curlist1.append(int(S[j]))
        vcur1.append(False)
    list1.append(curlist1)
    visited.append(vcur1)
print('list1:', list1)
print("visited:", visited)