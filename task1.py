input_number = input("Please, enter a number: ")


def oddOrEven(num):
    if not num.isdigit():
        exit("Please use Integer numbers")
    if int(num) % 2 == 0:
        print(f"Число {num} є парним")
    else:
        print(f"Число {num} є непарним")


oddOrEven(input_number)
