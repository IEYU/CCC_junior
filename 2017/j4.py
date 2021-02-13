inp = int(input())

rounds = inp // (720)
left = inp % (720)

def one_round(time):
    hrs = time // 60
    mins = time % 60
    counter = 0

    if hrs >= 10:
        if hrs == 12:
            counter += 2
        elif hrs == 11:
            counter += 1

        for hr in range(1, 10):#1,2
            difference = 0
            #addition cases
            for min_first in range(1,6):#1,2,3,4,5
                #11,12,13,14,15
                if (hr + difference) == min_first and min_first < 6 and (min_first + difference) <= 9:
                    difference += 1
                    counter += 1
            #substraction cases
            difference = hr-1
            for min_second in range(1, hr):#1,2
                #22,21
                if (hr - difference) == min_second and min_second < 6 and(min_second - difference) >= 0:
                    counter += 1
                difference -= 1
    else:
        for hr in range(1, hrs):
            difference = 0
            #addition cases
            for min_first in range(1,6):#1,2,3,4,5
                #11,12,13,14,15
                if (hr + difference) == min_first and min_first < 6 and (min_first + difference) <= 9:
                    difference += 1
                    counter += 1
            #substraction cases
            difference = hr-1
            for min_second in range(1, hr):#1,2
                #22,21
                if (hr - difference) == min_second and min_second < 6 and(min_second - difference) >= 0:
                    counter += 1
                difference -= 1
        counter += 1
    return counter
#111,123,135,147,159
#222,234,246,258,210
#333,345,357,321
#444,456,432,420
#555,543,531
#654,642,630
#753,741
#852,840
#951
#1111
#1234
print(rounds * 31 + one_round(left))
