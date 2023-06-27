from RCE.RemoteCommandExecutation import check_rce_vulnerability_command
from RCE.RemoteCodeExecute import check_rce_vulnerability_code
def check_rce_vulnerabilities(url):
    vulnerabilities_found = []

    # 检测基于命令注入的RCE漏洞
    rce_command_vulnerability = check_rce_vulnerability_command(url)
    if rce_command_vulnerability:
        vulnerabilities_found.append('远程命令漏洞')

    # 检测基于代码注入的RCE漏洞
    rce_code_vulnerability = check_rce_vulnerability_code(url)
    if rce_code_vulnerability:
        vulnerabilities_found.append('远程代码漏洞')

    if vulnerabilities_found:
        return vulnerabilities_found[-1]  # 只返回最新检测出的漏洞，最多一个
    else:
        return None