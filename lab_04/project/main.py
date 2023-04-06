from Table import Table
import calcAlg as ca

fileNameOne = "../data/dataOne.csv"
fileNameTwo = "../data/dataTwo.csv"

def inputTableData(dim: int):
    amount = int(input("Amount of nodes:"))
    xStart = int(input("Start X:"))
    xEnd = int(input("End X:"))

    if dim == 1:
        return amount, xStart, xEnd
    else:
        yStart = int(input("Start Y:"))
        yEnd = int(input("End Y:"))

        return amount, xStart, xEnd, yStart, yEnd

def inputPolyPow():
    pow = int(input("Polynom power:"))

    return pow

oneDimTable = Table()
twoDimTable = Table()

opts = "# ONE dimensional approximation\n" \
        "1. Generate table\n" \
        "2. Read table from file\n" \
        "3. Print Table\n" \
        "4. Edit weights\n" \
        "5. Make graphics\n" \
        "\n# TWO dimensional approximation\n" \
        "6. Generate table\n" \
        "7. Read table from file\n" \
        "8. Print Table\n" \
        "9. Edit weights\n" \
        "10. Make graphics\n" \
        "0. Exit\n" \

def menu():
            
    print(opts)
            
    opt = int(input("Enter option: "))

    if opt == 0:
        return
    else:
        if opt == 1:
            amount, xStart, xEnd = inputTableData(1)
            oneDimTable.generateTable(ca.funcA, amount, [xStart, xEnd])
        elif opt == 2:
            oneDimTable.readFromFile(fileNameOne)
        elif opt == 3:
            oneDimTable.printTable()
        elif opt == 4:
            pass
        elif opt == 5:
            oneDimTable.drawGraphics()
        elif opt == 6:
            amount, xStart, xEnd, yStart, yEnd = inputTableData(2)
            twoDimTable.generateTable(ca.funcA, amount, [xStart, xEnd, yStart, yEnd])
        elif opt == 7:
            twoDimTable.readFromFile(fileNameTwo)
        elif opt == 8:
            twoDimTable.printTable()
        elif opt == 9:
            pass
        elif opt == 10:
            twoDimTable.drawGraphics()

        menu()

menu()