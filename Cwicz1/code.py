#from playsound import playsound

#playsound('C:\\Users\\Ja\\PycharmProjects\\pythonCwicz1\\waterfall-140894.mp3');


import webbrowser

import requests

#przyklad działania:
#pageurl – pobrana strona, date-data w formacie rok miesiac dzien np. 20230126
#zapytanie do api:
#http://archive.org/wayback/available?url=example.com&timestamp=20060101

pageurl = "pja.edu.pl"
url ="http://archive.org/wayback/available?url="+pageurl+"&timestamp="+str("20230126")
url1 ="http://archive.org/wayback/available?url="+pageurl+"&timestamp="+str("20220126")
url2 ="http://archive.org/wayback/available?url="+pageurl+"&timestamp="+str("20210126")

response = requests.get(url)
d = response.json()
page = d["archived_snapshots"]["closest"]["url"]
webbrowser.open(page)


response = requests.get(url1)
d = response.json()
page = d["archived_snapshots"]["closest"]["url"]
webbrowser.open(page)

response = requests.get(url2)
d = response.json()
page = d["archived_snapshots"]["closest"]["url"]
webbrowser.open(page)