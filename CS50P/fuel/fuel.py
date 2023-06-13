while True:
    try:
        fraction = input("Fraction: ")
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)
        if x > y:
            continue
        else:
            percent = ( x / y )* 100
            break
    except (ValueError, ZeroDivisionError):
        pass


if percent <= 1:
    print("E")
elif percent >= 99:
    print("F")
else:
    print(f"{round(percent)}%")