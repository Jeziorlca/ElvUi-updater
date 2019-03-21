#from lxml import html
import requests
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

###### DONE:######
#def installed_version ():
    #Opens file and checks the current version installed of ElvUi
#    f = open (game_location + file_location, "r")
#    tmp = f.readlines()[2]
#    return tmp[12:17:1]
#print (installed_version())
##################

#if installed_version() == get_version():
#    print ("You are up to date")
#else:
#download latest package and extract to "_retail_\Interface\AddOns"
#    print ("version will be updated")
