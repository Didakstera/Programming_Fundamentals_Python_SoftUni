strings_amount = int(input())
for inputs in range(strings_amount):
    string_check = input()
    if "," in string_check or "." in string_check or "_" in string_check:
        print(f"{string_check} is not pure!")
    else:
        print(f"{string_check} is pure.")
