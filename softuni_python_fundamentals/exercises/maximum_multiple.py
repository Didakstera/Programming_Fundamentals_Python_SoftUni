divisor = int(input())
boundary = int(input())
integer = boundary
while integer % divisor != 0:
    integer -= 1
print(f"{integer}")
