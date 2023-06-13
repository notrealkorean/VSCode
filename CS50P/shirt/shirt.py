from sys import argv, exit
from PIL import Image, ImageOps


if len(argv) > 3:
    exit("Too many command-line arguments")
elif len(argv) < 3:
    exit("Too few command-line arguments")

try:
    file_type = ["jpg", "jpeg", "png"]
    input = argv[1].split(".")[1].lower()
    output = argv[2].split(".")[1].lower()
    if not input in file_type or not output in file_type:
        exit("Invalid file type")
    elif input != output:
        exit("Input and output have different extensions")

except IndexError:
    exit("Invalid input")

try:
    image = Image.open(argv[1])
except FileNotFoundError:
    exit(argv[1] + "not found.")

shirt = Image.open("shirt.png")
size = shirt.size
muppet = ImageOps.fit(image, size)
muppet.paste(shirt, shirt)
muppet.save(argv[2])
