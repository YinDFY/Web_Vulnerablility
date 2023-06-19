'''
爬取页面所有链接
'''
import requests
from bs4 import BeautifulSoup
from queue import Queue

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

def spider2_content(url):
    unvisited = Queue()
    links1 = spider1_link(url)
    for link in links1:
        unvisited.put(link)
    while not unvisited.empty():
        suburl = unvisited.get()
        links2 = spider1_link(url+suburl)
        for link in links2:
            if link not in links1:
                links1.append(link)
                unvisited.put(link)

    unique_link = [x for i, x in enumerate(links1) if x not in links1[:i]]
    for link in unique_link:
        print(link)


if __name__ == '__main__':
    spider2_content("http://192.168.1.192:8086/pikachu/")
