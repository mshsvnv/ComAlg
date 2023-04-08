from Table import Table
import calcAlg as ca

fileNameOne = "../data/dataOne.csv"
fileNameTwo = "../data/dataTwo.csv"

def inputTableData(dim: int):

    amountX = int(input("\nAmount of nodes: "))
    xStart = int(input("Start X: "))
    xEnd = int(input("End X: "))

    if dim == 1:
        return [amountX], xStart, xEnd
    else:
        amountY = int(input("\nAmount of nodes: "))
        yStart = int(input("Start Y: "))
        yEnd = int(input("End Y: "))

        return [amountX, amountY], xStart, xEnd, yStart, yEnd

def inputPolyPow():
    power = int(input("\nPolynom power: "))

    return power

def changeWeights(myTable: Table):

    msg = "\n1. All ones\n" \
          "2. By number\n"
    
    print(msg)

    opt = int(input("Enter option: "))
    if opt == 1:
        myTable.weight //= myTable.weight
    else:
        num = int(input("Enter number: "))
        weight = float(input("Enter weight: "))

        myTable.weight[num - 1] = weight

oneDimTable = Table()
twoDimTable = Table()

opts = "\n# ONE dimensional approximation\n" \
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
        "\n# Solve ODE\n" \
        "11. Solve\n" \
        "\n0. Exit\n" \

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
            changeWeights(oneDimTable)
        elif opt == 5:
            power = inputPolyPow()
            koefs1 = ca.solveSystemOne(oneDimTable, 1)
            koefs2 = ca.solveSystemOne(oneDimTable, 2)
            koefsN = ca.solveSystemOne(oneDimTable, power)
            
            oneDimTable.drawGraphics(koefs1, koefs2, koefsN)
        elif opt == 6:
            amount, xStart, xEnd, yStart, yEnd = inputTableData(2)
            twoDimTable.generateTable(ca.funcB, amount, [xStart, xEnd, yStart, yEnd])
        elif opt == 7:
            twoDimTable.readFromFile(fileNameTwo)
        elif opt == 8:
            twoDimTable.printTable()
        elif opt == 9:
            changeWeights(twoDimTable)
        elif opt == 10:
            power = inputPolyPow()

            koefs = ca.solveSystemTwo(twoDimTable, power)
            twoDimTable.drawGraphics(koefs)
        elif opt == 11:
            ca.solveODE()

        menu()

menu()