from lxml import html
import requests
page = requests.get('https://www.tukui.org/download.php?ui=elvui')
#tree = html.fromstring(page.content)
#tmp = page.text
f = open("tmp.txt", "w")
f.write(page.text)