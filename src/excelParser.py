"""Module for parsing Excel docs."""

# import xlwings as xw  # use to read specific columns? can it read all found?
import pandas as pd


class ExcelParser:
    """Parses .XLSX files for data to be used by the other classes."""

    # constructor. so object can just exist, then you insert values easily.
    def __init__(self):
        """Create ExcelParser object. Controlling the object is separate."""
        self.sheet = ""

    def pickFile(self, fileLocation):
        """Select an Excel file. May use Pandas or Excel, idrk as of yet."""
        # error checking?
        # self.sheet = xw.Book(fileLocation).sheets["Sheet1"]
        self.sheet = pd.read_excel(fileLocation)

    def requireColumns(self, c1, c2):
        """Another docstring."""
        pass

    def printFile(self):
        """Aight so this is an example docstring."""
        # r = self.sheet.range("A1:A25").value
        # c = self.sheet.range("F5").value
        print(self.sheet)


# anything y000 p00t here is more or less for testing this crap out
ep = ExcelParser()
ep.pickFile(r"..\data\For_aduquaas.xlsx")
ep.printFile()
