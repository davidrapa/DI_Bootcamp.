matrix = [["7", "i", "3"],
         ['T', 's', 'i'],
        ['h', '%', 'x'],
        ['i', '', '#'],
        ['s', 'M', ''],
        ['$', 'a', ''],
        ['#', 't', '%'],
        ['^', 'r', '!'],
          ]

final_sent = []
for column in range(len(matrix[0])):
    for row in range(len(matrix[0])):
        if matrix[row][column].isalpha():
            final_sent.append((matrix[row][column]))

print(''.join(final_sent))