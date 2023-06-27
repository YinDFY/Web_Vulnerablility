import re
import requests
import urllib.parse
from bs4 import BeautifulSoup


def build_payloads_get(url, payload):
    # 编码参数
    encoded_params = urllib.parse.urlencode(payload)

    # 将查询参数附加到URL中
    full_url = url + '?' + encoded_params

    # 发送GET请求
    response = requests.get(full_url)
    return response

def build_payloads_post(url, payload):
    # 发送POST请求
    response = requests.post(url, data=payload)

    return response

def getParameter(url, data):
    response = requests.get(url)
    # 使用 BeautifulSoup 解析页面
    soup = BeautifulSoup(response.content, "html.parser")

    # 查找所有的表单
    forms = soup.find_all("form")

    # 定义空列表
    name = []
    value_t = []

    # 遍历每个表单，获取参数
    for form in forms:
        # 查找表单中的所有输入元素
        inputs = form.find_all("input")

        # 打印表单参数及其值
        for input in inputs:
            # 获取输入元素的 name 属性值
            param = input.get("name")
            if param:
                # 获取输入元素的 value 属性值
                value = input.get("value")
                if value is None:
                    value = data
                name.append(param)
                value_t.append(value)

    # 返回列表
    return name, value_t

def checkResponseForString(response, data):
    if data in response.text:
        # print("字符串 '{}' 存在于响应中".format(data))
        return True
    else:
        # print("字符串 '{}' 不存在于响应中".format(data))
        return False

def check_xss_get_reflected(url):
    data = '<script>alert(1)</script>'
    # 获取表单参数和值
    name, value_t = getParameter(url, data)
    # 构建payload
    payload = {}
    for i in range(len(name)):
        payload[name[i]] = value_t[i]

    # 打印payload
    # print("Payload:", payload)
    # 构建payload并发送GET请求
    response = build_payloads_get(url, payload)

    return checkResponseForString(response, data)

def check_xss_post_reflected(url):
    payload_login = {
        'username': 'admin',
        'password': '123456',
        'submit': 'Login'
    }
    # 创建会话对象
    session = requests.Session()

    # 发送登录请求，获取并保存 Cookie
    response = session.post(url, data=payload_login)
    data = '<script>alert(document.cookie)</script>'
    data_url = 'http://192.168.1.192:8086/pikachu/vul/xss/xsspost/xss_reflected_post.php'
    # 检查登录是否成功
    if response.status_code == 200:
        # 使用已保存的 Cookie 发送其他请求
        payload = {'message': '<script>alert(document.cookie)</script>', 'submit': 'submit'}
        response = session.post(data_url, data=payload)

        # 处理响应数据
        if response.status_code == 200:
            # 提取需要的数据或进行其他操作
            return checkResponseForString(response, data)
        else:
            return False
    else:
        return False

def check_xss_stored(url):
    data = '<script>alert(document.cookie)</script>';
    # 构建查询参数
    payload = {'message': '<script>alert(document.cookie)</script>', 'submit': 'submit'}
    # 构建payload并发送GET请求
    response = build_payloads_post(url, payload)

    return checkResponseForString(response, data)

def check_xss_dom(url):
    try:
        # 发送GET请求获取页面响应
        response = requests.get(url)
        response_text = response.text

        # 检查页面响应中是否包含关键词
        if 'innerHTML' in response_text or 'innerText' in response_text or 'setAttribute' in response_text:
            return True
        else:
            return False

    except requests.RequestException as e:
        print("请求错误:", e)
        return False

def check_xss_filterate(url):
    data = '<a herf="#" onclick="alert(document.cookie)">';
    # 获取表单参数和值
    name, value_t = getParameter(url, data)
    # 构建payload
    payload = {}
    for i in range(len(name)):
        payload[name[i]] = value_t[i]

    # 打印payload
    # print("Payload:", payload)
    # 构建payload并发送GET请求
    response = build_payloads_get(url, payload)

    return checkResponseForString(response, data)

def check_xss_htmlspecialchars(url):
    data = "#' onclick='alert(document.cookie)'"
    # 获取表单参数和值
    name, value_t = getParameter(url, data)
    # 构建payload
    payload = {}
    for i in range(len(name)):
        payload[name[i]] = value_t[i]

    # 打印payload
    # print("Payload:", payload)
    # 构建payload并发送GET请求
    response = build_payloads_get(url, payload)

    return checkResponseForString(response, data)

def check_xss_href(url):
    data = "javascript:alert(document.cookie)"
    # 获取表单参数和值
    name, value_t = getParameter(url, data)
    # 构建payload
    payload = {}
    for i in range(len(name)):
        payload[name[i]] = value_t[i]

    # 打印payload
    # print("Payload:", payload)
    # 构建payload并发送GET请求
    response = build_payloads_get(url, payload)

    return checkResponseForString(response, data)

def check_xss_js(url):
    data = "';alert(1);//"
    # 获取表单参数和值
    name, value_t = getParameter(url, data)
    # 构建payload
    payload = {}
    for i in range(len(name)):
        payload[name[i]] = value_t[i]

    # 打印payload
    # print("Payload:", payload)
    # 构建payload并发送GET请求
    response = build_payloads_get(url, payload)

    return checkResponseForString(response, data)

def check_xss_vulnerabilities(url):
    vulnerabilities_found = []

    if check_xss_get_reflected(url):
        vulnerabilities_found = ['XSS GET Reflected']
    else:
        if check_xss_post_reflected(url):
            vulnerabilities_found.append('XSS POST Reflected')
        if check_xss_stored(url):
            vulnerabilities_found.append('XSS Stored')
        if check_xss_dom(url):
            vulnerabilities_found.append('XSS DOM')
        if check_xss_filterate(url):
            vulnerabilities_found.append('XSS Filterate')
        if check_xss_htmlspecialchars(url):
            vulnerabilities_found.append('XSS htmlspecialchars')
        if check_xss_href(url):
            vulnerabilities_found.append('XSS Href')
        if check_xss_js(url):
            vulnerabilities_found.append('XSS JavaScript')

    if len(vulnerabilities_found)!=0:
        return vulnerabilities_found[-1]  # 只返回最新检测出的漏洞，最多一个
    else:
        return None



# 示例用法
if __name__ == '__main__':
    # check_xss_get_reflected('http://192.168.1.192:8086/pikachu/vul/xss/xss_reflected_get.php')
    # check_xss_post_reflected('http://192.168.1.192:8086/pikachu/vul/xss/xsspost/post_login.php')
    # check_xss_stored('http://192.168.1.192:8086/pikachu/vul/xss/xss_stored.php')
    # check_xss_filterate('http://192.168.1.192:8086/pikachu/vul/xss/xss_01.php')
    # check_xss_htmlspecialchars('http://192.168.1.192:8086/pikachu/vul/xss/xss_02.php')
    # check_xss_href('http://192.168.1.192:8086/pikachu/vul/xss/xss_03.php')
    # check_xss_js('http://192.168.1.192:8086/pikachu/vul/xss/xss_04.php')
    # check_xss_dom('http://192.168.1.192:8086/pikachu/vul/xss/xss_dom.php')
    print(check_xss_vulnerabilities('http://192.168.1.192:8086/pikachu/vul/xss/xss_reflected_get.php'))