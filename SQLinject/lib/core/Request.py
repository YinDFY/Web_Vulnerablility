import bs4
import re
import requests

from SQLinject.lib.core.Check import SQLCheck


class request:

    def getvalue(url):
        re = ''
        if SQLCheck.returnselect(url) != 'null':
            re += SQLCheck.returnselect(url)
        if SQLCheck.returninput(url) != 'null':
            re += SQLCheck.returninput(url)
        if SQLCheck.returntextarea(url) != 'null':
            re += SQLCheck.returntextarea(url)
        return re

    def setpost(url, payload):
        # post
        session = requests.Session()
        response = session.post(url, data=payload)
        print(response.status_code)
        Soup = bs4.BeautifulSoup(response.text, 'lxml')
        return SQLCheck.hasError(Soup.text)

    def setget(url, payload):
        # get
        url += payload
        session = requests.Session()
        response = session.get(url)
        print(response.status_code)
        Soup = bs4.BeautifulSoup(response.text, 'lxml')
        return SQLCheck.hasError(Soup.text)

    def setgetdata(url,payloads):
        n = 1
        payload = "?"
        pattern = r'[^,]*,'
        values = re.findall(pattern, request.getvalue(url))
        tag = values.__len__()
        while n <= tag / 2:
            values[2 * n - 1] = values[2 * n - 1].replace(',', '')
            values[2 * n - 2] = values[2 * n - 2].replace(',', '')
            if n != 1:
                payload += '&'
            if values[2 * n - 1] == 'null':
                payload += values[2 * n - 2] + '=' + payloads[2]
            else:
                payload += values[2 * n - 2] + '=' + values[2 * n - 1]
            n += 1
        return payload

    def setpostdata(url,payloads):
        n = 1
        payload = {}
        pattern = r'[^,]*,'
        values = re.findall(pattern, request.getvalue(url))
        tag = values.__len__()
        while n <= tag / 2:
            values[2 * n - 1] = values[2 * n - 1].replace(',', '')
            values[2 * n - 2] = values[2 * n - 2].replace(',', '')
            if values[2 * n - 1] == 'null':
                payload[values[2 * n - 2]] = payloads[0]
            else:
                payload[values[2 * n - 2]] = values[2 * n - 1]
            n += 1
        return payload
