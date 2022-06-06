command = ""
while command != "End":
    command = input()
    if command == "SoftUni" or command == "End":
        continue
    else:
        for char in range(len(command)):
            print(command[char] * 2, end="")
    print("")
