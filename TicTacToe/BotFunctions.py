import random

def winCondition(board, bot):
    if board['top-L'] == bot and board['top-M'] == bot and board['top-R'] == bot:
        return True
    elif board['mid-L'] == bot and board['mid-M'] == bot and board['mid-R'] == bot:
        return True
    elif board['low-L'] == bot and board['low-M'] == bot and board['low-R'] == bot:
        return True
    elif board['top-L'] == bot and board['mid-L'] == bot and board['low-L'] == bot:
        return True
    elif board['top-M'] == bot and board['mid-M'] == bot and board['low-M'] == bot:
        return True
    elif board['top-R'] == bot and board['mid-R'] == bot and board['low-R'] == bot:
        return True
    elif board['top-L'] == bot and board['mid-M'] == bot and board['low-R'] == bot:
        return True
    elif board['top-R'] == bot and board['mid-M'] == bot and board['low-L'] == bot:
        return True
    else:
        return False

def filledIn(board, position, keys):
    values = list(board.values())
    if values[position] == ' ':
        return keys[position]
    else:
        return 0

def checking(l, bot, meh, best, realv):
    opp = {'O': 'X', 'X': 'O'}
    if l.count(' ') != 3 and l.count(' ') != 0: # Meaning theres bound to be 1 bot and opp
        if l.count(bot) == 2: # Win condition
            best.append(realv[l.index(' ')])
        elif l.count(opp[bot]) == 2: # Loss condition
            best.append(realv[l.index(' ')])
        elif l.count(bot) == 1 and l.count(opp[bot]) == 1:
            pass
        else:
            for i in range(len(l)):
                if l[i] == ' ':
                    meh.append(realv[i])

def botMove(board, bot, keys):  # Dictionary, bot, and keys
    values = list(board.values())
    number = values.count(' ')
    if number == 9:
        while True:
            botPosition = random.randint(0, 8)
            positionCheck = filledIn(board, botPosition, keys) # Gets the exact spot key
            if positionCheck != 0:
                board[positionCheck] = bot # And uses the key to pinpoint the move
                return board
            else:
                continue
    else:
        meh = []
        best = []
        if values[:3].count(' ') != 3 and values[:3].count(' ') != 0: # Meaning theres bound to be 1 bot and opp
            checking(values[:3], bot, meh, best, [0, 1, 2])
        if values[3:6].count(' ') != 3 and values[3:6].count(' ') != 0:
            checking(values[3:6], bot, meh, best, [3, 4, 5])
        if values[6:].count(' ') != 3 and values[6:].count(' ') != 0:
            checking(values[6:], bot, meh, best, [6, 7, 8])
        if values[::3].count(' ') != 3 and values[::3].count(' ') != 0:
            checking(values[::3], bot, meh, best, [0, 3, 6])
        if values[1::3].count(' ') != 3 and values[1::3].count(' ') != 0:
            checking(values[1::3], bot, meh, best, [1, 4, 7])
        if values[2::3].count(' ') != 3 and values[2::3].count(' ') != 0:
            checking(values[2::3], bot, meh, best, [2, 5, 8])
        if values[::4].count(' ') != 3 and values[::4].count(' ') != 0:
            checking(values[::4], bot, meh, best, [0, 4, 8])
        if values[2:7:2].count(' ') != 3 and values[2:7:2].count(' ') != 0:
            checking(values[2:7:2], bot, meh, best, [2, 4, 6])

        if len(best) > 0:
            position = best[random.randrange(len(best))]
            board[keys[position]] = bot
        else:
            position = meh[random.randrange(len(meh))]
            board[keys[position]] = bot
        return board
