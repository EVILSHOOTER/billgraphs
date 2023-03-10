"""Module for parsing Excel docs."""

# import xlwings as xw  # use to read specific columns? can it read all found?
import pandas as pd
from datetime import date


class ExcelParser:
    """Parses .XLSX files for data to be used by the other classes."""
    
    def __init__(self):
        """Create ExcelParser object. Controlling the object is separate."""
        self.OGtable = None  # the OG table without edits
        self.NEWtable = None  # this shall be the updated table for drawing

    def pickFile(self, fileLocation):
        """Select an Excel file. May use Pandas or Excel, idrk as of yet."""
        self.OGtable = pd.read_excel(fileLocation)

    def printOGtable(self):
        """Print the entire doc. usually useless."""
        print(self.OGtable)  # whole sheet

    def printNEWtable(self):
        """Print the entire table. Mostly for testing purposes."""
        print(self.NEWtable)  # whole sheet

    def row(self, row=None, column=None):
        """Read a row, optionally choose the specific column too."""
        result = self.NEWtable.iloc[row]  # i-locate
        if column is not None:
            if isinstance(column, str):
                result = result.loc[column]  # by key
            elif isinstance(column, int):
                result = result.iloc[column]  # by number
        return result

    def rowLength(self):
        """Return no. of columns of table (headers excluded)."""
        return self.OGtable.index.stop

    def columnLength(self):
        """Return no. of columns in table."""
        return len(self.OGtable.columns)

    def test(self):
        """Test."""
        print(type(self.row(1, 4)))

    def convertTable(self):
        """Convert table into a more usable form for graphs."""
        self.NEWtable = self.OGtable
        for columnName in self.NEWtable:
            column = self.NEWtable[columnName]
            # print(columnName + ": " + str(column.dtype))
            if str(column.dtype) == "datetime64[ns]":  # birthdate conversion
                d = date(1900, 1, 1)  # anchor date. nice to get Y-axis from.
                self.NEWtable[columnName] = self.NEWtable[columnName].apply(
                    lambda x: (x.date()-d).days)  # days since 1900


# anything y000 p00t here is more or less for testing this crap out
ep = ExcelParser()
ep.pickFile(r"..\data\For_aduquaas.xlsx")
# ep.row(0, "Date of Birthe")
ep.convertTable()
ep.printNEWtable()


# program aint gon catch all the errors but who cares
# thinking of making the errors caught overall and printed in a log
# have user tell me wtf is up so I can fix, and the program continues to work
