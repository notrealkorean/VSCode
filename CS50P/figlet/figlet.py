from pyfiglet import Figlet
from random import choice
from sys import argv, exit

figlet = Figlet()
fontlist = figlet.getFonts()

if len(argv) == 1:
    text = input("Text: ")
    figlet.setFont(font = choice(fontlist))
    print(figlet.renderText(text))

elif len(argv) == 3 and (argv[1] == "-f" or argv[1] == "--font") and argv[2] in fontlist:
    text = input("Text: ")
    figlet.setFont(font = argv[2])
    print(figlet.renderText(text))

else:
    exit("Invalid usage")

