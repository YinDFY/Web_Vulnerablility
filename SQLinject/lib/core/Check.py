import re


class SQLEcho:
    def hasError(text):
        pattern = r'You have an error in your SQL syntax'
        match = re.search(pattern, text)
        if match:
            return True
        else:
            return False
