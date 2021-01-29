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
    if (MoveColumn<=3 and MoveColumn>=1) and (MoveRow<=3 and MoveRow>=1):
        if player == 1:
            if currentField[MoveColumn-1][MoveRow-1]==' ':
                currentField[MoveColumn-1][MoveRow-1]='X'
                if(MoveColumn==MoveRow):
                    if(currentField[0][0]=='X' and currentField[1][1]=='X' and currentField[2][2]=='X'):
                        gameEnd=True
                        won=1
                if((currentField[MoveColumn-1][0]=='X' and currentField[MoveColumn-1][1]=='X' and currentField[MoveColumn-1][2]=='X')or(currentField[0][MoveRow-1]=='X' and currentField[1][MoveRow-1]=='X' and currentField[2][MoveRow-1]=='X')):
                    gameEnd=True
                    won=1
                if(currentField[2][0]=='X' and currentField[1][1]=='X' and currentField[0][2]=='X'):
                    gameEnd=True
                    won=1
                player = 2
        else:
            if currentField[MoveColumn-1][MoveRow-1]==' ':
                currentField[MoveColumn-1][MoveRow-1]='O'
                if(MoveColumn==MoveRow):
                    if(currentField[0][0]=='O' and currentField[1][1]=='O' and currentField[2][2]=='O'):
                        gameEnd=True
                        won=2
                if((currentField[MoveColumn-1][0]=='O' and currentField[MoveColumn-1][1]=='O' and currentField[MoveColumn-1][2]=='O')or(currentField[0][MoveRow-1]=='O' and currentField[1][MoveRow-1]=='O' and currentField[2][MoveRow-1]=='O')):               
                    gameEnd=True
                    won=2
                if(currentField[2][0]=='X' and currentField[1][1]=='X' and currentField[0][2]=='X'):
                    gameEnd=True
                    won=1
                player = 1
        print('\n')
        drawField(currentField)
        if gameEnd:
            print('\n')
            print('Player ',won,' won ! Game ends !')
            break
    else:
        print("Invalid row or column! Please try again!")