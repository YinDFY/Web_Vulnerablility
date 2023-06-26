from file_upanddown.download import poc_download
from file_upanddown.upload import poc_upload

def check_file_vulnerabilities(url):
    vulnerabilities_found = []

    if poc_upload(url):
        vulnerabilities_found = ['文件上传漏洞']
    if poc_download(url):
        vulnerabilities_found.append('文件下载漏洞')

    return vulnerabilities_found[:1]  # 只返回最新检测出的漏洞，最多一个