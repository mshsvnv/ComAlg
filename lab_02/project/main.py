import calcAlg as ca
from Table import Table

splineTable = Table()
splineTable.readData("./data/data.csv")
Table.printData(splineTable.data, "init")

NeWtonTable = Table()
NeWtonTable.readData("./data/data.csv")
Table.printData(NeWtonTable.data, "init")