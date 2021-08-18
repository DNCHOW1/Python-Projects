# Better way to find divisors of a number, because it prints it nicely for the eyes
# Also, it's very simple! Since the factor of a number will most likely appear at
# the end, it's just like absolute value. If 1st index, get 2nd last item.

def divisor(num):
    num_divisible = []
    for i in range(1, num + 1):       # +1 so that it includes the number as well
        if num % i == 0:
            num_divisible.append(i)  # If no remainder, will add to the empty list
        else:                        # If remainder, will just keep going
            pass

    return num_divisible

def match(num):                            # Function matches the factors, nice to see
    divisors = {}
    num_divisible = divisor(num)
    if len(num_divisible) % 2 == 0:     # When len of list is even, there aren't much problems

        for i in range(int(len(num_divisible)/2)):
            divisors[num_divisible[i]] = num_divisible[0 - (1 + i)] # Will use the -1 to get the last factor,
                                                                    # As it keeps going, will get 2nd to last, etc.

    else:                               # When len is odd however, won't print
                                        # out the full set of factors, so +1 to iterate fully
        for i in range(int(len(num_divisible)/2) + 1):
            divisors[num_divisible[i]] = num_divisible[0 - (1 + i)]

    return divisors
