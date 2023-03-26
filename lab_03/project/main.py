from Table import Table
import calcAlg as ca

fileName = "data.txt"

myTable = Table()
# myTable.readFile(fileName)

xstart, xend, xpoints = -5, 5, 20
ystart, yend, ypoints = -3, 4, 50
zstart, zend, zpoints = -1, 2, 30

myTable.generateTable(xstart, xend, xpoints,
                      ystart, yend, ypoints,
                      zstart, zend, zpoints)

myTable.printInitTable()

myTable.inputData()

print("\nFunction value: {:.4f}".format(myTable.f(myTable.values[0], myTable.values[1], myTable.values[2])))
funcValue = ca.makeMultiDimInterpolationNewton(myTable)
print("Newton interpolation: {:.4f}".format(funcValue))

funcValue = ca.makeMultiDimInterpolationSpline(myTable)
print("Spline interpolation: {:.4f}".format(funcValue))

funcValue = ca.makeMultiDimInterpolationBoth(myTable)
print("Newton + Spline interpolation: {:.4f}".format(funcValue))

# for nz in range(1, int(myTable.powers[2] + 1)):

#     print("\nnz =", nz)
#     func1 = []
#     for ny in range(1, int(myTable.powers[0] + 1)):

#         func2 = []
#         for nx in range(1, int(myTable.powers[1] + 1)):

#             old = myTable.powers

#             myTable.powers = [nz, ny, nz]
#             func2.append(ca.makeMultiDimInterpolationNewton(myTable))

#             myTable.powers = old
#         func1.append(func2)

#     Table.printFinalTable(func1, myTable.powers)
