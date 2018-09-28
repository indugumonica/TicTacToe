def display_board(l):
    print l[:3]
    print l[3:6]
    print l[6:]


def player_input():
    value = int(input("please enter player 1 input: "))
    return value


def player2_input():
    value = int(input("please enter player 2 input: "))
    return value


def wincheck(l):
    if l[0] == l[1] == l[2] and l[0] != 0:
        return True
    elif l[0] == l[3] == l[6] and l[0] != 0:
        return True
    elif l[0] == l[4] == l[8] and l[0] != 0:
        return True
    elif l[1] == l[4] == l[7] and l[1] != 0:
        return True
    elif l[3] == l[4] == l[5] and l[3] != 0:
        return True
    elif l[2] == l[4] == l[6] and l[2] != 0:
        return True
    elif l[6] == l[7] == l[8] and l[6] != 0:
        return True
    elif l[2] == l[5] == l[8] and l[2] != 0:
        return True

    else:
        return False


def main():
    l = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    while l.count(0) > 1:
        display_board(l)
        player1 = player_input()
        if l[player1] == 0:
            l[player1] = 1
        else:
            print('this block is already filled')
            player1 = player_input()
        if wincheck(l):
            print('player 1 won the game')
            break
        display_board(l)
        player2 = player2_input()
        if l[player2] == 0:
            l[player2] = 2
        else:
            print('this block is already filled')
            player2 = player2_input()
        if wincheck(l):
            print('player 2 won the game ')
            break
    if not wincheck(l):
        print ('no one one the game')
        display_board(l)

def tic_tac_toe():
    while raw_input("Do you want to play: yes or no ") == 'yes':
        main()
    print "Okay bye bye"
