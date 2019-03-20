def get_version ():
    return True
# Function that checks current version available
def installed_version (path):
    #with open("_retail_\Interface\AddOns\ElvUI\ElvUI.toc", r)
    return False

# Function that checks what is the current version of elvUI in addons folder in "_retail_\Interface\AddOns\ElvUI\ElvUI.toc" file
if installed_version == get_version:
    print ("You are up to date")
else:
#download latest package and extract to "_retail_\Interface\AddOns"
    print ("version will be updated")
