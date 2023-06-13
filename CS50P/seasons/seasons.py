from datetime import date, datetime
import inflect
from sys import exit
p = inflect.engine()

def main():
    dob = input("Date of Birth: ")
    print (calc(dob))




def calc(s):
    try:
        dob_object = datetime.strptime(s, "%Y-%m-%d").date()
        today = date.today()
        final = p.number_to_words((today - dob_object).days * 1440, andword="").capitalize()
        return final + " minutes"
    except ValueError:
        exit("Invalid date")



if __name__ == "__main__":
    main()