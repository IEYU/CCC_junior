N = int(input())
real_seq, all_seq = [], []

for _ in range(N):
    inp = input().split()
    seq = []
    for elem in inp:
        elem = int(elem)
        seq.append(elem)
        all_seq.append(elem)
    real_seq.append(seq)

largest = max(all_seq)

def rotate(lst):
    new_lst = []
    i = len(lst) - 1    #2,1,0
    while i >= 0:   #3 times
        for j in range(len(lst[i])):#0,1,2
            if len(new_lst) < len(lst):  #len(new_lst) == 0
                new_lst.append([lst[i][j]])   #[7]
            else:
                new_lst[j].append(lst[i][j])
        i -= 1
    lst = new_lst
    return lst

while real_seq[-1][-1] != largest:
    real_seq = rotate(real_seq)

for elem in real_seq:
    print(*elem)


#[[1,2,3],
# [4,5,6],
# [7,8,9]]

#[[7,4,1],
# [8,5,2],
# [9,6,3]]
'''
12  31
34  42
'''