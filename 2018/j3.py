from typing import no_type_check_decorator


c1 = 0
city = input().split()
for x in city:
    x = int(x)
city.insert(0,c1)
n = 5
one = city[0]
two = one + int(city[1])
three = two + int(city[2])
four = three + int(city[3])
five = four + int(city[4])

l1 = str(abs(one-one)) + ' ' + str(abs(one-two)) + ' ' + str(abs(one-three)) + ' ' + str(abs(one-four)) + ' ' + str(abs(one-five))
l2 = str(abs(two-one)) + ' ' + str(abs(two-two)) + ' ' + str(abs(two-three)) + ' ' + str(abs(two-four)) + ' ' + str(abs(two-five))
l3 = str(abs(three-one)) + ' ' + str(abs(three-two)) + ' ' + str(abs(three-three)) + ' ' + str(abs(three-four)) + ' ' + str(abs(three-five))
l4 = str(abs(four-one)) + ' ' + str(abs(four-two)) + ' ' + str(abs(four-three)) + ' ' + str(abs(four-four)) + ' ' + str(abs(four-five))
l5 = str(abs(five-one)) + ' ' + str(abs(five-two)) + ' ' + str(abs(five-three)) + ' ' + str(abs(five-four)) + ' ' + str(abs(five-five))

print(l1)
print(l2)
print(l3)
print(l4)
print(l5)