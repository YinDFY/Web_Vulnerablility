
import sys
import requests
import re
import random
from multiprocessing.dummy import Pool as ThreadPool


list_rar = list(set([i.replace("\n","") for i in open("rar.txt","r").readlines()]))
houzui = ['.rar','.zip','.tar','.tar.bz2','.sql','.7z','.bak','.txt']
headerss = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]

def scan(urlx):
    UA = random.choice(headerss)
    headers = {'User-Agent': UA}
    url1 = urlx + '/.svn/entries'
    try:
        r = requests.head(url=url1, headers=headers, timeout=5)
        print(r.url + " : " + str(r.status_code))
        if r.status_code == 200:
            try:
                r1 = requests.get(url=url1, headers=headers, timeout=5)
                if 'dir' in r1.content and 'svn' in r1.content:
                    with open('svn.txt', 'a+') as a:
                        a.write(url1 + '\n')
                else:
                    pass
            except Exception as e:
                pass
        else:
            pass
    except Exception as e:
        print(e)

    url2 = urlx + '/.git/config'
    try:
        UA = random.choice(headerss)
        headers = {'User-Agent': UA}
        r3 = requests.head(url=url2, headers=headers, timeout=5)
        print(r3.url + " : " + str(r3.status_code))
        if r3.status_code == 200:
            try:
                r4 = requests.get(url=url2, headers=headers, timeout=5)
                if 'repositoryformatversion' in r4.content:
                    with open('git.txt', 'a+') as aa:
                        aa.write(url2 + '\n')
                else:
                    pass
            except Exception as e:
                pass
        else:
            pass
    except Exception as e:
        pass

    url_3 = urlx + '/' + urlx.split(".", 2)[1]
    for x in houzui:
        url3 = url_3 + str(x)
        try:
            UA = random.choice(headerss)
            headers = {'User-Agent': UA}
            r5 = requests.head(url=url3, headers=headers, timeout=5)
            print(r5.url + ' : ' + str(r5.status_code) + ' : ' + str(r5.headers["Content-Length"]))
            try:
                if int(r5.headers["Content-Length"]) > 188888:
                    with open('backup.txt', 'a+') as aaa:
                        aaa.write(url3 + '\n')
                else:
                    pass
            except Exception as e:
                pass
        except Exception as e:
            pass

    for x in list_rar:
        url4 = urlx + x.replace('\n', '')
        try:
            UA = random.choice(headerss)
            headers = {'User-Agent': UA}
            r6 = requests.head(url=url4, headers=headers, timeout=5)
            print(r6.url + " : " + str(r6.status_code) + ' : ' + str(r6.headers["Content-Length"]))
            try:
                if int(r6.headers["Content-Length"]) > 188888:
                    with open('backup.txt', 'a+') as aaa:
                        aaa.write(url4 + '\n')
                else:
                    pass
            except Exception as e:
                pass
        except Exception as e:
            pass

    url5 = urlx + '/WEB-INF/web.xml'
    try:
        UA = random.choice(headerss)
        headers = {'User-Agent': UA}
        r7 = requests.head(url=url5, headers=headers, timeout=5)
        print(r7.url + " : " + str(r7.status_code))
        if r7.status_code == 200:
            try:
                r8 = requests.get(url=url5, headers=headers, timeout=5)
                if '<web-app' in r8.content:
                    with open('webinf.txt', 'a+') as aa:
                        aa.write(url5 + '\n')
                else:
                    pass
            except Exception as e:
                pass
        else:
            pass
    except Exception as e:
        pass


smxc = int(input(str('设置扫描线程数(10-500):')))
url_list = list(set([i.replace("\n", "") for i in open("url.txt", "r").readlines()]))
pool = ThreadPool(processes=smxc)  # 线程数量
result = pool.map(scan, url_list)
pool.close()
pool.join()
'''
代码的具体功能如下：
通过读取文件 "url.txt"，将其中的URL列表加载到内存中。
设置线程池的线程数量。
针对每个URL，创建一个线程，使用随机选择的User-Agent头部发送HTTP请求。
对每个URL执行以下操作：
检查是否存在 ".svn/entries" 文件，如果存在且内容中包含 "dir" 和 "svn" 字符串，则将该URL记录在名为 "svn.txt" 的文件中。
检查是否存在 ".git/config" 文件，如果存在且内容中包含 "repositoryformatversion" 字符串，则将该URL记录在名为 "git.txt" 的文件中。
使用不同的文件扩展名（如".bak"、".zip"等），构建新的URL，发送请求并检查响应的内容长度是否大于188,888字节。如果满足条件，则将该URL记录在名为 "backup.txt" 的文件中。
检查是否存在 "WEB-INF/web.xml" 文件，如果存在且内容中包含 "<web-app" 字符串，则将该URL记录在名为 "webinf.txt" 的文件中。
'''
