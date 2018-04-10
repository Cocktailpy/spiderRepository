import urllib.request


def timeout_setting():
    """超时设置"""
    try:
        file = urllib.request.urlopen("http:/www.baidu.com/", timeout=30)
        data = file.open()
        print(len(data))
    except Exception as e:
        print("出现异常--》" + str(e))
