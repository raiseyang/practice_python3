tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]

colWidths = [0] * len(tableData)
for i,array in enumerate(tableData):
    colWidths[i] = 0
    for word in array:
        if len(word) >colWidths[i]:
            colWidths[i] = len(word)

for j in range(0,4):
    for i,array in enumerate(tableData):
        if i == 0:
            print(array[j].rjust(colWidths[i]),end=' ')
        else:
            print(array[j].ljust(colWidths[i]),end=' ')

    print("")

print(colWidths)