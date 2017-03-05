#!/usr/bin/env python
""""""

tableData = [['apples', 'oranges', 'cherries', 'banana'],
                            ['Alice', 'Bob', 'Carol', 'David'],
                            ['dogs', 'cats', 'moose', 'goose']]

maxlenlist = []
for i in range(len(tableData)):
    maxlenlist.append(0)
    for item in tableData[i]:
        if len(item) > maxlenlist[i]:
            maxlenlist[i] = len(item)
print(maxlenlist)
for i in range(len(tableData[0])):
    for j in range(len(tableData)):
        print(tableData[j][i].rjust(maxlenlist[j]) + " ", end = "")
    print("")
