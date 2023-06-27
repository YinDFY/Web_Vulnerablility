from burteforce.burteforce import burteforce_form
from burteforce.burteforce_client import burteforce_client
from burteforce.burteforce_server import burteforce_server

def check_burtforce(url):
    vulnerabilities_found = []

    if burteforce_client(url):
        vulnerabilities_found.append('客户端暴力破解漏洞')
    if burteforce_server(url):
        vulnerabilities_found.append('服务端暴力破解漏洞')
    if burteforce_form(url):
        vulnerabilities_found.append('表单暴力破解漏洞')
    if vulnerabilities_found:
        return vulnerabilities_found[-1]  # 只返回最新检测出的漏洞，最多一个
    else:
        return None
