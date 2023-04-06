import numpy as np
import random as r
import csv
import prettytable as pt
import matplotlib.pyplot as plt
class Table:

    def __init__(self):
        self.x = None           # array of x
        self.y = None           # array of y
        self.z = None           # array of z (for two dimensional approx)

        self.weight = None      # array of wights
        self.dimension = None   # dimension

        self.amount = None      # amount of points
        
    def readFromFile(self, name: str):

        with open(name, 'r') as file:
            points = list(csv.DictReader(file))

        self.dimension = 2 if len(points[0]) == 4 else 1
        data = np.empty((len(points), 2 + self.dimension))

        self.amount = len(points)

        i = 0
        for point in points:
            data[i, 0] = float(point.get('x'))
            data[i, 1] = float(point.get('y'))

            if self.dimension == 2:
                data[i, 2] = float(point.get('z'))
                data[i, 3] = float(point.get('weight'))
            else:
                data[i, 2] = float(point.get('weight'))
            i += 1
        
        data = data[data[:, 0].argsort(kind = "mergesort")]

        self.x = data[:, 0]
        self.y = data[:, 1]

        if self.dimension == 2:
            self.z = data[:, 2]
            self.weight = data[:, 3]
        else:
            self.weight = data[:, 2]

    def generateTable(self, func, amount, params: list):
        
        xStart = min(params[:2])
        xEnd = max(params[:2])

        self.dimension = 1 if len(params) == 2 else 2

        self.x = np.linspace(xStart, xEnd, amount)

        if self.dimension == 1:
            self.y = np.array([func(x) for x in self.x])
            self.y += np.random.normal(scale = 0.1, size = amount)
            
            self.weight = np.array([1 / abs(self.y[i] - func(self.x[i])) for i in range(amount)])
        else:
            yStart = min(params[2:])
            yEnd = max(params[2:])

            self.y = np.linspace(yStart, yEnd, amount)

            self.z = np.array([func(self.x[i], self.y[i]) for i in range(amount)])
            self.z += np.random.normal(scale = 0.1, size = amount)

            self.weight = np.array([1 / abs(self.z[i] - func(self.x[i], self.y[i])) for i in range(amount)])
        
        self.amount = amount

    def drawGraphics(self):
        
        if self.dimension == 1:
            plt.grid(True)
            plt.xlabel("X-axis")
            plt.ylabel("Y-axis")

            plt.scatter(self.x, self.y, color = "blue")
            plt.legend(["Init data"])

            plt.show()
        else:
            ax = plt.axes(projection="3d")

            ax.set_xlabel("X-axis")
            ax.set_ylabel("Y-axis")
            ax.set_zlabel("Z-axis")

            ax.scatter3D(self.x, self.y, self.z, color = "blue")
            ax.legend(["Init data"])

            plt.show()

    @staticmethod
    def formatStr(value):
        return "{:.3f}".format(value)

    def printTable(self):

        table = pt.PrettyTable()

        fieldNames = ["№", "X", "Y"]

        if self.dimension == 2:
            fieldNames.append("Z")

        fieldNames.append("Weight")

        table.field_names = fieldNames

        for i in range(self.amount):
            data = [str(i + 1)] + [Table.formatStr(self.x[i]), 
                           Table.formatStr(self.y[i])]
            
            if self.dimension == 2:
                data += [Table.formatStr(self.z[i])]

            data += [Table.formatStr(self.weight[i])]

            table.add_row(data)
        
        print(table)



