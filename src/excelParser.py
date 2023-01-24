# import some classes?
# from Server.BaseServer import Server for subclasses

class ExcelParser:
    def __init__(self, daVar):
        self.var = daVar
        print("hello world")

    def func(self, param1):
        print("func been d0ne: " + self.var)

# anything y000 p00t here is more or less for testing this crap out
ep = ExcelParser("h0l4 m1 4m1g0")
ep.func("y0")
