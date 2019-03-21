import requests
import re
#Base Settings
url = "https://www.tukui.org/download.php?ui=elvui"
page = requests.get(url)
game_location = "E:\\Nowy folder\\World of Warcraft\\"
file_location = "_retail_\\Interface\\AddOns\\ElvUI\\ElvUI.toc"

def get_version():
    pattern = "/downloads/elvui-"r"\d\d\.\d\d"
    for i, line in enumerate(page.text.split("\n")):
        for match in re.finditer(pattern, line):          
            return match.group().split("-")[-1].strip()
print (get_version())

def installed_version ():
    pattern = re.compile("## Version: "r"\d\d\.\d\d")
    for i, line in enumerate(open (game_location + file_location)):
        for match in re.finditer(pattern, line):          
            return match.group().split(":")[-1].strip()
print(installed_version())

if installed_version() == get_version():
    print ("You are up to date")
else:
#download latest package and extract to "_retail_\Interface\AddOns"
    print ("version will be updated")