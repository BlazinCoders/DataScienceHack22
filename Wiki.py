from bs4 import BeautifulSoup
import requests
def getWiki(wikiTitle):
        search = wikiTitle
        search = search.replace(" ","_")
        title="**"+search.capitalize()+"**"
        url = "https://en.wikipedia.org/wiki/"+search
        page = requests.get(url)
        soup = BeautifulSoup(page.content,'html.parser')
        list(soup.children)
        value = soup.find_all('p')
        content=value[1].get_text()+'\nFor More Refer: https://en.wikipedia.org/wiki/'+search
        wikiOut=title+"\n"+content
        return wikiOut
