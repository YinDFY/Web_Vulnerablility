from SQLinject.lib.core import Request

if __name__ == '__main__':
    re = Request.request

    url1 = 'http://192.168.249.131/pikachu/vul/sqli/sqli_id.php'
    data1 = {
        'id': "2'",
        'submit': '提交'
    }

    url2 = 'http://192.168.249.131/pikachu/vul/sqli/sqli_str.php'
    data2 = "?name='&submit=查询"

    print(re.setpost(url1, data1), re.setget(url2, data2))
