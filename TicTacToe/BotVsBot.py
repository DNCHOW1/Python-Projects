import BigBoard, BotFunctions, DifferentBlocks, random, time
# NOTE: Add a score talley, to list what blocks the bots took over. Also, comments

def botBoard():
    randomBoard = random.randrange(len(allBoards))
    return allBoards[randomBoard][4], allBoards[randomBoard][3], randomBoard
    # Returns dictionary, keys, and which board it is

def initializeAll():
    global topLeftBoard, topMidBoard, topRightBoard
    global midLeftBoard, midMidBoard, midRightBoard
    global lowLeftBoard, lowMidBoard, lowRightBoard
    #global allBoards
    topLeftBoard = BigBoard.initializeBoard(DifferentBlocks.tLBoard.board)
    topMidBoard = BigBoard.initializeBoard(DifferentBlocks.tMBoard.board)
    topRightBoard = BigBoard.initializeBoard(DifferentBlocks.tRBoard.board)
    midLeftBoard = BigBoard.initializeBoard(DifferentBlocks.mLBoard.board)
    midMidBoard = BigBoard.initializeBoard(DifferentBlocks.mMBoard.board)
    midRightBoard = BigBoard.initializeBoard(DifferentBlocks.mRBoard.board)
    lowLeftBoard = BigBoard.initializeBoard(DifferentBlocks.lLBoard.board)
    lowMidBoard = BigBoard.initializeBoard(DifferentBlocks.lMBoard.board)
    lowRightBoard = BigBoard.initializeBoard(DifferentBlocks.lRBoard.board)

def tie(board):
    tieCounter = 0
    for i in board.values():
        if i == 'X' or i =='O':
            tieCounter += 1
        else:
            pass
    if tieCounter == 9:
        return True
    else:
        return False

initializeAll()
allBoards = [topLeftBoard, topMidBoard, topRightBoard,
             midLeftBoard, midMidBoard, midRightBoard,
             lowLeftBoard, lowMidBoard, lowRightBoard]
BigBoard.makeBoards(topLeftBoard, topMidBoard, topRightBoard,
                    midLeftBoard, midMidBoard, midRightBoard,
                    lowLeftBoard, lowMidBoard, lowRightBoard,)
print('\n')
moves = 0
fbot, sbot = 'X', 'O'
fbot_points, sbot_points = 0,0
bots = [fbot, sbot]
bot_points = [fbot_points, sbot_points]
while len(allBoards) != 0:
    try:
        for i in range(2):
            moves += 1
            time.sleep(1)
            bot_board, board_keys, currentBoard = botBoard()
            BotFunctions.botMove(bot_board, bots[i], board_keys)
            initializeAll() # Updates the boards
            BigBoard.makeBoards(topLeftBoard, topMidBoard, topRightBoard, # And makes the new boards
                                midLeftBoard, midMidBoard, midRightBoard,
                                lowLeftBoard, lowMidBoard, lowRightBoard,)
            boardCondition = BotFunctions.winCondition(bot_board, bots[i])
            if boardCondition == True:
                bot_points[i] += 1
                allBoards.pop(currentBoard)
            else:
                TIE = tie(bot_board)
                if TIE == True:
                    allBoards.pop(currentBoard)
                else:
                    pass
                pass

            print('\n')
            if i == 1:
                i = 0
    except ValueError:
        break

print('X Points:{}'.format(bot_points[0]))
print('O Points:{}'.format(bot_points[1]))
print('X took {}.'.format('s'))
print('O took {}.'.format('s'))
print('Moves: {}'.format(moves))
