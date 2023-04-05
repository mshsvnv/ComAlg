fileName = "../data/data_one_dimensional.csv"

def inputTableData():
    xStart = int(input("Start X:"))
    xEnd = int(input("End X:"))
    n = int(input("Amount of nodes:"))

    return xStart, xEnd, n

def inputPolyPow():
    pow = int(input("Polynom power:"))

    return pow

def menu():

    pass
    # One dimensional approximation
    # 1. Generate table
    # 2. Read table from file
    # 3. Edit weights:
    # # 3.1 All ones
    # # 3.2 By number
    # 4. Make Graphics
    # 5. Print Table

    # Two dimensional approximation
    # same
