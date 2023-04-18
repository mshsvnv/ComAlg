import numpy as np
import random as r
import csv
import prettytable as pt
import matplotlib.pyplot as plt
import calcAlg as ca
class Table:

    def __init__(self):
        self.x = None           # array of x
        self.y = None           # array of y
        self.z = None           # array of z (for two dimensional approx)

        self.weight = None      # array of wights
        self.dimension = None   # dimension

        self.delta = None       # variance
        
    def readFromFile(self, name: str):

        with open(name, 'r') as file:
            points = list(csv.DictReader(file))

        self.dimension = 2 if len(points[0]) == 4 else 1

        data = np.empty((len(points), 2 + self.dimension))

        i = 0
        for point in points:
            data[i, 0] = np.float16(point.get('x'))
            data[i, 1] = np.float16(point.get('y'))

            if self.dimension == 2:
                data[i, 2] = np.float16(point.get('z'))
                data[i, 3] = np.float16(point.get('weight'))
            else:
                data[i, 2] = np.float16(point.get('weight'))
            i += 1
        
        data = data[data[:, 0].argsort(kind = "mergesort")]

        self.x = data[:, 0]
        self.y = data[:, 1]

        if self.dimension == 2:
            self.z = data[:, 2]
            self.weight = data[:, 3]
        else:
            self.weight = data[:, 2]

    def generateTable(self, func, amount: list, params: list):
        
        xStart = min(params[:2])
        xEnd = max(params[:2])

        self.dimension = 1 if len(params) == 2 else 2

        if self.dimension == 1:

            self.x = np.linspace(xStart, xEnd, amount[0])

            self.weight = np.random.uniform(low = 0, high = 0.5, size = amount[0])

            self.y = func(self.x) #* self.weight

        else:
            yStart = min(params[2:])
            yEnd = max(params[2:])

            x = np.linspace(xStart, xEnd, amount[0])
            y = np.linspace(yStart, yEnd, amount[1])

            self.weight = np.random.uniform(low = 0, high = 2, size = amount[0] * amount[1])

            Y, X = np.meshgrid(y, x)

            self.x = X.ravel()
            self.y = Y.ravel()
            self.z = func(self.x, self.y) #* self.weight

            self.writeToFile()
    
    def writeToFile(self):

        with open("../data/new.csv", mode = "w") as w_file:

            names = ["x", "y", "z", "weight"]

            file_writer = csv.DictWriter(w_file, delimiter = ",", 
                                        lineterminator="\r", fieldnames=names)
            
            file_writer.writeheader()

            dim = np.shape(self.x)[0]

            for i in range(dim):
                file_writer.writerow({"x": self.formatStr(self.x[i]), "y": self.formatStr(self.y[i]), "z": self.formatStr(self.z[i]), "weight": self.formatStr(self.weight[i])})

    def editWeight(self, opt, num = 1, weight = 1):
        
        if opt == 1:
            # if self.dimension == 1:
            #     self.y //= self.weight
            # else:
            #     self.z //= self.weight
            
            self.weight //= self.weight
        else:
            if self.dimension == 1:
                self.y[num - 1] //= self.weight[num - 1]
                self.y[num - 1] *= weight
            else:
                self.z[num - 1] //= self.weight[num - 1]
                self.z[num - 1] *= weight

            self.weight[num - 1] = weight

    def drawGraphics(self, *args):

        if self.dimension == 1:

            plt.grid(True)
            plt.xlabel("X-axis")
            plt.ylabel("Y-axis")

            plt.scatter(self.x, self.y, color = "blue", label = "Init data")

            x = np.linspace(self.x[0], self.x[-1], 100)
            
            for koefs in args:
                
                y = ca.getPolynomLine(x, koefs)
                print(koefs)

                color = (r.random(), r.random(), r.random())

                plt.plot(x, y, color = color, label = "{}-degree polynom".format(len(koefs) - 1))
            
            plt.legend()
            plt.show()
        else:
            ax = plt.axes(projection="3d")

            ax.set_xlabel("X-axis")
            ax.set_ylabel("Y-axis")
            ax.set_zlabel("Z-axis")

            ax.scatter3D(self.x, self.y, self.z, color = "blue")
            
            ax.legend(["Init data"])

            x, y = np.meshgrid(np.linspace(np.min(self.x), np.max(self.x), 100), 
                               np.linspace(np.min(self.y), np.max(self.y), 100))
           
            koefs = args[0]

            print(koefs)
            z = ca.getPolynomSurface(x, y, koefs)
            
            ax.plot_surface(x, y, z, cmap = "viridis")

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

        if self.dimension == 1:
            dim = np.shape(self.x)[0]

            for i in range(dim):

                data = [str(i + 1), Table.formatStr(self.x[i]), 
                                    Table.formatStr(self.y[i]),
                                    Table.formatStr(self.weight[i])]

                table.add_row(data)
        else:
            dim = np.shape(self.x)[0]
            
            for i in range(dim):
                data = [str(i + 1), Table.formatStr(self.x[i]), 
                                    Table.formatStr(self.y[i]),
                                    Table.formatStr(self.z[i]),
                                    Table.formatStr(self.weight[i])]

                table.add_row(data)

        print(table)



