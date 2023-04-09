from prettytable import PrettyTable

table = PrettyTable()

# we can add data by using rows
table.field_names = ["Pokemon Name", "Type"]
table.add_row(["Pikachu", "Electric"])
table.add_row(["Squirtle", "Water"])
table.add_row(["Charmander", "Fire"])

# we can add data by using column
table.add_column("Power", ["10", "20", "30"])

table.align = "l"
print(table)
