# Written by M.O.V.E and Eric Martin for COMP9021


'''
Generates a list L of random nonnegative integers smaller than the length of L,
whose value is input by the user, and outputs two lists:
- a list M consisting of L's middle element, followed by L's first element,
  followed by L's last element, followed by L's second element, followed by
  L's penultimate element...;
- a list N consisting of L[0], possibly followed by L[L[0]], possibly followed by
  L[L[L[0]]]..., for as long as L[L[0]], L[L[L[0]]]... are unused, and then,
  for the least i such that L[i] is unused, followed by L[i], possibly followed by
  L[L[i]], possibly followed by L[L[L[i]]]..., for as long as L[L[i]], L[L[L[i]]]...
  are unused, and then, for the least j such that L[j] is unused, followed by L[j],
  possibly followed by L[L[j]], possibly followed by L[L[L[j]]]..., for as long as
  L[L[j]], L[L[L[j]]]... are unused... until all members of L have been used up.
'''


import sys
from random import seed, randrange


try:
    arg_for_seed, length = input('Enter two nonnegative integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, length = int(arg_for_seed), int(length)
    if arg_for_seed < 0 or length < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
L = [randrange(length) for _ in range(length)]
print('\nThe generated list L is:')
print('  ', L)
M = [0] * len(L)
N = [0] * len(L)
tempM = list(L)
tempN = list(L)

if L == []:
    M = N = []
else:
    M[0] = tempM.pop(len(L) // 2)
    for i in range(1, len(L)):
        if i % 2 != 0:
            M[i] = tempM.pop(0)
        else:
            M[i] = tempM.pop(-1)

    N[0] = tempN[0]
    tempN[0] = -5
    for i in range(1, len(L)):
        if tempN[N[i-1]] == -5:
            for x in range(len(tempN)):
                if tempN[x] != -5:
                    N[i] = tempN[x]
                    tempN[x] = -5
                    break
        else:
            N[i] = tempN[N[i-1]]
            tempN[N[i-1]] = -5
        
    
    
print('\nHere is M:')
print('  ', M)
print('\nHere is N:')
print('  ', N)
print('\nHere is L again:')
print('  ', L)
