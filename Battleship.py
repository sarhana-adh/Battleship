# --------------------------------------------------Board itself as object with grids as class ----------------------------------------#
import random
import tkinter


def split(word):
    return [char for char in word]
# --------------------------------------------------Players as objects --------------------------------#


class Board:
    def __init__(self):
        self.gridCordinate = []
        self.AirCraftName = 'A'
        self.AirCraftSize = 5
        self.BattleShipName = 'B'
        self.BattleShipSize = 4
        self.SubmarineName = 'S'
        self.SubmarineSize = 3
        self.DestroyerName = 'D'
        self.DestroyerSize = 2
        self.PatrolBoatName = 'P'
        self.PatrolBoatSize = 2


UserPlayer = Board()
ComputerPlayer = Board()

# -------------------------------------first this new game does random placing x ----------------------------------------------------


def Randomplacement(size, letter, CoOrdinatesForTheGrid):
    OrientationToss = random.randint(0, 1)
    if OrientationToss == 0:
        while True:
            Verticalstartpoint = random.randint(0, (10-size))
            Horizontalstartpoint = random.randint(0, 9)
            for x in range(Verticalstartpoint, Verticalstartpoint+size):
                positionValid = False
                if CoOrdinatesForTheGrid[x][Horizontalstartpoint] == " ":
                    positionValid = True
                else:
                    positionValid = False
                    break

            if positionValid:
                for x in range(Verticalstartpoint, Verticalstartpoint+size):
                    CoOrdinatesForTheGrid[x][Horizontalstartpoint] = chr(
                        letter)
                break

    elif OrientationToss == 1:
        while True:
            Horizantalpoint = random.randint(0, (10-size))
            Verticalstartpoint = random.randint(0, 9)
            for x in range(Horizantalpoint, Horizantalpoint+size):
                positionValid = False
                if CoOrdinatesForTheGrid[Verticalstartpoint][x] == " ":
                    positionValid = True
                else:
                    break

            if positionValid:
                for x in range(Horizantalpoint, Horizantalpoint+size):
                    CoOrdinatesForTheGrid[Verticalstartpoint][x] = chr(letter)
                break


def PrintTheBoard(CoOrdinatesForTheGrid, Gamer):
    print("\nBoard of " + str(Gamer))
    print("  a b c d e f g h i j\n")
    for x in range(10):
        print(x, end=" ")
        for y in range(10):
            print(CoOrdinatesForTheGrid[x][y], end=" ")
        print("")


def CheckTheBoard(CoOrdinatesForTheGrid, Gamer):
    endGame = True
    for x in range(10):
        for y in range(10):
            if CoOrdinatesForTheGrid[x][y].isupper():
                endGame = False
                break
                break
    if endGame:
        print("The Game has finished." + Gamer + "won")
        exit(0)


# CoOrdinatesForTheGridUser = []

for i in range(10):
    rows = []
    for j in range(10):
        rows.append(" ")
    UserPlayer.gridCordinate.append(rows)


Randomplacement(5, 65, UserPlayer.gridCordinate)
Randomplacement(4, 66, UserPlayer.gridCordinate)
Randomplacement(3, 83, UserPlayer.gridCordinate)
Randomplacement(3, 68, UserPlayer.gridCordinate)
Randomplacement(2, 80, UserPlayer.gridCordinate)
PrintTheBoard(UserPlayer.gridCordinate, "Computer")
# print("\n \n GRID ARRANGEMENT FOR USER ")
# print("  a b c d e f g h i j\n")
# for x in range(10):
#     print (x, end=" ")
#     for y in range(10):
#         print(CoOrdinatesForTheGridUser[x][y], end=" ")
#     print("")


#  Random arrangement for Players
for i in range(10):
    rows = []
    for j in range(10):
        rows.append(" ")
    ComputerPlayer.gridCordinate.append(rows)

Randomplacement(5, 65, ComputerPlayer.gridCordinate)
Randomplacement(4, 66, ComputerPlayer.gridCordinate)
Randomplacement(3, 83, ComputerPlayer.gridCordinate)
Randomplacement(3, 68, ComputerPlayer.gridCordinate)
Randomplacement(2, 80, ComputerPlayer.gridCordinate)
PrintTheBoard(ComputerPlayer.gridCordinate, "User")


myDict = {
    'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9
}
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]


while True:
    # Checks if either computer or user won, by checking each arrays/boards
    CheckTheBoard(UserPlayer.gridCordinate, " User ")
    CheckTheBoard(ComputerPlayer.gridCordinate, " Computer ")
    userGuess = input("Type in your guess in format 4a. For reference the number 5th row from top, therefore the grid starts from 0 and ends at 9. While the a represents the first column from left. The columns ends at alphabet j \n")
    Guessed = split(userGuess)
    GuessedList = []
    if (int(Guessed[0]) in range(0, 9)) & (str(Guessed[1]) in alphabet):
        if userGuess in GuessedList:
            print("The guess is repeated")

            # else check when actually go through eerything
            xCoordinate = int(Guessed[0])
            yCoordinate = myDict.get(Guessed[1])
 # function gets added here
        elif UserPlayer.gridCordinate[int(Guessed[0])][myDict.get(Guessed[1])] != " ":
            # need to change all capital letters to lower letter
            needToreplace = UserPlayer.gridCordinate[int(
                Guessed[0])][myDict.get(Guessed[1])]
            for x in range(10):
                for y in range(10):
                    if UserPlayer.gridCordinate[x][y] == needToreplace:
                        UserPlayer.gridCordinate[x][y] = UserPlayer.gridCordinate[x][y].lower(
                        )
            GuessedList.append(userGuess)
            PrintTheBoard(UserPlayer.gridCordinate, "Computer")

        elif UserPlayer.gridCordinate[int(Guessed[0])][myDict.get(Guessed[1])] == " ":
            UserPlayer.gridCordinate[int(
                Guessed[0])][myDict.get(Guessed[1])] = "x"
            GuessedList.append(userGuess)
            PrintTheBoard(UserPlayer.gridCordinate, "Computer")

    else:
        print("Try Again!! \n")

    while True:
        # Is being randomly guessed by the computer
        GuessListX = []
        GuessListY = []
        GuessByComputerX = random.randint(0, 9)
        GuessByComputerY = random.randint(0, 9)
        if GuessByComputerX in GuessListX:
            index = GuessListX.index(GuessByComputerX)
            if GuessListY[index] == GuessByComputerY:
                print("")  # repeated hence no need to add to list
        else:
            GuessListX.append(GuessByComputerX)
            GuessListY.append(GuessByComputerY)
            if ComputerPlayer.gridCordinate[GuessByComputerY][GuessByComputerY] != " ":
                # need to change all capital letters to lower letter
                needToreplace = ComputerPlayer.gridCordinate[GuessByComputerX][GuessByComputerY]
                for x in range(10):
                    for y in range(10):
                        if ComputerPlayer.gridCordinate[x][y] == needToreplace:
                            ComputerPlayer.gridCordinate[x][y] = ComputerPlayer.gridCordinate[x][y].lower(
                            )
                PrintTheBoard(ComputerPlayer.gridCordinate, "User")

            elif ComputerPlayer.gridCordinate[GuessByComputerX][GuessByComputerY] == " ":
                ComputerPlayer.gridCordinate[GuessByComputerX][GuessByComputerY] = "x"
                PrintTheBoard(ComputerPlayer.gridCordinate, "User")

            break
