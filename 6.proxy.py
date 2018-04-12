"""
使用同一个IP去爬取同一个网站上的网页，容易被服务器屏蔽
"""
import urllib.request


# ip地址：网址:端口号
def use_proxy(proxy_addr, url):
    # 使用urllib.request.ProxyHandler()设置对应的代理服务器信息
    # 格式：urllib.request.ProxyHandler({'http': 代理服务器地址})
    proxy = urllib.request.ProxyHandler({'http': proxy_addr})

    # 自定义opener对象，（代理信息，urllib.request.HTTPHandler类）
    opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)

    # 创建全局默认的opener对象
    urllib.request.install_opener(opener)

    # 爬取网页信息，编码后赋给变量data
    data = urllib.request.urlopen(url).read().decode('utf-8')
    return data


if __name__ == '__main__':
    proxy_addr = "202.75.210.45:7777"
    data = use_proxy(proxy_addr, "https://www.baidu.com/")
    print(len(data))
