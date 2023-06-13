grocery = dict()

while True:
    try:
        item = input()
        if not item in grocery:
            grocery[item] = 1
        else:
            grocery[item] += 1

    except EOFError:
        grocery = dict(sorted(grocery.items()))
        for row in grocery:
            print(grocery[row], row.upper())
        break
