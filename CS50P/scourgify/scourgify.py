from sys import argv, exit
import csv

if len(argv) > 3:
    exit("Too many command-line arguments")
elif len(argv) < 3:
    exit("Too few command-line arguments")
elif argv[1][-4:] != ".csv":
    exit("Not a csv file")

try:
    list = []
    flh = []

    with open(argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            list.append(row)

    for row in list:
        person = []
        person.append(row["name"].split(", ")[0])
        person.append(row["name"].split(", ")[1])
        person.append(row["house"])
        flh.append(person)


    with open(argv[2], "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for row in flh:
            writer.writerow({"first": row[1], "last": row[0], "house": row[2]})



except FileNotFoundError:
    exit("Could not read " + argv[1])

