import csv 
import numpy as np
import prettytable as pt

class Table:

    def __init__(self):

        self.table = None       # table for output
        self.data = None        # init data

        self.rows = 0           # amount of rows
        self.columns = 0        # amount of columns

        self.polyPow = 0

    def readData(self, name: str):

        try:
            with open(name, "r") as file:
                points = list(csv.DictReader(file))
        except:
            raise FileNotFoundError("No valid file!") from None

        x = np.array([])
        y = np.array([])
        
        for point in points:
            try:
                x = np.append(x, float(point.get("x")))      
                y = np.append(y, float(point.get("y")))    
            except:
                raise ValueError("Wrong data in input file!") from None

        self.rows = x.size
        self.columns = 2

        self.data = np.zeros((self.rows, self.columns))

        self.data[:, 0] = x
        self.data[:, 1] = y

        self.data = self.data[self.data[:, 0].argsort(kind = "meregesort")]

    def makeConfiguration(self, xValue, polyPow):

        # if not (np.amin(self.data[:, 0]) <= xValue <= np.amax(self.data[:, 0])):
        #     raise ValueError("Extrapolation is forbidden!") from None
        
        self.polyPow = polyPow
        index = 0

        for i in range(1, self.rows):
            if self.data[i - 1, 0] <= xValue <= self.data[i, 0]: 
                index = i
                break

        i = 0
        beg, end = index, index

        while (i != polyPow):
            if beg != 0:
                beg -= 1
                i += 1

            if (i == polyPow):
                break

            if end != self.rows - 1:
                end += 1
                i += 1

        for i in range(beg):
            self.data = np.delete(self.data, 0, axis = 0)

        for i in range(end + 1, self.rows):
            self.data = np.delete(self.data, -1, axis = 0)

        self.rows = self.polyPow + 1

    @staticmethod
    def formatStr(value):
        return "{:.6f}".format(value)

    @staticmethod
    def printData(data, type = "init"):
        
        table = pt.PrettyTable()

        if type == "init":
            fieldNames = ["№", "X", "Y"]
        else:
            pass

        table.field_names = fieldNames

        for i in range(len(data)):
            table.add_row([str(i + 1)] + list(map(Table.formatStr, data[i])))

        print(table)
