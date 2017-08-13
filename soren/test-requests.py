import requests

def main():
	losSantos = "https://www.roblox.com/My/Groups.aspx?gid=3168876"
	randomHotel = "https://www.roblox.com/My/Groups.aspx?gid=3022142"
	lastGroupPage = "https://www.roblox.com/search/groups?keyword=Hotel"
	baseGroupURL = "https://www.roblox.com/My/Groups.aspx?gid="
	baseGroupAdminURL = "https://www.roblox.com/my/groupadmin.aspx?gid=3168876"
	
	#print(requests.get(baseGroupAdminURL).text)
	
	groups = list(range(1, 500000))
		
	for group in groups:
		page = requests.get(baseGroupURL + str(group))		
		findUnownedGroups(group, page.text.split("\n"))

def findUnownedGroups(group, lines):	
			
		for line in lines:
			if ("No One" in line):
				print(group)
		
main()
