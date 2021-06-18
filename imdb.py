import http.client
import urllib.request
from bs4 import BeautifulSoup

conn = http.client.HTTPSConnection("imdb8.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "<"YOUR KEY...!!!">",
    'x-rapidapi-host': "imdb8.p.rapidapi.com"
    }
conn.request("GET", "/title/get-most-popular-movies?homeCountry=GB&purchaseCountry=GB&currentCountry=GB", headers=headers)

res = conn.getresponse()
data = res.read()
namescode=[]
namesfetch=[]
retlist=data.decode("utf-8")
names=retlist.split(',')
for name in names:
    namecode=name.split('/')
    namescode.append(namecode[2])
i=0
souplist=[]
while(i<3):
    souplist.append(namescode[i])
    i=i+1
# Now fetch the name of top three
topthree=[]
for nam in souplist:
    url="https://www.imdb.com/title/"+str(nam)+"/"
    link=urllib.request.urlopen(url)
    data=link.read()
    mydata=data.decode("utf-8")
    link.close()
    soup=BeautifulSoup(mydata, 'html.parser')
    name=soup.find("title")
    moviname=name.text.strip()
    print(moviname,url)
