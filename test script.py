from lxml import html
import requests
page = requests.get('https://www.tukui.org/download.php?ui=elvui')
f = open("demofile.txt", "w")
f.write(page.text)
##print(page.text)