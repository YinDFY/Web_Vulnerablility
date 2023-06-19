import bs4
import re
import requests

from SQLinject.lib.core import Check


class request:

    def __init__(self):
        self.SQLCheck = Check.SQLCheck()

    def getvalue(self, url):
        re = ''
        if self.SQLCheck.returnselect(url) != 'null':
            re += self.SQLCheck.returnselect(url)
        if self.SQLCheck.returninput(url) != 'null':
            re += self.SQLCheck.returninput(url)
        if self.SQLCheck.returntextarea(url) != 'null':
            re += self.SQLCheck.returntextarea(url)
        return re

    def setpost(self, url, payload):
        # post
        session = requests.Session()
        response = session.post(url, data=payload)
        # print(response.status_code)
        Soup = bs4.BeautifulSoup(response.text, 'lxml')
        return Soup.text

    def setget(self, url, payload):
        # get
        url += payload
        session = requests.Session()
        response = session.get(url)
        # print(response.status_code)
        Soup = bs4.BeautifulSoup(response.text, 'lxml')
        return Soup.text

    def setgetdata(self, url, payload):
        n = 1
        self_payload = "?"
        pattern = r'[^,]*,'
        values = re.findall(pattern, self.getvalue(url))
        tag = values.__len__()
        while n <= tag / 2:
            values[2 * n - 1] = values[2 * n - 1].replace(',', '')
            values[2 * n - 2] = values[2 * n - 2].replace(',', '')
            if n != 1:
                self_payload += '&'
            if values[2 * n - 1] == 'null':
                self_payload += values[2 * n - 2] + '=' + payload
            else:
                self_payload += values[2 * n - 2] + '=' + values[2 * n - 1]
            n += 1

        return self_payload

    def setpostdata(self, url, payload):
        n = 1
        self_payload = {}
        pattern = r'[^,]*,'
        values = re.findall(pattern, self.getvalue(url))
        tag = values.__len__()
        while n <= tag / 2:
            values[2 * n - 1] = values[2 * n - 1].replace(',', '')
            values[2 * n - 2] = values[2 * n - 2].replace(',', '')
            if values[2 * n - 1] == 'null':
                self_payload[values[2 * n - 2]] = payload
            else:
                self_payload[values[2 * n - 2]] = values[2 * n - 1]
            n += 1
        return self_payload

    def is_eq_(self, url, payload1, payload2):
        if self.setget(url, self.setgetdata(url, payload1)) == self.setget(url, self.setgetdata(url, payload2)):
            return False
        else:
            return True

    def checkvul(self, url, payload):

        if self.hasError(self.setpost(url, self.setpostdata(url, payload))):
            return True

        elif self.hasError(self.setget(url, self.setgetdata(url, payload))):
            return True

        elif self.hasError(self.setget(url, '?id=' + payload)):
            return True

    def hasError(self, text):
        flag = False
        pattern = r'You have an error in your SQL syntax'
        ret1 = re.search(pattern, text)
        pattern = r'XPATH syntax error'
        ret2 = re.search(pattern, text)
        if ret1:
            flag = True
        elif ret2:
            flag = True
        return flag
