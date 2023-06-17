import re
import requests


class SQLCheck:

    def getrequesttext(url):
        return requests.get(url).text

    def getname(text):
        pattern = r'name="([^"]+)"'
        ret = re.search(pattern, text)
        if ret:
            ste = ret.group()
            tr = ste.replace('name=', '')
            name = tr.replace('"', '')
            return name
        else:
            return 'null'

    def getvalue(text):
        pattern = r'value="([^"]+)"'
        ret = re.search(pattern, text)
        if ret:
            ste = ret.group()
            tr = ste.replace('value=', '')
            value = tr.replace('"', '')
            return value
        else:
            return 'null'

    def returnselect(url):

        urltext = SQLCheck.getrequesttext(url)
        pattern = r'<select.*>'
        rets = re.findall(pattern, urltext)
        if rets:
            texts = ''
            for ret in rets:
                texts += SQLCheck.getname(ret) + ',' + SQLCheck.getvalue(ret) + ','
            return texts
        else:
            return 'null'

    def returninput(url):

        urltext = SQLCheck.getrequesttext(url)
        pattern = r"<input[^>]*\/>"
        rets = re.findall(pattern, urltext)
        if rets:
            texts = ''
            for ret in rets:
                texts += SQLCheck.getname(ret) + ',' + SQLCheck.getvalue(ret) + ','
            return texts
        else:
            return 'null'

    def returntextarea(url):

        urltext = SQLCheck.getrequesttext(url)
        pattern = r'<textarea[^>]*\/>'
        rets = re.findall(pattern, urltext)
        if rets:
            texts = ''
            for ret in rets:
                texts += SQLCheck.getname(ret) + ',' + SQLCheck.getvalue(ret) + ','
            return texts
        else:
            return 'null'

    def hasError(text):
        pattern = r'You have an error in your SQL syntax'
        ret = re.search(pattern, text)
        if ret:
            return True
        else:
            return False
