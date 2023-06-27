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
    # links.remove("https://github.com/zhuifengshaonianhanlu")
    # links.remove("http://www.dvwa.co.uk/")
    return links

def spider1_content(url):
    response = requests.get(url)
    html_content = response.text
    return html_content

def is_same_origin(url1, url2):
    parsed_url1 = urlparse(url1)
    parsed_url2 = urlparse(url2)
    return parsed_url1.netloc == parsed_url2.netloc

def remove_query_params(url):
    parts = url.split("?")
    clean_url = parts[0]
    return clean_url
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
    # links.remove("https://github.com/zhuifengshaonianhanlu")
    # links.remove("http://www.dvwa.co.uk/")
    return links

def spider1_content(url):
    response = requests.get(url)
    html_content = response.text
    return html_content

def is_same_origin(url1, url2):
    parsed_url1 = urlparse(url1)
    parsed_url2 = urlparse(url2)
    return parsed_url1.netloc == parsed_url2.netloc

def remove_query_params(url):
    parts = url.split("?")
    clean_url = parts[0]
    return clean_url
def spider2_content(url):
    base_url = url
    unvisited = Queue()
    links1 = spider1_link(url)
    for link in links1:
        unvisited.put(link)
    while not unvisited.empty():
        suburl = unvisited.get()
        suburl = remove_query_params(suburl)
        absolute_url = urljoin(base_url, suburl)  # 构建绝对URL
        if is_same_origin(base_url, absolute_url):  # 判断是否同源
            links2 = spider1_link(absolute_url)
            for link in links2:
                if link not in links1:
                    links1.append(link)
                    unvisited.put(link)

    unique_link = [x for i, x in enumerate(links1) if x not in links1[:i]]
    final_list = []
    for link in unique_link:
        absolute_link = urljoin(base_url, link)  # 构建绝对URL
        final_list.append(absolute_link)
    final_list.remove("https://github.com/zhuifengshaonianhanlu")
    final_list.remove("http://www.dvwa.co.uk/")
    ans = []
    for url in final_list:
        ans.append(remove_query_params(url))
    ans = list(set(ans))
    for url in ans:
        print(url)
    return ans








if __name__ == '__main__':
    spider2_content("http://192.168.1.192:8086/pikachu/")
