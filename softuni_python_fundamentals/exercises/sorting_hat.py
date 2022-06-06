name = ""
while name != "Welcome!":
    char_counter = 0
    name = input()
    if name == "Welcome!":
        print("Welcome to Hogwarts.")
    elif name == "Voldemort":
        print("You must not speak of that name!")
        break
    else:
        for char in range(len(name)):
            char_counter += 1
        if char_counter < 5:
            print(f"{name} goes to Gryffindor.")
        elif char_counter == 5:
            print(f"{name} goes to Slytherin.")
        elif char_counter == 6:
            print(f"{name} goes to Ravenclaw.")
        elif char_counter > 6:
            print(f"{name} goes to Hufflepuff.")
