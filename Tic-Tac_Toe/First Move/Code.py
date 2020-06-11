def board():
    print(f"""
    ---------
    | {ui[0]} {ui[1]} {ui[2]} |
    | {ui[3]} {ui[4]} {ui[5]} |
    | {ui[6]} {ui[7]} {ui[8]} |
    ---------""")


ui = list(input("Enter cells: "))
board()
count = 0
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
            ui[position] = 'X'
            board()
            quit()
        elif ui[position] in ['X', 'O']:
            print("This cell is occupied! Choose another one!")
