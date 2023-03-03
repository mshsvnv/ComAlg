import csv 
import numpy as np
import prettytable as pt
import calcAlg as ca
class Table:

    def __init__(self, method: str):

        self.method = method

        self.table = None       # table for output
        self.data = None        # init data

        self.rows = 0           # amount of rows
        self.columns = 0        # amount of columns

        self.polyPow = 0

    def readData(self, name: str, type = "direct"):

        try:
            with open(name, "r") as file:
                points = list(csv.DictReader(file))
        except:
            raise FileNotFoundError("No valid file!") from None

        x = np.array([])
        y = np.array([])
        yDer = np.array([])
        
        for point in points:
            try:
                x = np.append(x, float(point.get("x")))      
                y = np.append(y, float(point.get("y"))) 

                if len(point) == 3:     
                    yDer = np.append(yDer, float(point.get("yDer")))       
            except:
                raise ValueError("Wrong data in input file!") from None

        self.rows = x.size
        self.columns = 3

        self.data = np.zeros((self.rows, self.columns))
        self.dataReverse = np.zeros((self.rows, self.columns))

        if type == "direct":
            self.data[:, 0] = x
            self.data[:, 1] = y

            if len(yDer) != 0:
                self.data[:, 2] = yDer

            # self.data = self.data[self.data[:, 0].argsort(kind = "meregesort")]
        else:
            self.data[:, 1] = x
            self.data[:, 0] = y

            if len(yDer) != 0:
                for i in range(self.rows):
                    if yDer[i] != 0:
                        self.data[i, 2] = 1 / yDer[i]
                    else:
                        self.data[i, 2] = 1 / (10 ** 8)

        self.data = self.data[self.data[:, 0].argsort(kind = "meregesort")]

    def getDifferences(self):
        
        diff = list()

        for i in range(1, self.rows):
            diff.append(self.data[i - 1, 1] - self.data[i, 1])

        for i in range(1, len(diff)):
            if diff[i] * diff[i - 1] < 0:
                return i

        return 0

    def makeConfiguration(self, xValue, polyPow, method = "Newton"):

        if not (np.amin(self.data[:, 0]) <= xValue <= np.amax(self.data[:, 0])):
            raise ValueError("Extrapolation is forbidden!") from None
        
        # self.data = np.delete(self.data, 0, axis = 0)
        # self.rows -= 1

        self.polyPow = polyPow
        index = 0

        for i in range(1, self.rows):
            if self.data[i - 1, 0] <= xValue <= self.data[i, 0]: 
                index = i
                break

        i = 0
        beg, end = index, index

        point = self.getDifferences()
        print(point)

        # TODO сделать массив разностей, получить индексы монотонности, найти наиболее подходящий отрезок
            
        while (i != polyPow):
        
            if point <= self.rows // 2:
                if beg != point:
                    i += 1
                    beg -= 1

                if (i == polyPow):
                    break
                
                if end != self.rows - 1:
                    end += 1
                    i += 1
            else:
                if beg != 0:
                    i += 1
                    beg -= 1

                if (i == polyPow):
                    break
                
                if end != point:
                    end += 1
                    i += 1

        for i in range(beg):
            self.data = np.delete(self.data, 0, axis = 0)

        for i in range(end + 1, self.rows):
            self.data = np.delete(self.data, -1, axis = 0)

        print(self.data)

        self.rows = self.polyPow + 1

    def duplicateConfiguration(self):

        for i in range(0, self.rows * 2, 2):
            self.data = np.insert(self.data, i + 1, self.data[i], 0)

        self.rows *= 2

    def makeNewTable(self, table):

        newY = []

        for i in range(self.rows):
            newY.append(ca.getPolyValue(self, table.data[i, 0]))

        return newY


    def addDifferences(self, column):

        for i in range(self.rows):
            self.data[i, 1] -= column[i]

            temp = self.data[i, 1]
            self.data[i, 1] = self.data[i, 0]
            self.data[i, 0] = temp

    @staticmethod
    def formatStr(value):
        return "{:.6f}".format(value)

    @staticmethod
    def printData(data, len_n = int, type = "direct"):
        
        table = pt.PrettyTable()

        if type == "system":
            fieldNames = ["Polynom power", "X", "Y"]
        else:
            fieldNames = ["Polynom power", "Newton", "Hermit"]

        table.field_names = fieldNames

        for i in range(len_n):
            table.add_row([str(i + 1)] + list(map(Table.formatStr, data[i])))

        print(table)

    def printTable(self, method = "kek"):

        self.table = pt.PrettyTable()

        filedNames = ["№"]
        for i in range(self.columns):
            if i == 0:
                filedNames.append("X")
            elif i == 1:
                filedNames.append("Y")
            else:
                filedNames.append("Y" + '\'' * (i - 1))

        self.table.field_names = filedNames

        for i in range(self.rows):
            self.table.add_row([str(i + 1)] + list(map(Table.formatStr, self.data[i])))

        print(method)
        print(self.table)
