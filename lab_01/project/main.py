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

NewtonTable = Table("Newton")
HermitTable = Table("Hermit")

NewtonTable.readData("data.csv")

HermitTable.readData("data.csv")

NewtonTable.printData("\nInit table: ")

xValue, polyPow = inputData()

NewtonTable.makeConfiguration(xValue, polyPow)
ca.calculateDividedDiffNewton(NewtonTable)

HermitTable.makeConfiguration(xValue, polyPow)
HermitTable.duplicateConfiguration()

ca.calculateDividedDiffHermit(HermitTable)

NewtonTable.printData("\nNewton method:")
HermitTable.printData("\nHermit method:")

ca.getNewtonPoly(NewtonTable, xValue)
ca.getHermitPoly(HermitTable, xValue)

