from lxml import html
import requests
def get_version ():
    page = requests.get(' https://www.tukui.org/download.php?ui=elvui')
    tree = html.fromstring(page.content)
    f = open("demofile.txt", "w")
    f.write(tree)
    #get version form pharsing website code https://www.tukui.org/download.php?ui=elvui
    return True
# Function that checks current version available
def installed_version (path):
    #get current version installed in file ("_retail_\Interface\AddOns\ElvUI\ElvUI.toc", r)
    return False
if installed_version == get_version:
    print ("You are up to date")
else:
#download latest package and extract to "_retail_\Interface\AddOns"
    print ("version will be updated")
