"""异常处理"""
import urllib.request
import urllib.error

try:
    urllib.request.urlopen("http://blog.csdn.net")
except urllib.error.URLError as e:
    if hasattr(e, "code"):
        # 异常状态
        print(e.code)
    if hasattr(e, "reason"):
        # 异常原因
        print(e.reason)
