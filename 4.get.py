"""
Get请求：Get请求会通过URL网址传递消息，可以直接在URL中写上要传递的信息，
也可以由表单进行传递。如果使用表单进行传递，这表单中的信息会自动转为URL
地址中的数据，通过URL地址传递
"""
import urllib.request


def search_without_chinese():
    # 构建对应的URL地址，该URL地址包含GET请求的字段名和字段内容等信息，并且
    # URL地址满足GET请求的格式，即“http://网址？字段名1=字段内容1&字段名2=字段内容2”
    keywd = "hello"
    url = "http://www.baidu.com/s?wd=" + keywd
    # 以对应的URL为参数，构建Request对象
    req = urllib.request.Request(url)
    # 通过urlopen()打开构建的Request对象
    data = urllib.request.urlopen(req).read()
    fhandle = open("./doc/4.html", "wb")
    fhandle.write(data)
    fhandle.close()


def search_with_chinese():
    url = "http://www.baidu.com/s?wd="
    # 中文
    keywd = "你好"
    # 对中文进行编码
    key_code = urllib.request.quote(keywd)
    url_all = url + key_code
    req = urllib.request.Request(url_all)
    data = urllib.request.urlopen(req).read()
    fh = open("./doc/5.html", "wb")
    fh.write(data)
    fh.close()
    pass


if __name__ == '__main__':
    # search_without_chinese()
    search_with_chinese()

    pass
