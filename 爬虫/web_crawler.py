'''
爬取页面所有链接
'''
import requests
from bs4 import BeautifulSoup
content = {}
# 发送HTTP请求获取页面内容
url = "http://192.168.1.192:8086/pikachu/"  # 替换成你要爬取的网页地址
response = requests.get(url)
html_content = response.text
content[url] = html_content
print(html_content)#一级爬虫
# 使用BeautifulSoup解析HTML页面
soup = BeautifulSoup(html_content, "html.parser")

# 提取页面中的所有链接
links = []
for link in soup.find_all("a"):
    href = link.get("href")
    if href not in links:
        links.append(href)

# 打印提取的链接
for link in links:
    print(url+link)
    sub_url = url + link
    sub_response  = requests.get(sub_url)
    content[sub_url] = sub_response.text
#二级爬虫
id = 0
for key,value in content.items():
    print('|---------------------------------------------------------------------|')
    print(id)
    id = id+1
    print(key,value)
    print('|---------------------------------------------------------------------|')
    print()

