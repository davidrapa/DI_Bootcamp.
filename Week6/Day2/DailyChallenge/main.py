
ask_str = input('I need a string. The string must be 10 characters long.')

if len(ask_str) <= 9:
    print ('string not long enough')
elif len(ask_str) >= 11:
    print ('string too long')
else:
    print("First character:", ask_str[0])
    print("Last character:", ask_str[-1])

    for i in range(len(ask_str)):
        print(ask_str[:i + 1])

