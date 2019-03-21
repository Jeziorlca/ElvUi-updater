import requests
import re
import os.path
#Base Settings
url = "https://www.tukui.org/download.php?ui=elvui"
page = requests.get(url)
game_location = "d:\\World of Warcraft\\"
file_location = "_retail_\\Interface\\AddOns\\ElvUI\\ElvUI.toc"

def get_version():
    pattern = "/downloads/elvui-"r"\d\d\.\d\d"
    for i, line in enumerate(page.text.split("\n")):
        for match in re.finditer(pattern, line):          
            return match.group().split("-")[-1].strip()    

print (get_version())

def download_file_name():
    pattern = "/downloads/elvui-"r"\d\d\.\d\d"
    for i, line in enumerate(page.text.split("\n")):
        for match in re.finditer(pattern, line):          
            return match.group().split('/')[-1]

print (download_file_name())
print ('https://www.tukui.org/downloads/'+download_file_name()+'.zip')

def installed_version ():
    pattern = re.compile("## Version: "r"\d\d\.\d\d")
    for i, line in enumerate(open (game_location + file_location)):
        for match in re.finditer(pattern, line):          
            return match.group().split(":")[-1].strip()
print(installed_version())

def download_update():
    url = 'https://www.tukui.org/downloads/'+download_file_name()+'.zip' 
    r = requests.get(url)
    with open('C:\\Users\\Jezior\\source\\repos\\ElvUi-updater\\'+download_file_name()+'.zip', 'wb') as f:  
        f.write(r.content)

#if installed_version() == get_version():
#    print ("You are up to date")
#else:
#download latest package and extract to "_retail_\Interface\AddOns"
  #  print ("version will be updated")

#if os.path.exists(game_location + file_location):
#   else:
#        print ("Could not find ElvUI.toc")