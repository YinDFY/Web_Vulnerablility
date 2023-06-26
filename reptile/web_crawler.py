'''
爬取页面所有链接
'''
import requests
from bs4 import BeautifulSoup
from queue import Queue
from urllib.parse import urljoin, urlparse

def spider1_link(url):
    links = []
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, "html.parser")
    for link in soup.find_all("a"):
        href = link.get("href")
        if href not in links:
            links.append(href)
    return links

def spider1_content(url):
    response = requests.get(url)
    html_content = response.text
    return html_content

def is_same_origin(url1, url2):
    parsed_url1 = urlparse(url1)
    parsed_url2 = urlparse(url2)
    return parsed_url1.netloc == parsed_url2.netloc

def spider2_content(url):
    url_list=[]
    base_url = url
    unvisited = Queue()
    links1 = spider1_link(url)
    for link in links1:
        unvisited.put(link)
    while not unvisited.empty():
        suburl = unvisited.get()
        absolute_url = urljoin(base_url, suburl)  # 构建绝对URL
        if is_same_origin(base_url, absolute_url):  # 判断是否同源
            links2 = spider1_link(absolute_url)
            for link in links2:
                if link not in links1:
                    links1.append(link)
                    unvisited.put(link)

    unique_link = [x for i, x in enumerate(links1) if x not in links1[:i]]
    for link in unique_link:
        absolute_link = urljoin(base_url, link)  # 构建绝对URL
        # print(absolute_link)
        url_list.append(absolute_link)
    return url_list


if __name__ == '__main__':
    spider2_content("http://192.168.1.192:8086/pikachu/")
