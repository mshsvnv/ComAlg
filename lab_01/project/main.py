import calcAlg as ca
from classTable import Table

def inputData(xText: str):

    xValue = input("\nInput {}: ".format(xText))

    try:
        xValue = float(xValue)
    except:
        raise ValueError("Wrong type of value!") from None

    polyPow = input("\nInput polynom's power: ")

    try:
        polyPow = int(polyPow)
    except:
        raise ValueError("Wrong type of power!") from None
 
    return xValue, polyPow

def printMenu():

    actions = ["1. Direct interpolation",
               "2. Reverse interpolation",
               "3. Solve SOLE",
               "4. Exit"]
    
    print("\n\t::Menu::\n")

    for act in actions:
        print(act)
    
    act = input("\nAct: ")

    try:
        act = int(act)
    except:
        ValueError("Wrong value for act!")

    if not (1 <= act <= 4):
        ValueError("Wrong value for act!")

    return act

def directInterpolation():
    NewtonTable = Table("Newton")                       # прямая интерполяция
    HermitTable = Table("Hermit")

    NewtonTable.readData("data/data.csv")
    HermitTable.readData("data/data.csv")

    NewtonTable.printData("\nInit table: ")

    xValue, polyPow = inputData("X")

    NewtonTable.makeConfiguration(xValue, polyPow)
    ca.calculateDividedDiffNewton(NewtonTable)

    HermitTable.makeConfiguration(xValue, polyPow)
    HermitTable.duplicateConfiguration()
    ca.calculateDividedDiffHermit(HermitTable)

    NewtonTable.printData("\nNewton's method:")
    HermitTable.printData("\nHermit's method:")

    ca.getPolyValue(NewtonTable, xValue, True)
    ca.getPolyValue(HermitTable, xValue, True)

def reverseInterpolation():

    NewtonTableReverse = Table("Newton")                # обратная интерполяция
    HermitTableReverse = Table("Hermit")

    NewtonTableReverse.readData("data/data.csv", "reverse")
    HermitTableReverse.readData("data/data.csv", "reverse")

    xValue, polyPow = inputData("Y")

    NewtonTableReverse.makeConfiguration(xValue, polyPow)
    ca.calculateDividedDiffNewton(NewtonTableReverse)

    HermitTableReverse.makeConfiguration(xValue, polyPow)
    HermitTableReverse.duplicateConfiguration()
    ca.calculateDividedDiffHermit(HermitTableReverse)

    NewtonTableReverse.printData("\nNewton's method:")
    HermitTableReverse.printData("\nHermit's method:")

    ca.getPolyValue(NewtonTableReverse, xValue, True, "reverse")
    ca.getPolyValue(HermitTableReverse, xValue, True, "reverse")

def  solveSOLE():
    tableFirst = Table("Tabel_1")                       # решение СЛАУ Ньютоном
    tableFirst.readData("data/data_1.csv")
    tableFirst.printData("\nx(y)")

    tableSecond = Table("Table_2")
    tableSecond.readData("data/data_2.csv")
    tableSecond.printData("\ny(x)")
    
    xValue, polyPow = inputData("Y")

    tableFirst.makeConfiguration(tableFirst.data[tableFirst.rows // 2, 0], tableFirst.rows - 1)
    ca.calculateDividedDiffNewton(tableFirst)
    
    newY = tableFirst.makeNewTable(tableSecond)
    tableSecond.addDifferences(newY)

    tableSecond.printData("\nNew Table")

    tableSecond.makeConfiguration(xValue, polyPow)
    ca.calculateDividedDiffNewton(tableSecond)

    print("\nAnswer for SOLE:")
    
    xValue = ca.getPolyValue(tableSecond, xValue, True, "reverse")
    ca.getPolyValue(tableFirst, xValue, True)

if __name__ == "__main__":

    while True:
        act = printMenu()

        if act == 1:
            directInterpolation()
        elif act == 2:
            reverseInterpolation()
        elif act == 3:
            solveSOLE()
        else:
            break