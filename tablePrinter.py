tableData = [['apples', 'oranges', 'cherries', 'banana'],
			 ['Alice', 'Bob', 'Carol', 'David',],
			 ['dogs', 'cats', 'moose', 'goose']]

def printTable(tableData):
	colWidths = [0] * len(tableData)
	for k in range (len(tableData)):
		for j in range (len(tableData[0])):
			if colWidths[k] < len(tableData[k][j]):
				colWidths[k] = len(tableData[k][j])
	print(colWidths)

for u in range (len(tableData[0])):
	for v in range(len(tableData)):
		print(tableData[u][v].rjust(colWidths[u] + 1), end='')
		print()

print(tableData)