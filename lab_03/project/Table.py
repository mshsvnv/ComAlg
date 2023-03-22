import numpy as np
import prettytable as pt
from matplotlib import pyplot as plt

class Table:

    def __init__(self):
        self.x = None
        self.y = np.array([])
        self.z = np.array([])

        self.func = np.array([])

        self.powers = np.array([])
        self.values = np.array([])


    def readFile(self, fileName):
        with open(fileName, 'r') as file:

            curFunc = []

            for line in file.readlines():

                line = line.split()

                if line[0] == 'z':

                    if len(curFunc):
                        self.func = np.append(self.func, np.array(curFunc))

                    self.z = np.append(self.z, float(line[-1]))

                    curFunc = []
                elif line[0] == 'y\\x':
                    if self.x is None:
                        self.x = np.array(list(map(float, line[1::1])))
                else:
                    if self.y.shape[0] != self.x.shape[0]:
                        self.y = np.append(self.y, float(line[0]))

                    curFunc.append(list(map(float, line[1::1])))

        self.func = np.append(self.func, np.array(curFunc))
        self.func = self.func.reshape(self.z.shape[0],
                                      self.y.shape[0],
                                      self.x.shape[0]) 

    def inputData(self):

        var = ['x', 'y', 'z']
        print('\n')

        for i in range(3):

            try:
                value = float(input("Input {} value: ".format(var[i])))
            except:
                raise ValueError("Incorrect data!") from None
            
            if not (np.min(self.x) <= value <= np.max(self.x)):
                raise TypeError("Extrapolation is forbidden!") from None
            
            self.values = np.append(self.values, value)

        for i in range(3):

            try:
                power = int(input("Input n{} power: ".format(var[i])))
            except:
                raise ValueError("Incorrect data!") from None
            
            if not(0 <= power <= self.x.shape[0] - 1):
                raise TypeError("Incorrect power!") from None
            
            self.powers = np.append(self.powers, power)

    @staticmethod
    def getFormat(num):
        return "{:.1f}".format(num)
    
    def printInitTable(self):
        rows = self.y.shape[0]
        columns = self.x.shape[0]
        zAmount = self.z.shape[0]

        field_names = ["Y\X"]

        for i in range(columns):
            field_names.append(str(self.getFormat(self.x[i])))

        for i in range(zAmount):
            
            print("\nz =", self.getFormat(self.z[i]))
            
            table = pt.PrettyTable()
            table.field_names = field_names

            for j in range(rows):
                table.add_row([str(self.y[j])] + list(map(self.getFormat, self.func[i][j])))

            print(table)

    @staticmethod
    def printFinalTable(values, powers):
        table = pt.PrettyTable()

        field_names = ["ny\\nx"]

        for i in range(int(powers[1])):
            field_names.append(str(i + 1))

        table.field_names = field_names

        for i in range(len(values)):
            row = [i + 1] + list(map(Table.getFormat, values[i]))
            table.add_row(row)

        print(table)





        
