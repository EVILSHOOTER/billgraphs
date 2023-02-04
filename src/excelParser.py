"""Module for parsing Excel docs."""

# import xlwings as xw  # use to read specific columns? can it read all found?
import pandas as pd
import numpy


class ExcelParser:
    """Parses .XLSX files for data to be used by the other classes."""

    # constructor. so object can just exist, then you insert values easily.
    def __init__(self):
        """Create ExcelParser object. Controlling the object is separate."""
        self.sheet = None  # the OG table without edits
        self.table = None  # this shall be the updated table for drawing from

    def pickFile(self, fileLocation):
        """Select an Excel file. May use Pandas or Excel, idrk as of yet."""
        self.sheet = pd.read_excel(fileLocation)

    def printFile(self):
        """Print the entire doc. usually useless."""
        print(self.sheet)  # whole sheet

    def printTable(self):
        """Print the entire table. Mostly for testing purposes."""
        print(self.table)  # whole sheet

    def row(self, row=None, column=None):
        """Read a row, optionally choose the specific column too."""
        result = self.sheet.iloc[row]  # i-locate
        if column is not None:
            if isinstance(column, str):
                result = result.loc[column]  # by key
            elif isinstance(column, int):
                result = result.iloc[column]  # by number
        return result

    def rowLength(self):
        """Return no. of columns of table (headers excluded)."""
        return self.sheet.index.stop

    def columnLength(self):
        """Return no. of columns in table."""
        return len(self.sheet.columns)

    def test(self):
        """Test."""
        print(type(self.row(1, 4)))

    def convertTable(self):
        """Convert table into a more usable form for graphs."""
        self.table = self.sheet  # and then we edit this

        (self.sheet - pd.Timestamp("1970-01-01")) // pd.Timedelta("1s")
        
        for index, row in self.table.iterrows():
            for colIndex, column in enumerate(row):  # enumarate gives da index too
                if isinstance(column, pd._libs.tslibs.timestamps.Timestamp):
                    print("timestamp")
                #print(colIndex)
            print(row[1])  # can use key or number to index columns


# anything y000 p00t here is more or less for testing this crap out
ep = ExcelParser()
ep.pickFile(r"..\data\For_aduquaas.xlsx")
# ep.row(0, "Date of Birthe")
print(ep.convertTable())


# program aint gon catch all the errors but who cares
# thinking of making the errors caught overall and printed in a log
# have user tell me wtf is up so I can fix, and the program continues to work
