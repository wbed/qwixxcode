import random

def playerStart():
    playerTable = []
    flag5 = True
    while flag5 == True:
        noPlayers = int(input("How Many Players?(Min: 2/Max: 5): "))
        if noPlayers == 2 or noPlayers == 3 or noPlayers == 4 or noPlayers == 5:
            flag5 = False
        else:
            print("Invalid Input.")
            flag5 = True

    for i in range(0, noPlayers):
        playerTable.append(input("Player Name: "))
        print(playerTable)

    activePlayer = playerTable[random.randint(0, noPlayers - 1)]

    if playerTable.index(activePlayer) == len(playerTable) - 1:
        index = 0
    else:
        index = playerTable.index(activePlayer) + 1

    activePlayer = playerTable[index]

    return activePlayer, playerTable, noPlayers


def rules():
    flag6 = True
    while flag6 == True:
        rulesI = input("Do you want to know the rules?(y/n): ")
        if rulesI == "y" or rulesI == "n":
            flag6 = False
            if rulesI == "y":
                f = open("rules.txt", 'r')
                file_contents = f.read()
                print('\n' + file_contents)
            else:
                print("Ok, enjoy your game!")
        else:
            flag6 = True
            print("Invalid Input.")


def makeGameBoard():
    gameBoard = [
        [
            [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, '🔒', 'R'],  #GB1
            [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, '🔒', 'Y'],
            [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, '🔒', 'G'],
            [12, 12, 10, 9, 8, 7, 6, 5, 4, 3, 2, '🔒', 'B']
        ],
        [
            [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, '🔒', 'R'],  #GB2
            [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, '🔒', 'Y'],
            [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, '🔒', 'G'],
            [12, 12, 10, 9, 8, 7, 6, 5, 4, 3, 2, '🔒', 'B']
        ],
        [
            [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, '🔒', 'R'],  #GB3
            [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, '🔒', 'Y'],
            [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, '🔒', 'G'],
            [12, 12, 10, 9, 8, 7, 6, 5, 4, 3, 2, '🔒', 'B']
        ],
        [
            [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, '🔒', 'R'],  #GB4
            [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, '🔒', 'Y'],
            [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, '🔒', 'G'],
            [12, 12, 10, 9, 8, 7, 6, 5, 4, 3, 2, '🔒', 'B']
        ],
        [
            [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, '🔒', 'R'],  #GB5
            [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, '🔒', 'Y'],
            [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, '🔒', 'G'],
            [12, 12, 10, 9, 8, 7, 6, 5, 4, 3, 2, '🔒', 'B']
        ]
    ]
    return gameBoard


def diceRoll(colouredDice):
    for i in range(0, len(colouredDice)):
        colouredDice[i][1] = random.randint(1, 6)
    return colouredDice


def addWhiteDice(colouredDice):
    whiteDiceTotal = colouredDice[0][1] + colouredDice[1][1]
    return whiteDiceTotal


def crossOutRows(DiceTotal, noPlayers_, gameBoard, colourChoice):
    if colourChoice == "r":
        gameBoard[noPlayers_ - 1][0][DiceTotal - 2] = "X"
    elif colourChoice == "y":
        gameBoard[noPlayers_ - 1][1][DiceTotal - 2] = "X"
    elif colourChoice == "g":
        gameBoard[noPlayers_ - 1][2][12 - DiceTotal] = "X"
    elif colourChoice == "b":
        gameBoard[noPlayers_ - 1][3][12 - DiceTotal] = "X"

    print('\n' + playerTable[noPlayers_ - 1] + "'s Gameboard: ")
    print(*gameBoard[noPlayers_ - 1], sep="\n")

    return gameBoard


def crossOutWhite(whiteDiceTotal_, noPlayers, penPoint):
    DiceTotal = whiteDiceTotal_
    while noPlayers > 0:
        flag1 = True
        while flag1 == True:
            print('\n' + playerTable[noPlayers - 1] +
                  ", do you want to cross out the total of white dice?(y/n): ")
            ifskip = input('')
            if ifskip == 'y':
                flag9 = True
                while flag9 == True:
                    print("Which row do you want to cross out", DiceTotal,
                          "in?")
                    colourChoice = input('(r/y/g/b): ')
                    if colourChoice == 'r' or colourChoice == 'y' or colourChoice == 'g' or colourChoice == 'b':
                        print("Crossed out", DiceTotal,
                              "in " + colourChoice + ".")
                        flag9 = False
                    else:
                        print("Invalid Input.")
                        flag9 = True
                crossOutRows(DiceTotal, noPlayers, gameBoard, colourChoice)
                flag1 = False
                noPlayers = noPlayers - 1
                penPoint = 0
            elif ifskip == "n":
                print(playerTable[noPlayers - 1] + " skipped their turn.")
                flag1 = False
                if playerTable[noPlayers - 1] == activePlayer:
                    penPoint = 1
                noPlayers = noPlayers - 1
            else:
                print("Invalid Input.")
                flag1 = True
    return penPoint


