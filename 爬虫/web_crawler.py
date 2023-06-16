import requests
from bs4 import BeautifulSoup
import queue
from threading import Thread

class Spider:
    def __init__(self, url,spider_num = 1):#爬虫的构造函数输入是网页连接和爬虫的线程数量
        self.url = url
        self.unvisited = queue.Queue()
        self.visited = queue.Queue()
        self.spider = spider_num
        self.links = []#存储无重复爬取的连接
        self.content = []#存储页面源码
    '''
    收集本页面源代码--------------一级爬虫
    '''
    def fetch_page(self):#一级爬虫，爬取网页源码存储在self.html_content里
        response = requests.get(self.url)
        self.html_content = response.text
        return response.content
    def thisurl_content(self):
        print(self.html_content)
    '''
    收集url并打印输出-------------二级爬虫
    '''
    def get_url(self):#抓取页面中包含的所有连接并存储在unbisted队列中
        soup = BeautifulSoup(self.html_content, "html.parser")
        for link in soup.find_all("a"):
            href = link.get("href")
            if href not in self.links:
                self.links.append(href)
        for item in self.links:
            self.unvisited.put(item)

    def print_scanurl(self):#将获取到的相关连接打印输出
        self.thread_printurl = Thread(target= self.printurl)
        self.thread_printurl.start()

    def printurl(self):
        for link in self.links:
            print(url + link)

    '''
    三级爬虫，启用子线程，爬取本Web页面的所有内容
    '''

    def extended_spider(self):
        self.content.append(self.fetch_page(self.url))
        self.get_url()
        self.print_scanurl()
        if not self.unvisited.empty():
            self.thread_subspider = Thread(target = self.subspider)
            self.thread_subspider.start()

    def subspider(self,subu):
        suburl = self.unvisited.get()
        allurl = self.url+suburl
        response = requests.get(allurl)
        html_content = response.text
        self.content.append(html_content)
        soup = BeautifulSoup(html_content, "html.parser")
        for link in soup.find_all("a"):
            href = link.get("href")
            if href not in self.links:
                self.links.append(href)
                self.unvisited.put(href)
                


if __name__ == '__main__':
    # 使用示例
    url = 'http://192.168.1.192:8086/pikachu/'
    spider = Spider(url)
    spider.fetch_page()
    spider.get_url()
    spider.print_scanurl()

