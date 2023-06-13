def main():
    time = input("What time is it? ")
    time_converted = convert(time)
    if 7 <= time_converted <= 8:
        print("breakfast time")
    elif 12 <= time_converted <= 13:
        print("lunch time")
    elif 18 <= time_converted <= 19:
        print("dinner time")
    else:
        return 0



def convert(time):
    hour, min = time.split(":")
    return float(hour) + float(min) / 60


if __name__ == "__main__":
    main()