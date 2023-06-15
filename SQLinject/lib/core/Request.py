import requests
import bs4
from SQLinject.lib.core.Check import SQLEcho


class request:

    def setpost(url, payload):
        # post
        session = requests.Session()
        response = session.post(url, data=payload)
        Soup = bs4.BeautifulSoup(response.text, 'lxml')
        return SQLEcho.hasError(Soup.text)

    def setget(url, payload):
        # get
        url += payload
        session = requests.Session()
        response = session.get(url)
        Soup = bs4.BeautifulSoup(response.text, 'lxml')
        return SQLEcho.hasError(Soup.text)
