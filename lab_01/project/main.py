import calcAlg as ca
from classTable import Table

def inputData():

    xValue = input("\nInput x: ")

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

if __name__ == "__main__":

    NewtonTable = Table("Newton")                       # прямая интерполяция
    HermitTable = Table("Hermit")

    NewtonTable.readData("data/data.csv")
    HermitTable.readData("data/data.csv")

    NewtonTable.printData("\nInit table: ")

    xValue, polyPow = inputData()

    NewtonTable.makeConfiguration(xValue, polyPow)
    ca.calculateDividedDiffNewton(NewtonTable)

    HermitTable.makeConfiguration(xValue, polyPow)
    HermitTable.duplicateConfiguration()
    ca.calculateDividedDiffHermit(HermitTable)

    NewtonTable.printData("\nNewton's method:")
    HermitTable.printData("\nHermit's method:")

    ca.getPolyValue(NewtonTable, xValue, True)
    ca.getPolyValue(HermitTable, xValue, True)

    NewtonTableReverse = Table("Newton")                # обратная интерполяция
    HermitTableReverse = Table("Hermit")

    NewtonTableReverse.readData("data/data.csv", "reverse")
    HermitTableReverse.readData("data/data.csv", "reverse")

    xValue = 0

    NewtonTableReverse.makeConfiguration(xValue, polyPow)
    ca.calculateDividedDiffNewton(NewtonTableReverse)

    HermitTableReverse.makeConfiguration(xValue, polyPow)
    HermitTableReverse.duplicateConfiguration()
    ca.calculateDividedDiffHermit(HermitTableReverse)

    NewtonTableReverse.printData("\nNewton's method:")
    HermitTableReverse.printData("\nHermit's method:")

    ca.getPolyValue(NewtonTableReverse, xValue, True, "reverse")
    ca.getPolyValue(HermitTableReverse, xValue, True, "reverse")

    tableFirst = Table("Tabel_1")                       # решение СЛАУ Ньютоном
    tableFirst.readData("data/data_1.csv")
    tableFirst.printData("\nx(y)")

    tableSecond = Table("Table_2")
    tableSecond.readData("data/data_2.csv")
    tableSecond.printData("\ny(x)")

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



