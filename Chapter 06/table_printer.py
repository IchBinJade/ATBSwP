"""
Write a function named printTable() that takes a list of lists of strings
and displays it in a well-organized table with each column right-justified.
Assume that all the inner lists will contain the same number of strings.
"""


def print_table(table):
    row_len = len(table[0])
    col_len = len(table)
    for col in range(row_len):
        for row in range(col_len):
            width = len(max(tuple(table[row]), key=len))
            print(table[row][col].rjust(width), end=' ')
        print()


table_data = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

print_table(table_data)
