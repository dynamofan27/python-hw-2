input_line = input("Input string: ")


def transformStr(str):
    if len(str) > 5:
        str = str[0:5] + "..."

    if str[0] == 'l' or str[0] == 'L':
        print(str.lower())
    elif str[0] == 'u' or str[0] == 'U':
        print(str.upper())
    else:
        print(str)

transformStr(input_line)
