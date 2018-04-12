import urllib.request
import urllib.parse


def request_method_get():
    # 1.设置好URL网址
    url = "http://www.iqianyue.com/mypost"

    # 2.构建表单数据，并使用urllib.parse.urlencode对数据进行编码处理
    postdata = urllib.parse.urlencode({
        "name": "xxx",  # 用户名
        "pass": "xxx"  # 密码
    }).encode('utf-8')

    # 3.创建Request对象，参数包括URL地址和要传递的数据
    req = urllib.request.Request(url, postdata)

    # 4.使用add_header()添加头信息，模拟浏览器进行爬取
    req.add_header(
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36")
    # 5.使用urllib.request.urlopen()打开对应的Request对象，完成信息传递
    data = urllib.request.urlopen(req).read()

    # 6.后续处理
    fhandle = open("./6.html", "wb")
    fhandle.write(data)
    fhandle.close()
