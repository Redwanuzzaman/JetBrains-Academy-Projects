ui = str(input("Enter cells: "))
print("---------")
count = 0
for i in range(len(ui)):
    count += 1
    if count % 3 == 1:
        print("|", end=" ")
    print(ui[i], end=" ")
    if count % 3 == 0:
        print("|")

print("---------")
