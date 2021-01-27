def drawField(field):
    for row in range(5):
        if row%2==0:
            practicalRow = int(row/2)
            for column in range(5):
                if column%2==0:
                    practicalColumn = int(column/2)
                    if column!=4:
                        print(field[practicalColumn][practicalRow],end='')
                    else:
                        print(field[practicalColumn][practicalRow])
                else:
                    print('|',end='')
        else:
            print('-----')

currentField = [[' ', ' ', ' '],[' ', ' ', ' '],[' ', ' ', ' ']]
drawField(currentField)
player = 1
gameEnd= False
won = 0
while(True):
    print('\n')
    print('Player ',player,' turn: ')
    MoveColumn = int(input("Enter column\n"))
    MoveRow = int(input("Enter row\n"))
    if player == 1:
        if currentField[MoveColumn][MoveRow]==' ':
            currentField[MoveColumn][MoveRow]='X'
            if(MoveColumn==MoveRow):
                if(currentField[0][0]=='X' and currentField[1][1]=='X' and currentField[2][2]=='X'):
                    gameEnd=True
                    won=1
            if(currentField[MoveColumn][0]=='X' and currentField[MoveColumn][1]=='X' and currentField[MoveColumn][2]=='X'):
                gameEnd=True
                won=1
            player = 2
    else:
        if currentField[MoveColumn][MoveRow]==' ':
            currentField[MoveColumn][MoveRow]='O'
            if(MoveColumn==MoveRow):
                if(currentField[0][0]=='O' and currentField[1][1]=='O' and currentField[2][2]=='O'):
                    gameEnd=True
                    won=2
            if(currentField[MoveColumn][0]=='O' and currentField[MoveColumn][1]=='O' and currentField[MoveColumn][2]=='O'):               
                gameEnd=True
                won=2
            player = 1
    print('\n')
    drawField(currentField)
    if gameEnd:
        print('\n')
        print('Player ',won,' won ! Game ends !')
        break