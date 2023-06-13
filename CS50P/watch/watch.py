import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
   if link := re.search(r'.+src="(https?://(?:www\.)?youtube\.com/embed/.+)".+', s):
       revised1 = link.group(1).replace("embed/", "")
       revised2 = revised1.replace("youtube.com", "youtu.be")
       revised3 = re.sub("^http:", "https:", revised2)
       revised4 = re.sub(r"www\.", "", revised3)

       return revised4

   else:
       return None




if __name__ == "__main__":
    main()