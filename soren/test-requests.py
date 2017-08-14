import requests
import re
from datetime import datetime


def main():
    losSantos = "https://www.roblox.com/My/Groups.aspx?gid=3168876"
    randomHotel = "https://www.roblox.com/My/Groups.aspx?gid=3022142"
    lastGroupPage = "https://www.roblox.com/search/groups?keyword=Hotel"
    baseGroupURL = "https://www.roblox.com/My/Groups.aspx?gid="
    baseGroupAdminURL = "https://www.roblox.com/my/groupadmin.aspx?gid=3168876"

    # ENTER THE START AND END OF THE RANGE HERE
    # Small range for testing
    # Large range when you are ready to generate the output
    startRange = 38
    endRange = 44

    # ENTER MINIMUM MEMBERS YOU WANT TO LOG
    # For now, we are using 1. If you only want to look at groups with
    # many members, then make this number larger
    minMembers = 1

    groups = list(range(startRange, endRange))

    with open("../logs/roblox-groups" + datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + ".txt", "w") as file:

      for group in groups:
         page = requests.get(baseGroupURL + str(group))
         lines = page.text.split("\n")
         record = str(group)
         haveSeen = False

         for line in lines:

             if ("No One" in line):
                 record += ": UNOWNED"

             num = re.search("([0-9]+) member", line)
             if (num):
                 if (haveSeen):
                     record += ""
                 else:
                     haveSeen = num.group(1)
                     record += ": " + haveSeen

         print(record)
         if (re.search("UNOWNED", record) and int(haveSeen) > minMembers):
             file.write(str(record))
             file.write("\n")

      file.close()


main()
