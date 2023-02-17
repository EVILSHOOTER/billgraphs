"""Main script for running all of the files."""

from excelParser import ExcelParser
from graphRenderer import GraphRenderer

graph = GraphRenderer()
excel = ExcelParser()

excel.pickFile(r"data\For_aduquaas.xlsx")
excel.convertTable()
excel.printNEWtable()
