#from lxml import html
import requests
import re
#Base Settings
url = "https://www.tukui.org/download.php?ui=elvui"
game_location = "E:\\Nowy folder\\World of Warcraft\\"
file_location = "_retail_\\Interface\\AddOns\\ElvUI\\ElvUI.toc"
#def get_version ():
#    page = requests.get(url)
#    tree = html.fromstring(page.content)
#    f = open("demofile.txt", "w")
#    f.write(tree)
    #get version form pharsing website code https://www.tukui.org/download.php?ui=elvui
#    return True
# Function that checks current version available

def installed_version ():
    pattern = re.compile("## Version: "r"\d\d\.\d\d")
    for i, line in enumerate(open (game_location + file_location)):
        for match in re.finditer(pattern, line):          
            return match.group().split(":")[-1].strip()
print(installed_version())

#if installed_version() == get_version():
#    print ("You are up to date")
#else:
#download latest package and extract to "_retail_\Interface\AddOns"
#    print ("version will be updated")