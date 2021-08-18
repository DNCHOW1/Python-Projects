def initializeBoard(board): # Will create the mini blocks of the whole board
    topRow = '{}|{}|{}'.format(board['top-L'], board['top-M'], board['top-R'])
    midRow = '{}|{}|{}'.format(board['mid-L'], board['mid-M'], board['mid-R'])
    lowRow = '{}|{}|{}'.format(board['low-L'], board['low-M'], board['low-R'])
    keys = list(board.keys())
    bcomponets = [topRow, midRow, lowRow, keys, board]
    return bcomponets

def generatePortion(block1, block2, block3):
    seperator = '-+-+-'
    seperation = seperator + '?' + seperator + '?' + seperator
    row1 = ('{}?{}?{}'.format(block1[0], block2[0], block3[0]))
    row2 = ('{}?{}?{}'.format(block1[1], block2[1], block3[1]))
    row3 = ('{}?{}?{}'.format(block1[2], block2[2], block3[2]))
    print('{}\n{}\n{}\n{}\n{}'.format(row1, seperation, row2, seperation, row3))

def makeBoards(TLB, TMB, TRB, MLB, MMB, MRB, LLB, LMB, LRB):
    generatePortion(TLB, TMB, TRB)
    print('=====?=====?=====')
    generatePortion(MLB, MMB, MRB)
    print('=====?=====?=====')
    generatePortion(LLB, LMB, LRB)
