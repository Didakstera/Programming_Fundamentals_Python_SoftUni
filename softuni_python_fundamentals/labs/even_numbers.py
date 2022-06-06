amount_numbers = int(input())
for numbers in range(amount_numbers):
    new_number = int(input())
    if new_number % 2 != 0:
        print(f"{new_number} is odd!")
        break
else:
    print("All numbers are even.")
