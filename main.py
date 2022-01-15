import os
board = {'45': 2, '44': 1, '34':2, '35': 1}
directions = {"top_left": -11, "top":-10, "top_right":-9, "left": -1,
              "right": +1, "bot_left": +9, "bot": +10, "bot_right": +11}
board_size = 8

def update_board():

    for i in range(5):
        print('')
    print("   1  2  3  4  5  6  7  8")
    for r in range(board_size):

        print(str(r) + "  ", end='')

        for c in range(board_size):

            key = str(str(r) + str(c+1))
            key = board.get(key)

            if key == None:
                print(".  ", end= '')
            elif key == 1:
                print("o  ", end= '')
            elif key == 2:
                print("x  ", end= '')
            else:
                print(key, end= '')

        print(r)

    #print("   1  2  3  4  5  6  7  8")
    print()

def play_chess(playernum):

    location = input("Player " + str(playernum) + ", play a chess on a tile: ")

    try:

        if location.lower() == 'end':
            check_winner()
            return

        if location.lower() == 'pass':
            update_board()
            print("Player " + str(playernum) + " passed...")
            play_chess(2 if playernum == 1 else 1)
            return

        if board.get(str(location)) != None:
            update_board()
            print("Spot is Occupied, Try Again")
            play_chess(playernum)
            return

        placements = validate_location(location, playernum)
        if len(placements) == 0:
            update_board()
            print("The spot needs to take a chess to be valid, Try Again")
            play_chess(playernum)
            return

        #place chess at the original position, and also all the position that is valid
        place_chess(location, playernum)
        for i in range(len(placements)):
            if(placements[i] != None):
                place_chess(placements[i], playernum)

        update_board()
    except:
        update_board()
        print("Error handling request, try again")
        play_chess(playernum)
        return

def validate_location(location, playernum):

    checkfornum = 2 if playernum == 1 else 1
    valid_loactions = []

    #for each directions, check whether the tile matches with the numbers its looking for, if it does move forward and repeats
    for i in directions:
        #the temp list is to store every valid tile for a certain direction, until it is proven invalid(reaches a none tile) or valid (reaches my own tile)
        temp_valid = []
        print(i)

        for c in range(board_size):
            result = board.get(str(int(location) + ((c+1) * directions[i])))

            if result == checkfornum:
                print('the location is valid for direction ' + str(i) + " at " + str(int(location) + ((c+1) * directions[i])))
                temp_valid.append(str(int(location) + ((c+1) * directions[i])))
                continue
            elif result == playernum:
                valid_loactions += (temp_valid)
                print("find my own piece at " + str(int(location) + ((c+1) * directions[i])) + ' returning the templist')
                break
            elif result == None:
                print("finding non at " + str(int(location) + ((c+1) * directions[i])) + " deleting the temp list")
                break

    if len(valid_loactions) == 0:
        print("location not valid")
        return []
    else:
        print(valid_loactions)
        return valid_loactions

def place_chess(location, playernum):
    board[location] = playernum
    print("played at " + location)

def check_winner():
    player1 = 0
    player2 = 0
    for i in board:
        if board[i] == 1:
            player1 += 1
        else:
            player2 += 1

    if player1 == player2:
        print("Game is a DRAW at a score of " + str(player1) + "! GG~~")
    elif player1 > player2:
        print("Player 1 Wins at a score of " + str(player1) + "!!! Good Game!!!")
    elif player2 > player1:
        print("Player 2 Wins at a score of " + str(player2) + "!!! Good Game!!!")
    else:
        print("Error determining winner... :((")

    os._exit(1)



input("This is Othello, each move you play must capture/ reverse an opponents' chess, \n" 
      "You must place a chess next to an opponent's chess, all opponent's pieces that are \n"
      "between your new pieces and old pieces will be reversed. \n"
      'Try placing a move by typing coordinates "Column" + "Row", for Example, 33, 46, 55) \n'
      '"To pass simply type "pass" to pass your turn, type "end" to end game'
      "Press Enter to Initial the Game: ")

update_board()
while True:
    play_chess(1)
    play_chess(2)
