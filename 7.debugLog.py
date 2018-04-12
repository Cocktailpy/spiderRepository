"""边运行边打印调试日志"""
import urllib.request


def run_and_log():
    # 分别使用urllib.request.HTTPHandler()，urllib.request.HTTPSHandler()将debuglevel设为1
    httphd = urllib.request.HTTPHandler(debuglevel=1)
    httpshd = urllib.request.HTTPSHandler(debuglevel=1)

    # urllib.request.build_opener()创建自定义的opener对象，并使用1中的值作为参数
    opener = urllib.request.build_opener(httphd, httpshd)

    # 创建全局默认的opener对象
    urllib.request.install_opener(opener)
    data = urllib.request.urlopen("http://edu.51cto.com/")


if __name__ == '__main__':
    run_and_log()
