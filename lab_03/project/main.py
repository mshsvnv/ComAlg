from Table import Table
import calcAlg as ca

fileName = "data.txt"

myTable = Table()
myTable.readFile(fileName)

myTable.inputData()

funcValue = ca.makeMultiDimInterpolationNewton(myTable)
print("Newton interpolation: {:.4f}".format())

funcValue = ca.makeMultiDimInterpolationSpline(myTable)
print("Spline interpolation: {:.4f}".format())
