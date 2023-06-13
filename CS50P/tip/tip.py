def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")



def dollars_to_float(d):
    x = float(d.lstrip(d[0]))
    return x

def percent_to_float(p):
    x = float(p.rstrip(p[-1]))
    return x / 100

main()