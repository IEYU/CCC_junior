'''rule_one = str(input()).split()
rule_two = str(input()).split()
rule_three = str(input()).split()
one_length, two_length, three_length = len(rule_one[0]), len(rule_two[0]), len(rule_three[0])
dict = {str([rule_one[0]]): rule_one[-1],str([rule_two[0]]): rule_two[-1],str([rule_three[0]]): rule_three[-1]}
limit = input().split()
steps = int(limit[0])
initial = str(limit[1])
final = str(limit[-1])
print(dict)'''
rule_one = ['AA', 'AB']
rule_two = ['AB', 'BB']
rule_three = ['B', 'AA']
one_length, two_length, three_length = len(rule_one[0]), len(rule_two[0]), len(rule_three[0])
dict = {str(rule_one[0]): rule_one[-1],str(rule_two[0]): rule_two[-1],str(rule_three[0]): rule_three[-1]}
limit = [4, 'AB', 'AAAB']
steps = int(limit[0])
initial = str(limit[1])
final = str(limit[-1])

#AA AB
#AB BB
#B AA
#4 AB AAAB
#AB > BB > AAB > AAAA > AAAB
def shuffle(step = steps, init=initial, fin=final):
    if init == fin:
        return init
    elif step == 0:
        return init
    else:
        if str(init[0:one_length]) in dict:
            init = (init[:one_length-1] + dict[str(init[0:one_length])] + init[one_length:])
            print("1", init)
        elif str(init[0:two_length]) in dict:
            init = (init[:two_length-1] + dict[str(init[0:two_length])] + init[two_length:])
            print("2", init)
        elif str(init[0:three_length]) in dict:
            init = (init[:three_length-1] + dict[str(init[0:three_length])] + init[three_length:])
            print("3", init)
        return shuffle(step-1, init, fin)
shuffle(steps, initial, final)