# from Server.BaseServer import Server for subclasses
#import pandas as pd
#import openpyxl
import xlwings as xw

class ExcelParser:
    # constructor. so object can just exist, then you insert values easily.
    def __init__(self):
        self.sheet = ""

    def pickFile(self, fileLocation):
        # error checking?
        sheet = xw.Book(fileLocation).sheets["Sheet1"]

    def requireColumns(self, c1, c2):
        pass

    def printFile(self):
        r = sheet.range("A1:A25").value
        c = sheet.range("F5").value
        print(r)

# anything y000 p00t here is more or less for testing this crap out
ep = ExcelParser()
ep.pickFile(r"..\data\For_aduquaas.xlsx")
ep.printFile()

