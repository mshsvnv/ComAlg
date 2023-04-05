import numpy as np
import random as r
import csv
import prettytable as pt

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

        for point in points:
            self.x = np.append(self.x, float(point.get('x')))
            self.y = np.append(self.y, float(point.get('y')))

            if self.dimension == 2:
                self.z = np.append(self.z, float(point.get('z')))
            
            self.weight = np.append(self.weight, float(point.get('weight')))
            
        self.amount = np.shape(self.x)[0]            

    def generateTable(self, func, xStart, xEnd, amount):

        step = (max(xStart, xEnd) - min(xStart, xEnd)) / amount

        self.x = np.linspace(xStart, xEnd, step)
        self.y = np.array((func(i) for i in self.x))
        self.weight = np.array((r.randint(1, 10) for i in range(amount)))

    def drawGraphics(self):
        pass

    @staticmethod
    def formatStr(value):
        return "{:.3f}".format(value)

    def printTable(self):

        table = pt.PrettyTable()

        fieldNames = ["№", "X", "Y"]

        # if self.dimension == 1:
        #     field

        fieldNames.append("Weight")

        table.field_names = fieldNames

        for i in range(self.amount):
            table.add_row([str(i + 1)] + 
                          [Table.formatStr(self.x[i]), 
                           Table.formatStr(self.y[i]),
                           Table.formatStr(self.weight[i])])
        
        print(table)



