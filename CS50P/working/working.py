import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if time := re.search("^([1-9][0-2]?):?([0-5][0-9])? (AM|PM) to ([1-9][0-2]?):?([0-5][0-9])? (AM|PM)$", s):
        if time.group(3) == "PM":
            h1 = int(time.group(1)) + 12
            if h1 == 24:
                h1 = 12
        else:
            h1 = int(time.group(1))
            if h1 == 12:
                h1 = 0
        if time.group(6) == "PM":
            h2 = int(time.group(4)) + 12
            if h2 == 24:
                h2 = 12
        else:
            h2 = int(time.group(4))
            if h2 == 12:
                h2 = 0
        if time.group(2):
            m1 = time.group(2)
        else:
            m1 = "00"
        if time.group(5):
            m2 = time.group(5)
        else:
            m2 = "00"

    else:
        raise ValueError()
    return f"{h1:02}:{m1:02} to {h2:02}:{m2:02}"

if __name__ == "__main__":
    main()