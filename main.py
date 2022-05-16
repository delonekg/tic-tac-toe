from board import Board

def main():

    board = Board()

    while True:
        print(board.board_drawing)

        def place_x():
            x_input = input("Where would X like to place first? Type a coordinate. For example: A2, B3\n").lower()
            if not board.place("X", x_input):
                place_x()
            else:
                print(board.board_drawing)

        place_x()

        if board.check_for_winner("X"):
            break
        
        if board.check_for_winner("O"):
           break

        def place_o():
            o_input = input("Where would O like to place first? Type a coordinate. For example: A2, B3\n").lower()
            if not board.place("O", o_input):
                place_o()
            else:
                print(board.board_drawing)

        place_o()

        if board.check_for_winner("X"):
            break
        
        if board.check_for_winner("O"):
            break

if __name__ == "__main__":
    main()
