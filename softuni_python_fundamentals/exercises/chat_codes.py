messages_amount = int(input())
for messages in range(1, messages_amount + 1):
    code = int(input())
    if code == 88:
        print("Hello")
    elif code == 86:
        print("How are you?")
    elif code < 88 and code != 86:
        print("GREAT!")
    else:
        print("Bye.")
