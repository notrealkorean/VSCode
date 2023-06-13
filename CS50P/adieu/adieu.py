import inflect

p = inflect.engine()
namelist = list()

while True:
    try:
        name = input("Name: ").capitalize()
        namelist.append(name)

    except EOFError:
        joint_list = p.join(namelist)
        print(f"\nAdieu, adieu, to " + joint_list)
        break
