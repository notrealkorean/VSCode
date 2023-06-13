from sys import argv, exit
from tabulate import tabulate
import csv

if len(argv) > 2:
    exit("Too many command-line arguments")
elif len(argv) < 2:
    exit("Too few command-line arguments")
elif argv[1][-4:] != ".csv":
    exit("Not a csv file")

try:
    menu = []
    with open(argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            menu.append(row)
        print(tabulate(menu, headers="keys", tablefmt="grid"))


except FileNotFoundError:
    exit("File does not exist")

