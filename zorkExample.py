exit = False
position = (0,0)
inventory = []
print("running....")
while not exit:
    command = input("command >> ")
    print(command)
    if command == "north":
        x, y = position
        position = (x, y+1)
    elif command == "south":
        x, y = position
        position = (x, y-1)
    elif command == "east":
        x, y = position
        position = (x+1, y)
    elif command == "west":
        x, y = position
        position = (x-1, y)
    elif command == "position":
        print(position)
    elif command == "collect":
        if position == (1,1):
            inventory.append("book")
            print("collected a book")
        else:
            print("nothing to collect")
    elif command == "invent":
        print(inventory)
    else:
        print("bad command")
    if position == (1,1):
        print("You see a book")
    if position == (1,2):
        print("You reached the north pole")
        exit = True
print("game over")
