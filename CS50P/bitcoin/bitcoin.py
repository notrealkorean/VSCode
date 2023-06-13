import json
import requests
from sys import argv, exit

if len(argv) < 2:
    exit("Missing command-line argument")
elif len(argv) > 2:
    exit("Too many command-line arguments")
else:
    try:
        b = float(argv[1])
        try:
            response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
            op = response.json()
            price = op["bpi"]["USD"]['rate_float']
            print(f"${(b * price):,.4f}")

        except requests.RequestException:
            exit("Error")

    except ValueError:
        exit("Command-line argument is not a number")

