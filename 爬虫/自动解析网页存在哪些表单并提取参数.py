import requests
from bs4 import BeautifulSoup
def getParameter(url):
    response = requests.get(url)
    # 使用 BeautifulSoup 解析页面
    soup = BeautifulSoup(response.content, "html.parser")

    # 查找所有的表单
    forms = soup.find_all("form")

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
                print("表单参数:", param)
                print("参数值:", value)


'''
示例输出：
表单参数: username
参数值: None
表单参数: password
参数值: None
表单参数: submit
参数值: Login
'''
