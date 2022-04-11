import re


class Coin:
    def __init__(self,colour):
        self.coin_name = None
        self.colour = colour
    
    def get_coin_name(self):
        return self.coin_name
    
    def possible_moves(self,from_position=None,board=None):
        return []
    
    def move_to(self, from_position=None,to_position=None,board=None):
        return False

    def get_board_coordinates(self, from_position):
        row = int(from_position[1])-1
        column = ord(from_position[0])-97
        return row, column
    
    def get_board_string_position(self,row, column):
        return chr(97+column)+str(row)

class Rook(Coin):
    def __init__(self, colour):
        super().__init__(colour)
        self.coin_name = colour+"_R"
    
    def possible_moves(self,from_position=None,board=None):
        row, column = self.get_board_coordinates(from_position)
        # print("[Debug] Current : ",row," ", column)    
        possible_moves = []
        if self.colour=="W":
            #Check in Forward Rows
            for r in range(row+1,8):
                if (board[r][column] == ""):
                    possible_moves.append(self.get_board_string_position(r+1,column))
                elif (board[r][column].coin_name.startswith("B")):
                    possible_moves.append(self.get_board_string_position(r+1,column))
                    break
                else :
                    break
            #Check Backward Rows
            for r in range(row-1,-1,-1):
                if (board[r][column] == ""):
                    possible_moves.append(self.get_board_string_position(r+1,column))
                elif (board[r][column].coin_name.startswith("B")):
                    possible_moves.append(self.get_board_string_position(r+1,column))
                    break
                else :
                    break
            #Check in Forward Columns
            for c in range(column+1,8):
                if (board[row][c] == ""):
                    possible_moves.append(self.get_board_string_position(row+1,c))
                elif board[row][c].coin_name.startswith("B"):
                    possible_moves.append(self.get_board_string_position(row+1,c))
                    break
                else:
                    break
            #Check in Backward Columns
            for c in range(column-1,-1,-1):
                if (board[row][c] == ""):
                    possible_moves.append(self.get_board_string_position(row+1,c))
                elif board[row][c].coin_name.startswith("B"):
                    possible_moves.append(self.get_board_string_position(row+1,c))
                    break
                else:
                    break
        else:
            for r in range(row-1,-1,-1):
                if (board[r][column] == ""):
                    possible_moves.append(self.get_board_string_position(r+1,column))
                elif (board[r][column].coin_name.startswith("W")):
                    possible_moves.append(self.get_board_string_position(r+1,column))
                    break
                else :
                    break
            for r in range(row+1,8):
                if (board[r][column] == ""):
                    possible_moves.append(self.get_board_string_position(r+1,column))
                elif (board[r][column].coin_name.startswith("W")):
                    possible_moves.append(self.get_board_string_position(r+1,column))
                    break
                else :
                    break
            for c in range(column+1,8):
                if (board[row][c] == ""):
                    possible_moves.append(self.get_board_string_position(row+1,c))
                elif board[row][c].coin_name.startswith("W"):
                    possible_moves.append(self.get_board_string_position(row+1,c))
                    break
                else:
                    break
            for c in range(column-1,-1,-1):
                if (board[row][c] == ""):
                    possible_moves.append(self.get_board_string_position(row+1,c))
                elif board[row][c].coin_name.startswith("W"):
                    possible_moves.append(self.get_board_string_position(row+1,c))
                    break
                else:
                    break
        return possible_moves
    
    def move_to(self, from_position=None, to_position=None, board=None):
        possible_moves = self.possible_moves(from_position,board)

        if to_position not in possible_moves:
            print("Move not possible")
            return False
        
        current_row, current_column = self.get_board_coordinates(from_position)
        new_row, new_column = self.get_board_coordinates(to_position)

        board[current_row][current_column] = ""
        board[new_row][new_column] = self

        return False

class Knight(Coin):
    def __init__(self, colour):
        super().__init__(colour)
        self.coin_name = colour+"_N"

class Bishop(Coin):
    def __init__(self, colour):
        super().__init__(colour)
        self.coin_name = colour+"_B"

class Queen(Coin):
    def __init__(self, colour):
        super().__init__(colour)
        self.coin_name = colour+"_Q"

class King(Coin):
    def __init__(self, colour):
        super().__init__(colour)
        self.coin_name = colour+"_K"

class Pawn(Coin):
    def __init__(self, colour):
        super().__init__(colour)
        self.coin_name = colour+"_P"
    
    def possible_moves(self,from_position=None,board=None):
        row, column = self.get_board_coordinates(from_position)
        # print("[Debug] Pawn Current : ",row," ", column)
        possible_moves = []
        if self.colour=="W":
            for r in range(row+2,row+4):
                if board[r][column] == "":
                    possible_moves.append(self.get_board_string_position(r,column))
            return possible_moves
        else:
            for r in range(row-1,row-3,-1):
                if board[r][column] == "":
                    possible_moves.append(self.get_board_string_position(r+1,column))
            return possible_moves
    
    def move_to(self, from_position=None, to_position=None,board=None):
        possible_positions = self.possible_moves(from_position,board)
        
        current_row, current_column = self.get_board_coordinates(from_position)
        new_row, new_column = self.get_board_coordinates(to_position)

        if (to_position in possible_positions) and (board[new_row][new_column] == ""):
            # print("[Debug] Move Possible")
            pass
        else:
            print("Move Not Possible")
            return False

        board[current_row][current_column] = ""
        board[new_row][new_column] = self

        return True