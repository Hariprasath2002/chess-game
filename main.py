from turtle import pos
from pieces import *

def print_board(board):
    def print_alphabets_row():
        print("\t",end="")
        for i in ["a","b","c","d","e","f","g","h"]:
            print(i,end="\t")
        print()
    print_alphabets_row()
    for idx, row in enumerate(reversed(board)):
        print(8-idx,end="\t")
        for column in row:
            if column:
                print(column.get_coin_name(),end="\t")
            else:
                print(column,end="\t")
        print()
    # for idx, row in enumerate(board):
    #     print(idx+1,end="\t")
    #     for column in row:
    #         if column:
    #             print(column.get_coin_name(),end="\t")
    #         else:
    #             print(column,end="\t")
    #     print()
    print_alphabets_row()
def get_new_board():
    board = []
    for i in range(8):
        board.append([""]*8)
    board[0][0] = Rook("W")
    board[0][1] = Knight("W")
    board[0][2] = Bishop("W")
    board[0][3] = Queen("W")
    board[0][4] = King("W")
    board[0][5] = Bishop("W")
    board[0][6] = Knight("W")
    board[0][7] = Rook("W")

    board[1] = [Pawn("W") for i in range(8)]


    board[7][0] = Rook("B")
    board[7][1] = Knight("B")
    board[7][2] = Bishop("B")
    board[7][3] = Queen("B")
    board[7][4] = King("B")
    board[7][5] = Bishop("B")
    board[7][6] = Knight("B")
    board[7][7] = Rook("B")

    board[6] = [Pawn("B") for i in range(8)]

    return board
def get_coin(position):
    row = int(position[1])-1
    column = ord(position[0])-97
    # print(position,row,column)

    return board[row][column]

if __name__=="__main__":
    board = get_new_board()
    '''
    Debug
    '''
    # moves = [("a2","a4"),("a7","a5"),("a1","a3"),("a8","a6"),("a3","h3"),("a6","h6")]
    # for move in moves:
    #     coin = get_coin(move[0])
    #     coin.move_to(move[0],move[1],board)
    print_board(board)
    turn = "W"
    while True:
        coin_from = input(turn+" > ")
        if coin_from.lower() == "exit":
            break
        if coin_from.lower() == "print":
            print_board(board)
            continue
        
        coin = get_coin(coin_from)
        print(coin.get_coin_name())
        if coin.get_coin_name()[0] != turn:
            print("This is "+turn+"'s turn. Choose the right coin")
            continue

        possible_moves = coin.possible_moves(coin_from,board)
        print("Possible moves : ",possible_moves)

        if len(possible_moves)==0:
            print("Try Again")
            continue

        coin_to = input("move to > ")
        
        coin.move_to(coin_from,coin_to,board)

        if coin.get_coin_name()[0] == turn:
            if turn=="W":
                turn = "B"
            else:
                turn = "W"