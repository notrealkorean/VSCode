import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    count = re.findall("(^um[^a-z]|[^a-z]um[^a-z]|[^a-z]um$|^um$)", s, re.IGNORECASE)
    return len(count)


if __name__ == "__main__":
    main()