from tabulate import tabulate


data = {}
data.update({"Georgian Lari" :"GEL"})
data.update({"Bolivian Boliviano":"BOB"})
data.update({"South African Rand":"ZAR"})

headers = ['Name', 'Code']
print_data = data.items()
print(tabulate(print_data, headers=headers))