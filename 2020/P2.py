P = int(input())    #limitation
N = int(input())    #n of people who have the disease on day 0
R = int(input())    #ppl infected on the next day

assert P <= 10**7
assert N <= P
assert R <= 10

total, day = 0, -1

while total <= P:
    total += N
    N *= R
    day += 1
print (day)