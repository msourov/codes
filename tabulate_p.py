from tabulate import tabulate
tmp = ['a','b','c','d']
data = [["mavs", 99],
        ["suns", 91],
        ["spurs", 94],
        ["nets", 88]]
f = [[*data[i], tmp[i]] for i in range(4)]
print(f)
col_name = ["team", "points", "class"]
print(tabulate(f, headers=col_name, tablefmt="fancy_grid", showindex="always"))