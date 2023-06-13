def main():
    word = input("Input: ")
    final = shorten(word)


    print(f"Output: {final}")


def shorten(word):
    final = str()
    vowels = ["a", "e", "i", "o", "u"]
    for char in word:
        if char.lower() in vowels:
            continue
        else:
            final = final + char
    return final


if __name__ == "__main__":
    main()






