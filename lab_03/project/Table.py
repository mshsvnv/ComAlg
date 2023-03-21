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

        for i in range(3):

            try:
                value = float(input("Input {} value: ".format(var[i])))
                power = int(input("Input n{} power: ".format(var[i])))
            except:
                raise ValueError("Incorrect data!") from None
            
            self.powers = np.append(self.powers, power)
            self.values = np.append(self.values, value)

    def printTable(self):
        pass