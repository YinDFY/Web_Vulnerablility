
import requests
import urllib.parse
from bs4 import BeautifulSoup


def build_payloads_get(url, payload, session):
    # 编码参数
    encoded_params = urllib.parse.urlencode(payload)

    # 将查询参数附加到URL中
    full_url = url + '?' + encoded_params

    # 发送GET请求
    response = session.get(full_url)
    return response


def build_payloads_post(url, payload, session):
    # 发送POST请求
    response = session.post(url, data=payload)

    return response


def getParameter(url, data, session):
    response = session.get(url)
    # 使用 BeautifulSoup 解析页面
    soup = BeautifulSoup(response.content, "html.parser")

    # 查找所有的表单
    forms = soup.find_all("form")

    # 遍历每个表单，获取参数
    name = []
    value_t = []
    for form in forms:
        # 查找表单中的所有输入元素
        inputs = form.find_all("input")

        for input in inputs:
            # 获取输入元素的 name 属性值
            param = input.get("name")

            if param:
                # 获取输入元素的 value 属性值
                value = input.get("value")
                if value is None:
                    value = data

                if param != "submit" and param != "token":
                    value = data

                print("表单参数:", param)
                print("参数值:", value)

                name.append(param)
                value_t.append(value)

    return name, value_t


def checkResponseForString(response, data):
    if data in response.text:
        print("字符串 '{}' 存在于响应中".format(data))
        return True
    else:
        print("字符串 '{}' 不存在于响应中".format(data))
        return False


def check_csrf_get(url):
    data = 'check_csrf_get'
    # 构建payload
    payload_login = {
        'username': 'lili',
        'password': '123456',
        'submit': 'Login'
    }

    # 打印payload
    print("Payload:", payload_login)
    # 创建会话对象
    session = requests.Session()

    # 编码参数
    encoded_params = urllib.parse.urlencode(payload_login)

    # 将查询参数附加到URL中
    full_url = url + '?' + encoded_params

    # 发送GET请求
    response = session.get(full_url)
    url_edit = 'http://192.168.1.192:8086/pikachu/vul/csrf/csrfget/csrf_get_edit.php'
    # 检查登录是否成功
    if response.status_code == 200:
        # 获取表单参数和值
        name, value_t = getParameter(url_edit, data, session)
        # 构建payload
        payload = {}
        for i in range(len(name)):
            payload[name[i]] = value_t[i]

        # 打印payload
        print("Payload:", payload)
        # 构建payload并发送GET请求
        response = build_payloads_get(url_edit, payload, session)

        # 处理响应数据
        if response.status_code == 200:
            # 提取需要的数据或进行其他操作
            return checkResponseForString(response, data)
        else:
            return '访问受保护页面失败'
    else:
        return '登录失败'


def check_csrf_post(url):
    data = 'check_csrf_post'
    # 构建payload
    payload_login = {
        'username': 'lili',
        'password': '123456',
        'submit': 'Login'
    }

    # 打印payload
    print("Payload:", payload_login)
    # 创建会话对象
    session = requests.Session()

    # 编码参数
    encoded_params = urllib.parse.urlencode(payload_login)

    # 将查询参数附加到URL中
    full_url = url + '?' + encoded_params

    # 发送GET请求
    response = session.get(full_url)
    url_edit = 'http://192.168.1.192:8086/pikachu/vul/csrf/csrfpost/csrf_post_edit.php'
    # 检查登录是否成功
    if response.status_code == 200:
        # 获取表单参数和值
        name, value_t = getParameter(url_edit, data, session)
        # 构建payload
        payload = {}
        for i in range(len(name)):
            payload[name[i]] = value_t[i]

        # 打印payload
        print("Payload:", payload)
        # 构建payload并发送POST请求
        response = build_payloads_post(url_edit, payload, session)

        # 处理响应数据
        if response.status_code == 200:
            # 提取需要的数据或进行其他操作
            return checkResponseForString(response, data)
        else:
            return '访问受保护页面失败'
    else:
        return '登录失败'


def check_csrf_token(url):
    data = 'check_csrf_get_token'
    # 构建payload
    payload_login = {
        'username': 'lili',
        'password': '123456',
        'submit': 'Login'
    }

    # 打印payload
    print("Payload:", payload_login)
    # 创建会话对象
    session = requests.Session()

    # 编码参数
    encoded_params = urllib.parse.urlencode(payload_login)

    # 将查询参数附加到URL中
    full_url = url + '?' + encoded_params

    # 发送GET请求
    response = session.get(full_url)
    url_edit = 'http://192.168.1.192:8086/pikachu/vul/csrf/csrftoken/token_get_edit.php'
    # 检查登录是否成功
    if response.status_code == 200:
        # 获取表单参数和值
        name, value_t = getParameter(url_edit, data, session)
        # 构建payload
        payload = {}
        for i in range(len(name)):
            payload[name[i]] = value_t[i]

        # 打印payload
        print("Payload:", payload)
        # 构建payload并发送POST请求
        response = build_payloads_get(url_edit, payload, session)

        # 处理响应数据
        if response.status_code == 200:
            # 提取需要的数据或进行其他操作
            return checkResponseForString(response, data)
        else:
            return '访问受保护页面失败'
    else:
        return '登录失败'


if __name__ == '__main__':
    print(check_csrf_get('http://192.168.1.192:8086/pikachu/vul/csrf/csrfget/csrf_get_login.php'))
    print(check_csrf_post('http://192.168.1.192:8086/pikachu/vul/csrf/csrfpost/csrf_post_login.php'))
    print(check_csrf_token('http://192.168.1.192:8086/pikachu/vul/csrf/csrftoken/token_get_login.php'))