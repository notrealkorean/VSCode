month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input("Date: ").strip()
        if date[0].isnumeric():
            m, d, y = date.split("/")
            m = int(m)
            d = int(d)
            y= int(y)
            if m > 12 or d > 31:
                continue
            else:
                print(f"{y}-{m:02}-{d:02}")
                break
        else:
            m_temp, d_temp, y = date.split(" ")
            m = month.index(m_temp) + 1
            d = int(d_temp[:-1])
            if m > 12 or d > 31:
                continue
            else:
                print(f"{y}-{m:02}-{d:02}")
                break
    except ValueError:
        pass


