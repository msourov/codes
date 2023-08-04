def func(inp):
    if inp[:9] == '011181129' and inp[9:13] == 'MALE' and inp[13:17] == '2.74' and inp[17] == ' ':
        try:
            if isinstance(int(inp[18:21]), int) and inp[21] in ['@', '#'] and inp[22] == ' ' and inp[23:25].isupper() \
                    and inp[25:28].islower() and int(inp[28:]) in range(-10, 11):
                return True
        except ValueError:
            try:
                if isinstance(float(inp[18:22]), float) and inp[22] in ['@', '#'] and inp[23] == ' ' \
                        and inp[24:26].isupper() and inp[26:29].islower() and float(inp[29:]) in range(-10, 11):
                    return True

            except ValueError:
                return False
    else:
        print(False)


i = input('Enter the input: ')
print(func(i))
