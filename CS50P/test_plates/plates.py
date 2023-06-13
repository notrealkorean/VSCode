import re

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    req = 0
    if s[0:2].isalpha:
        req += 1
    if 2 <= len(s) <= 6:
        req += 1

    if check_sequence(s):
        req += 1

    ban = [".", " ", "!", "?", "-", ",", "'"]
    for i in range(len(ban)):
        if ban[i] in s:
            req -= 1

    for i in range(len(s)):
        if s[i] == "0":
            if s[:i].isalpha():
                req -= 1


    if req == 3:
        return True
    else:
        return False


def check_sequence(sequence):
    pattern = r'^[A-Z]+(?:\d+)?$'
    match = re.match(pattern, sequence)
    if match:
        return True
    else:
        return False

if __name__ == "__main__":
    main()