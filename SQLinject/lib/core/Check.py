import re
import requests


class SQLCheck:

    def __init__(self):
        pass

    def getrequesttext(self, url):
        return requests.get(url).text

    def getname(self, text):
        pattern = r'name="([^"]+)"'
        ret = re.search(pattern, text)
        if ret:
            ste = ret.group()
            tr = ste.replace('name=', '')
            name = tr.replace('"', '')
            return name
        else:
            return 'null'

    def getvalue(self, text):
        pattern = r'value="([^"]+)"'
        ret = re.search(pattern, text)
        if ret:
            ste = ret.group()
            tr = ste.replace('value=', '')
            value = tr.replace('"', '')
            return value
        else:
            return 'null'

    def returnselect(self, url):

        urltext = self.getrequesttext(url)
        pattern = r'<select.*>'
        rets = re.findall(pattern, urltext)
        if rets:
            texts = ''
            for ret in rets:
                texts += self.getname(ret) + ',' + self.getvalue(ret) + ','
            return texts
        else:
            return 'null'

    def returninput(self, url):

        urltext = self.getrequesttext(url)
        pattern = r"<input[^>]*\/>"
        rets = re.findall(pattern, urltext)
        if rets:
            texts = ''
            for ret in rets:
                texts += self.getname(ret) + ',' + self.getvalue(ret) + ','
            return texts
        else:
            return 'null'

    def returntextarea(self, url):

        urltext = self.getrequesttext(url)
        pattern = r'<textarea.*>'
        rets = re.findall(pattern, urltext)
        if rets:
            texts = ''
            for ret in rets:
                texts += self.getname(ret) + ',' + self.getvalue(ret) + ','
            return texts
        else:
            return 'null'

