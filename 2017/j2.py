n = int(input())
shift = int(input())

out = 0
#12 + 120 + 1200 + 12000
while shift > 0:
    zero = 10 ** shift
    out += (n* zero)
    shift -= 1
print(n + out)