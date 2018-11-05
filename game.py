boards = [" " for i in range(9)]

def print_board():
    row1 = "|{}|{}|{}|".format(boards[0],boards[1],boards[2])
    row2 = "|{}|{}|{}|".format(boards[3],boards[4],boards[5])
    row3 = "|{}|{}|{}|".format(boards[6],boards[7],boards[8])
    print ("\n")
    print (row1)
    print (row2)
    print (row3)
    print ("\n")


def player_move(icon):
    if icon == "X":
        number = 1
    elif icon == "O":
        number = 2
    print ("Your turn player {}".format(icon))
    choice = input("Enter your move (1-9)")
    if boards[choice-1] == " ":
        boards[choice-1] = icon
    else:
        print ()
        print ("That space is taken!")

def is_victory(icon):
    if      (boards[0] == icon and boards[1] == icon and boards[2] == icon) or \
            (boards[3] == icon and boards[4] == icon and boards[5] == icon) or \
            (boards[6] == icon and boards[7] == icon and boards[8] == icon) or \
            (boards[0] == icon and boards[3] == icon and boards[6] == icon) or \
            (boards[1] == icon and boards[4] == icon and boards[7] == icon) or \
            (boards[2] == icon and boards[5] == icon and boards[8] == icon) or \
            (boards[0] == icon and boards[4] == icon and boards[8] == icon) or \
            (boards[2] == icon and boards[4] == icon and boards[6] == icon):
        return True
    else:
        return False

def is_draw():
    if " " not in boards:
        return True
    else:
        return False

while True:
    print_board()
    player_move("X")
    print_board()
    if is_victory("X"):
        print ("X Wins!, Congratulations!")
        break
    elif is_draw():
        print ("It's Draw!")
    player_move("O")
    if is_victory("O"):
        print ("O Wins!, Congratulations!")
        break
    elif is_draw():
        print ("It's Draw!")
