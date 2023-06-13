from sys import argv, exit

if len(argv) > 2:
    exit("Too many command-line arguments")
elif len(argv) < 2:
    exit("Too few command-line arguments")
elif argv[1][-3:] != ".py":
    exit("Not a python file")


try:
    lines = 0
    with open(argv[1]) as file:
        for line in file:
            if line.strip() != "":
                if not line.strip().startswith("#"):
                    lines += 1

    print(lines)



except FileNotFoundError:
    exit("File does not exist")