def crossOutColour(colouredDice, penPoint):
    flag1 = True
    print("\nDice Roll:", colouredDice)
    while flag1 == True:
        print('\n' + activePlayer +
              ", do you want to cross out the total of coloured dice?(y/n): ")
        activeDo = input()
        if activeDo == 'y':
            flag2 = True
            flag3 = True
            while flag2 == True:
                print('\n' + activePlayer +
                      ", what white die do you want to add?(w1/w2):")
                colouredDice1 = input("")
                if colouredDice1 == 'w1' or colouredDice1 == 'w2':
                    flag2 = False
                else:
                    print("Invalid Input.")
                    flag2 = True

            while flag3 == True:
                print('\n' + activePlayer +
                      ", what coloured die do you want to add?(r/y/g/b):")
                colourChoice = input("")
                if colourChoice == 'r' or colourChoice == 'y' or colourChoice == 'g' or colourChoice == 'b':
                    flag3 = False
                else:
                    print("Invalid Input.")
                    flag3 = True

            if colouredDice1 == 'w1':
                colouredDice1 = colouredDice[0][1]
            elif colouredDice1 == 'w2':
                colouredDice1 = colouredDice[1][1]
            if colourChoice == 'r':
                colouredDice2 = colouredDice[2][1]
            elif colourChoice == 'y':
                colouredDice2 = colouredDice[3][1]
            elif colourChoice == 'g':
                colouredDice2 = colouredDice[4][1]
            elif colourChoice == 'b':
                colouredDice2 = colouredDice[5][1]

            colouredDiceTotal = colouredDice1 + colouredDice2
            DiceTotal = colouredDiceTotal
            flag1 = False

            print("Crossed out", DiceTotal, "in " + colourChoice + ".")
            crossOutRows(DiceTotal, noPlayers, gameBoard, colourChoice)
        elif activeDo == "n":
            penPoint = penPoint + 1
            if penPoint == 2:
                penaltyTable[index] = penaltyTable[index] + 1
                print(activePlayer + " received a penalty point.\n")
            print(activePlayer + " skipped their turn.\n")
            flag1 = False
        else:
            print("Invalid Input.")
            flag1 = True


def makePenaltyTable(noPlayers):
    penaltyTable = []

    for i in range(0, noPlayers):
        penaltyTable.append(0)

    return penaltyTable


gameBoard = makeGameBoard()

rules()

activePlayer, playerTable, noPlayers = playerStart()

penaltyTable = makePenaltyTable(noPlayers)

endGame = False
while endGame == False:
    penPoint = 0

    if playerTable.index(activePlayer) == len(playerTable) - 1:
        index = 0
    else:
        index = playerTable.index(activePlayer) + 1

    activePlayer = playerTable[index]
    colouredDice = [['w1', 0], ['w2', 0], ['r', 0], ['y', 0], ['g', 0],
                    ['b', 0]]
    diceRoll_ = diceRoll(colouredDice)
    print(
        '\n---------------------------------------------------------------------------------------------'
    )
    print('Active Player:', activePlayer, '| Dice Roll: ', diceRoll_, '\n')

    whiteDiceTotal_ = addWhiteDice(colouredDice)
    print('The white dice add up to:', whiteDiceTotal_)

    penPoint = crossOutWhite(whiteDiceTotal_, noPlayers, penPoint)

    crossOutColour(colouredDice, penPoint)

    for i in range(0, noPlayers):
        print(playerTable[i] + "'s Penalties:", penaltyTable[i])
        if penaltyTable[i] >= 4:
            endGame = True

#    if lockedRows == 2:
#        endGame = True

    input("\nPress enter for new diceroll: ")

print("\n==GAME OVER==")