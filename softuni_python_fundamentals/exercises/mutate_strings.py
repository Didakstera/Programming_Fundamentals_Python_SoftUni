string_one = input()
string_two = input()
last_string = string_one
for char in range(len(string_two)):
        left = string_two[:char + 1]
        right = string_one[char + 1:]
        current = left + right
        if current == last_string:
            continue
        print(current)
        last_string = current
