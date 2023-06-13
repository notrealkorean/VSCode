calc = input("Expression: ")
x , y , z = calc.split(" ")
x = float(x)
z = float(z)

if y == "+":
    print(round(x + z, 1))
elif y == "-":
    print(round(x - z, 1))
elif y == "*":
    print(round(x * z, 1))
elif y == "/":
    print(round(x / z, 1))