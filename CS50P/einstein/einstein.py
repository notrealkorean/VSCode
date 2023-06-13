mass = str()

while not mass.isnumeric():
    mass = input("Mass (in kg): ")

mass = int(mass)

print(mass * 300000000**2)
