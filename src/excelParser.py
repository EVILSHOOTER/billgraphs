# from Server.BaseServer import Server for subclasses
import pandas as pd


class ExcelParser:
    # constructor. so object can just exist, then you insert values easily.
    def __init__(self):
        self.dataFrame = None

    
    def pickFile(self, fileLocation):
        # error checking?
        self.dataFrame = pd.read_excel(fileLocation)

    def printFile(self):
        print(self.dataFrame)

# anything y000 p00t here is more or less for testing this crap out
ep = ExcelParser()
#ep.pickFile("C:\Users\deck\Documents\Git\GitProjects\billgraphs\data\For_aduquaas.xlsx")
#ep.printFile()

