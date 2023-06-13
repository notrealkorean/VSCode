from random import randint

def main():
    level = get_level()
    score = 0

    for i in range(10):
        q = generate_integer(level)
        ans = q[0] + q[1]

        counter = 0

        while True:

            print(str(q[0]) + " + " + str(q[1]) + " = ", end ="")
            user_ans = input()

            if counter == 2:
                print(str(q[0]) + " + " + str(q[1]) + " = " + str(ans))
                break

            if int(user_ans) != ans or not user_ans.isnumeric:
                print("EEE")
                counter += 1
                continue
            else:
                score += 1
                break

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))

            if not 1 <= level <= 3:
                continue
            else:
                break

        except ValueError:
            pass
    return level


def generate_integer(level):
    if level == 1:
        x = randint(0,9)
        y = randint(0,9)
    elif level == 2:
        x = randint(10,99)
        y = randint(10,99)
    elif level == 3:
        x = randint(100,990)
        y = randint(100,999)

    return [x , y]


if __name__ == "__main__":
    main()


