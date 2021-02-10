flip = str(input())
seq = [1,2,3,4]
dict = {}
index = -1
for elem in flip:
    seq_copy = seq
    #print('original:', seq)
    #print('copy:', seq_copy)
    if elem =="H":
        seq_copy = (seq[2], seq[3], seq[0], seq[1])
        seq = seq_copy
    else:
        seq_copy = (seq[1], seq[0], seq[3], seq[2])
        seq = seq_copy
print(seq_copy[0], seq[1])
print(seq_copy[2],seq[3])