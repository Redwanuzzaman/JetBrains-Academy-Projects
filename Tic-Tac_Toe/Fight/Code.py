def board():
    print(f"""
    ---------
    | {ui[0]} {ui[1]} {ui[2]} |
    | {ui[3]} {ui[4]} {ui[5]} |
    | {ui[6]} {ui[7]} {ui[8]} |
    ---------""")


def win_status(pattern):
    if ui[0] + ui[1] + ui[2] == pattern \
            or ui[2] + ui[5] + ui[8] == pattern \
            or ui[8] + ui[7] + ui[6] == pattern \
            or ui[6] + ui[3] + ui[0] == pattern \
            or ui[3] + ui[4] + ui[5] == pattern \
            or ui[1] + ui[4] + ui[7] == pattern \
            or ui[0] + ui[4] + ui[8] == pattern \
            or ui[2] + ui[4] + ui[6] == pattern:
        return True


ui = list("_" for i in range(9))
board()
turn = 0
x_count, o_count = 0, 0

while True:
    coordinate = input("Enter the coordinates: ").split(" ")

    if not coordinate[0].isdigit():
        print("You should enter numbers!")
    else:
        position = 8 + int(coordinate[0]) - 3 * int(coordinate[1])
        if position < 0 or position > 8:
            print("Coordinates should be from 1 to 3!")
        elif ui[position] == '_':
            if turn % 2 == 0:
                ui[position] = 'X'
                board()
            else:
                ui[position] = 'O'
                board()
            turn += 1
        elif ui[position] in ['X', 'O']:
            print("This cell is occupied! Choose another one!")
    if win_status("XXX"):
        print("X wins")
        quit()
    elif win_status("OOO"):
        print("O wins")
        quit()
    elif turn == 9:
        print("Draw")
        quit()
