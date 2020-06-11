ui = str(input("Enter cells: "))
count = 0
x_count, o_count = 0, 0

print("---------")
for i in range(len(ui)):
    count += 1
    if count % 3 == 1:
        print("|", end=" ")
    print(ui[i], end=" ")
    if count % 3 == 0:
        print("|")
    if ui[i] == 'X':
        x_count += 1
    elif ui[i] == 'O':
        o_count += 1
print("---------")


def x_wins():
    if ui[0] == ui[1] and ui[0] == ui[2] and ui[0] == 'X':
        return True
    if ui[0] == ui[3] and ui[0] == ui[6] and ui[0] == 'X':
        return True
    if ui[0] == ui[4] and ui[0] == ui[8] and ui[0] == 'X':
        return True
    if ui[1] == ui[4] and ui[1] == ui[7] and ui[1] == 'X':
        return True
    if ui[2] == ui[5] and ui[2] == ui[8] and ui[2] == 'X':
        return True
    if ui[3] == ui[4] and ui[3] == ui[5] and ui[3] == 'X':
        return True
    if ui[6] == ui[7] and ui[6] == ui[8] and ui[6] == 'X':
        return True
    if ui[2] == ui[4] and ui[2] == ui[6] and ui[2] == 'X':
        return True


def o_wins():
    if ui[0] == ui[1] and ui[0] == ui[2] and ui[0] == 'O':
        return True
    if ui[0] == ui[3] and ui[0] == ui[6] and ui[0] == 'O':
        return True
    if ui[0] == ui[4] and ui[0] == ui[8] and ui[0] == 'O':
        return True
    if ui[1] == ui[4] and ui[1] == ui[7] and ui[1] == 'O':
        return True
    if ui[2] == ui[5] and ui[2] == ui[8] and ui[2] == 'O':
        return True
    if ui[3] == ui[4] and ui[3] == ui[5] and ui[3] == 'O':
        return True
    if ui[6] == ui[7] and ui[6] == ui[8] and ui[6] == 'O':
        return True
    if ui[2] == ui[4] and ui[2] == ui[6] and ui[2] == 'O':
        return True


def impossible_case():
    if x_wins() and o_wins():
        # print("1")
        return True
    if abs(x_count - o_count) > 1:
        # print("3")
        return True
    return False


if impossible_case():
    print("Impossible")
elif x_wins():
    print("X wins")
elif o_wins():
    print("O wins")
elif x_count + o_count == 9:
    print("Draw")
else:
    print("Game not finished")
