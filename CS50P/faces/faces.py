def main():
    x = input()
    output = convert(x)
    print(output)


def convert(input):
    if ":)" or ":(" in input:
        input = input.replace(":)", "🙂")
        input = input.replace(":(", "🙁")
        return input
    else:
        return input

main()
