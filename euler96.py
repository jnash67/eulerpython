import sudoku27


def chunks(l, n):
    """Yield successive num-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]


file = "p096_sudoku.txt"
# file = "sudoku1.txt"

sumOfNums = 0
count = 0
for chunk in chunks(list(open(file)), 10):
    gridstring = ''
    for l in range(0, 9):
        rowList = []
        row = chunk[l + 1].strip()
        row = row.replace("0", ".")
        gridstring = gridstring + row
    count += 1
    result = sudoku27.solve(gridstring)
    sudoku27.display(result)
    dig1 = int(result['A1'])
    dig2 = int(result['A2'])
    dig3 = int(result['A3'])
    num = dig1 * 100 + dig2 * 10 + dig3
    # num = result[0][0]*100+ result[0][1]*10+result[0][2]
    sumOfNums += int(num)
    print("Solved Sudoku {} which has top left num {}.  Running sum is {}".format(count, num, sumOfNums))
print("Sum of all the 3 digit numbers is {}".format(sumOfNums))
