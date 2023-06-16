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
            return 'not has'

    def getvalue(text):
        pattern = r'value="([^"]+)"'
        ret = re.search(pattern, text)
        if ret:
            ste = ret.group()
            tr = ste.replace('value=', '')
            value = tr.replace('"', '')
            return value
        else:
            return 'not has'

    def returnselectname(url):

        urltext = SQLCheck.getrequesttext(url)
        pattern = r'<select.*>{1}'
        ret = re.search(pattern, urltext)
        if ret:
            return ret.group()
        else:
            return 'not has'

    def returninputname(url):

        urltext = SQLCheck.getrequesttext(url)
        pattern = r'<input.*>{1}'
        ret = re.search(pattern, urltext)
        if ret:
            return ret.group()
        else:
            return 'not has'

    def returntextareaname(url):

        urltext = SQLCheck.getrequesttext(url)
        pattern = r'<textarea.*>{1}'
        ret = re.search(pattern, urltext)
        if ret:
            return ret.group()
        else:
            return 'not has'

    def hasError(text):
        pattern = r'You have an error in your SQL syntax'
        ret = re.search(pattern, text)
        if ret:
            return True
        else:
            return False
