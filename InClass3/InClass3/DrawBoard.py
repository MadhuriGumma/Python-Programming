def drawGameboard(board):
    print ('    |   |   ')
    print ('' +board[6]+ '    | ' +board[7]+ '  |   ' +board[8] )
    print ('    |   |   ')
    print ('---------------')
    print ('    |   |   ')
    print ('' +board[3]+ '    | ' +board[4]+ '  | ' +board[5] )
    print ('    |   |   ')
    print('-----------------')
    print ('    |   |   ')
    print ('' +board[0]+ '    | ' +board[1]+ '  |' +board[2] )
    print ('    |   |   ')

n= input('Enter the no. of grids in game board:')
print('The n value is:', n)
i=0
for i in n:
    drawGameboard(['', '', '', '', '', '', '', '', ''])