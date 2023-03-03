import calcAlg as ca
from classTable import Table

def inputData():

    xValue = input("\nInput X: ")

    try:
        xValue = float(xValue)
    except:
        raise ValueError("Wrong type of value!") from None
    
    return xValue

def directInterpolation():

    print("\nDirect interpolation:\n")

    dataAll = list()
    xValue = None
    len_n = 0

    for i in range(3):

        len_n = i + 1

        polyPow = i + 1
        NewtonTable = Table("Newton")                       
        HermitTable = Table("Hermit")

        NewtonTable.readData("data/data_new.csv")
        HermitTable.readData("data/data_new.csv")

        # if i + 1 == NewtonTable.rows:
        #     break

        if i == 0:
            NewtonTable.printTable("Initial Table")
            xValue =  inputData()

        NewtonTable.makeConfiguration(xValue, polyPow)
        ca.calculateDividedDiffNewton(NewtonTable)
        # NewtonTable.printTable()

        HermitTable.makeConfiguration(xValue, polyPow)
        HermitTable.duplicateConfiguration()
        ca.calculateDividedDiffHermit(HermitTable)
        # HermitTable.printTable()

        yValueNewton = ca.getPolyValue(NewtonTable, xValue)
        yValueHermit = ca.getPolyValue(HermitTable, xValue)

        dataAll.append([yValueNewton, yValueHermit])
    
    print("X: {:.3f}".format(xValue))
    len_n = int(len_n)
    Table.printData(dataAll, len_n)

def reverseInterpolation():

    print("\nReverse interpolation:\n")

    dataAll = list()
    xValue = 0
    len_n = 0

    for i in range(3):
        len_n = i + 1

        polyPow = i + 1
        NewtonTable = Table("Newton")                       
        HermitTable = Table("Hermit")

        NewtonTable.readData("data/data_new.csv", "reverse")
        HermitTable.readData("data/data_new.csv", "reverse")

        # if i + 1 == NewtonTable.rows:
        #     break

        NewtonTable.makeConfiguration(xValue, polyPow)
        ca.calculateDividedDiffNewton(NewtonTable)
        # NewtonTable.printTable()

        HermitTable.makeConfiguration(xValue, polyPow, "HermitR")
        HermitTable.duplicateConfiguration()
        ca.calculateDividedDiffHermit(HermitTable)
        # HermitTable.printTable()

        yValueNewton = ca.getPolyValue(NewtonTable, xValue)
        yValueHermit = ca.getPolyValue(HermitTable, xValue)

        dataAll.append([yValueNewton, yValueHermit] )
    
    print("Y: {:.3f}".format(xValue))
    len_n = int(len_n)
    Table.printData(dataAll, len_n, "reverse")

def solveSystem():

    print("\nSystem solution:\n")

    dataAll = list()
    len_n = 0

    for i in range(5):
        len_n = i

        polyPow = i + 1
        xValue = 0

        tableFirst = Table("Tabel_1")                      
        tableFirst.readData("data/data_1.csv")

        tableSecond = Table("Table_2")
        tableSecond.readData("data/data_2.csv")

        if i + 1 == tableFirst.rows:
            break

        tableFirst.makeConfiguration(tableFirst.data[tableFirst.rows // 2, 0], tableFirst.rows - 1)
        ca.calculateDividedDiffNewton(tableFirst)
        
        newY = tableFirst.makeNewTable(tableSecond)
        tableSecond.addDifferences(newY)

        # tableSecond.printData("\nNew Table")

        tableSecond.makeConfiguration(xValue, polyPow)
        ca.calculateDividedDiffNewton(tableSecond)

        # print("\nAnswer for System:")
        
        xValue = ca.getPolyValue(tableSecond, xValue)
        yValue = ca.getPolyValue(tableFirst, xValue)

        dataAll.append([xValue, yValue])

    len_n = int(len_n)
    Table.printData(dataAll, 5, "system")

if __name__ == "__main__":
    directInterpolation()

    reverseInterpolation()

    # solveSystem()