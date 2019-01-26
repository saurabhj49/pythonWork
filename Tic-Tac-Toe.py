board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
new_board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

def print_board(new_board):
    for i in range(0,3):
        print ("\t\t", end='')
        for j in range(0,3):
            print (new_board[i][j]+' ', end='')
        print('\n')

def check_input(new_input, new_board):
    ls1 = new_input.split(' ')
    if ' ' not in new_input:
        print ("\t Wrong Input!! Space should be there between two input values")
        return False
    elif not (ls1[0].isdigit() and ls1[1].isdigit() and (ls1[0] in ['1', '2', '3']) and (ls1[1] in ['1', '2', '3'])):
        print("\t Wrong Input!! Input should be between 1-3 only")
        return False
    elif new_board[int(ls1[0])-1][int(ls1[1])-1] in ['X', 'O']:
        print("\t Wrong Input!! Place already filled")
        return False
    else:
        return True

def play_on_board(new_board, new_input, symbol):
    ls = new_input.split(' ')
    new_board[int(ls[0])-1][int(ls[1])-1] = symbol
    print_board(new_board)

def check_winner(new_board, symbol):
    if (new_board[0][0]==new_board[1][0]==new_board[2][0]==symbol) or (new_board[0][1]==new_board[1][1]==new_board[2][1]==symbol) or (new_board[0][2]==new_board[1][2]==new_board[2][2]==symbol) or (new_board[0][0]==new_board[1][1]==new_board[2][2]==symbol) or (new_board[0][2]==new_board[1][1]==new_board[2][0]==symbol) or (new_board[0][0]==new_board[0][1]==new_board[0][2]==symbol) or (new_board[1][0]==new_board[1][1]==new_board[1][2]==symbol) or (new_board[2][0]==new_board[2][1]==new_board[2][2]==symbol):
        return True
    else:
        return False
        

def play_tic_tac(new_board):
    game = 'playing'
    print ("\t"+"Let's play TIC-TAC-TOE")
    print_board(new_board)
    p1 = input("1st Player name and symbol 'X' : ")
    p2 = input("2nd Player name and symbol 'O' : ")
    print ("\tHow to play ?")
    print ("\tChoose between 1 - 3 for row and column, in same line with 1 space. For marking position on board.")
    print ("\t Ex- if I want to check on 1st row 1st column, input will be - '1 1'")
    print ("\tLet us start the game! GoodLuck!!")
    while (game != 'end'):
        check_in = False
        while ( check_in == False):
            player_input = input(p1+" Enter your input : ")
            check_in = check_input(player_input, new_board)
            if check_in != False:
                play_on_board(new_board, player_input, "X")
                if check_winner(new_board, "X"):
                    print ("\t"+p1+ " have won the game!!!")
                    game = 'end'
                    break
        check_in = False
        while ( check_in == False):
            player_input = input(p2+" Enter your input : ")
            check_in = check_input(player_input, new_board)
            if check_in != False:
                play_on_board(new_board, player_input, "O")
                if check_winner(new_board, "O"):
                    print ("\t"+p2+ " have won the game!!!")
                    game = 'end'
                    break
            

play_tic_tac(new_board)
