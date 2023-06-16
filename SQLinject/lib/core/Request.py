import requests
import bs4
from SQLinject.lib.core.Check import SQLCheck


class request:


    def getvaluename(url):
        text1 = SQLCheck.returnselectname(url)
        text2 = SQLCheck.returninputname(url)
        text3 = SQLCheck.returntextareaname(url)

        if text1 != 'not has':
            print('select_name:'+SQLCheck.getname(text1))
        else:
            print('not has')

        if text2 != 'not has':
            print('input_name:'+SQLCheck.getname(text2))
            print('input_value:'+SQLCheck.getvalue(text2))
        else:
            print('not has')

        if text3 != 'not has':
            print('textarea_name:'+SQLCheck.getname(text3))
        else:
            print('not has')


    def setpost(url, payload):
        # post
        session = requests.Session()
        response = session.post(url, data=payload)
        Soup = bs4.BeautifulSoup(response.text, 'lxml')
        return SQLCheck.hasError(Soup.text)

    def setget(url, payload):
        # get
        url += payload
        session = requests.Session()
        response = session.get(url)
        Soup = bs4.BeautifulSoup(response.text, 'lxml')
        return SQLCheck.hasError(Soup.text)
