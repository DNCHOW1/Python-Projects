import random
values = [' ', 'O', ' ',
          ' ', ' ', ' ',
          ' ', ' ', ' ']

meh = []
best = []
opp = {'O': 'X', 'X': 'O'}
bot = 'X'
'''if values[:3].count(' ') != 3 and values[:3].count(' ') != 0: # Meaning theres bound to be 1 bot and opp
    if values[:3].count(bot) == 2: # Win condition
        best.append(values[:3].index(' '))
    elif values[:3].count(opp[bot]) == 2: # Loss condition
        best.append(values[:3].index(' '))
    elif values[:3].count(bot) == 1 and values[:3].count(opp[bot]) == 1:
        pass
    else:
        for i in range(len(values[:3])):
            if values[:3][i] == ' ':
                meh.append(i)

print(meh)
print(best)'''

x = [1, 2, 3, 4]
print(x[random.randrange(len(x))])
