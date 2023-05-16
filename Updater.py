import requests
import re
import os
import zipfile
import distutils
from distutils import dir_util
import tkinter
#Base Settings
url = "https://www.tukui.org/download.php?ui=elvui"
page = requests.get(url)
addons_location = "e:\\World of Warcraft\\_retail_\\Interface\\AddOns\\"
elviu_file_location = "ElvUI\\ElvUI_Mainline.toc"
working_dir = os.getcwd() + '\\temp\\'

if os.path.exists (working_dir) == True: #Check if working directory exists
        pass
else:
        os.makedirs(working_dir) #creates working directory

#Function that checks what is the latest version available to download on ElvUI website
def get_version():
    pattern = "/downloads/elvui-"r"\d\d\.\d\d...."
    for i, line in enumerate(page.text.split("\n")):
        for match in re.finditer(pattern, line):          
            return match.group().split("-")[-1].strip()  

#Function that checks what ElvUI version you have installed in your WoW addons folder
def installed_version ():
    pattern = re.compile("## Version: "r"\d\d\.\d\d")
    for i, line in enumerate(open (addons_location + elviu_file_location)):
        for match in re.finditer(pattern, line):          
            return match.group().split(":")[-1].strip()

#Function that downloads the latest version of ElvUI
def download_update():
    url = 'https://www.tukui.org/downloads/elvui-'+get_version() 
    r = requests.get(url)
    with open(working_dir + 'ElvUI-' + get_version(), 'wb') as f:  
        f.write(r.content)

#Here we check if the version installed is the same that the one we can download.
if installed_version() == get_version()[0:5]:
    print ("You are up to date")
    input("Press enter to exit :")
else:
    print ("Downloading latest version "+ get_version()[0:5])
    download_update() #downloads update 
    print ("Extracting new version")
    zip_ref = zipfile.ZipFile(working_dir + 'ElvUI-' + get_version(), 'r') #Extracts update
    zip_ref.extractall(working_dir + get_version())
    zip_ref.close()
    print ("Updating ElvUi")
    distutils.dir_util.copy_tree(working_dir + get_version() , addons_location) #Moves update from a temp folder to addons
    #distutils.dir_util.remove_tree (working_dir) #clears the temp
    print ("Update complete")
    input("Press enter to exit :")
# dupa