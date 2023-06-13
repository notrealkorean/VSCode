coke = 50
print(f"Amount Due: {coke}")
while coke > 0:
    while True:
        insert = input("Insert coin: ")
        if insert == "5" or insert == "10" or insert == "25":
            break
        else:
            print(f"Amount Due: {coke}")

    coke -= int(insert)
    if coke > 0:
        print(f"Amount Due: {coke}")
    elif coke <0:
        print(f"Change Owed: {-coke}")
    else:
        print(f"Change Owed: 0")