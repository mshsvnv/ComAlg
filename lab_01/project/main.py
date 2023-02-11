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

initTable = Table()

initTable.readData("data.csv")
initTable.printData("\nInit table: ")

xValue, polyPow = inputData()

initTable.makeConfiguration(xValue, polyPow)
initTable.duplicateConfiguration()

# ca.calculateDividedDiffNewton(initTable)
# print(ca.getNewtonPoly(initTable, xValue))

ca.calculateDividedDiffHermit(initTable)

initTable.printData("\nNewton method:")

# TODO: доделать main и графики