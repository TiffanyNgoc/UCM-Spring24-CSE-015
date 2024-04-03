from logic import TruthTable
myTable = TruthTable(["p", "q"], ["p or q"])
myTable.display()

myTable = TruthTable(["p", "q"], ["p or q", "p and q"])
myTable.display()

myTable = TruthTable(["a"], ["-a"])
myTable.display()

myTable = TruthTable(["a", "b"], ["a and b"])
myTable.display()

myTable = TruthTable(["a", "b"], ["a or b"])
myTable.display()

myTable = TruthTable(["a", "b"], ["a -> b"])
myTable.display()

myTable = TruthTable(["a", "b"], ["a <-> b"])
myTable.display()


