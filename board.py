from zoneinfo import available_timezones


class Board:

    def __init__(self):
        self.board_list = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.board_drawing = f"""
           {self.board_list[0][0]}   |   {self.board_list[0][1]}   |   { self.board_list[0][2]}
         - - - - - - - - - - -
           {self.board_list[1][0]}   |   {self.board_list[1][1]}   |   {self.board_list[1][2]}
         - - - - - - - - - - -
           {self.board_list[2][0]}   |   {self.board_list[2][1]}   |   {self.board_list[2][2]}
        """
        self.available_coordinates = ["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]

    def update_board(self):
        self.board_drawing = f"""
           {self.board_list[0][0]}   |   {self.board_list[0][1]}   |   { self.board_list[0][2]}
         - - - - - - - - - - -
           {self.board_list[1][0]}   |   {self.board_list[1][1]}   |   {self.board_list[1][2]}
         - - - - - - - - - - -
           {self.board_list[2][0]}   |   {self.board_list[2][1]}   |   {self.board_list[2][2]}
        """

    def place(self, letter, coordinate):
        if coordinate in self.available_coordinates:
            if coordinate[0] == "a":
                exact_coordinate = int(coordinate[1]) - 1
                self.board_list[0][exact_coordinate] = letter
                self.available_coordinates.remove(coordinate)
                self.update_board()
                return True
            elif coordinate[0] == "b":
                exact_coordinate = int(coordinate[1]) - 1
                self.board_list[1][exact_coordinate] = letter
                self.available_coordinates.remove(coordinate)
                self.update_board()
                return True
            elif coordinate[0] == "c":
                exact_coordinate = int(coordinate[1]) - 1
                self.board_list[2][exact_coordinate] = letter
                self.available_coordinates.remove(coordinate)
                self.update_board()
                return True
        else:
            print("Oops! That space is unavailable try again!")
            return False

    def check_for_winner(self, player):
        # Check Diagnonal Rows
        if self.board_list[0][0] == player and self.board_list[1][1] == player and self.board_list[2][2] == player:
            print(f"Player {player} won!")
            return True

        if self.board_list[0][2] == player and self.board_list[1][1] == player and self.board_list[2][0] == player:
            print(f"Player {player} won!")
            return True

        # Check Horizontal Rows

        for row in self.board_list:
            horizontal_count = 0
            for letter in row:
                if letter == player:
                    horizontal_count += 1
            if horizontal_count == 3:
                print(f"Player {player} won!")
                return True

        # Check Verticals Rows
        if self.board_list[0][0] == player and self.board_list[1][0] == player and self.board_list[2][0] == player:
            print(f"Player {player} won!")
            return True

        if self.board_list[0][1] == player and self.board_list[1][1] == player and self.board_list[2][1] == player:
            print(f"Player {player} won!")
            return True

        if self.board_list[0][1] == player and self.board_list[1][1] == player and self.board_list[2][1] == player:
            print(f"Player {player} won!")
            return True

        if self.board_list[0][2] == player and self.board_list[1][2] == player and self.board_list[2][2] == player:
            print(f"Player {player} won!")
            return True

        # Check if tied
        if len(self.available_coordinates) == 0:
            print("You both tied!")
            return True