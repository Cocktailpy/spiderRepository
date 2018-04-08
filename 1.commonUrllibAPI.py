import urllib.request


# >>>urlopen()
def urllib_urlopen():
    # 打开并爬取一个网页
    file = urllib.request.urlopen("http://www.baidu.com/")

    # 读取全部内容
    data = file.read()

    # # 读取全部内容
    # dataline = file.readline()

    # 将网页保存在本地
    fhandle = open("./doc/1.html", "wb")
    fhandle.write(data)
    fhandle.close()


# >>> urlretrieve(),urlcleanup
def urllib_urlretrieve_urlcleanup():
    # 直接打开并爬取网页地址，并保存信息
    filename = urllib.request.urlretrieve("http://edu.51cto.com/", filename="./doc/2.html")

    # 清除urlretrieve产生的缓存
    urllib.request.urlcleanup()


# >>>info()
def file_info():
    # 打开并爬取一个网页
    file = urllib.request.urlopen("http://www.baidu.com/")
    # 返回当起那环境有关的信息 格式：爬取的网页.info()
    print(file.info())


# >>> getcode(),geturl()
def file_getcode_geturl():
    # 打开并爬取一个网页
    file = urllib.request.urlopen("http://www.baidu.com/")
    # 返回当前网页的状态码 # 格式：爬取的网页.getcode()
    print(file.getcode())
    # 获取爬取的url地址  # 格式：爬取的网页.geturl()
    print(file.geturl())


# >>>quote(),unquote()
def quote_unquote():
    # quote()编码
    my_quote = urllib.request.quote("http://www.baidu.com")
    print(my_quote)
    # unquote()解码
    print(urllib.request.unquote(my_quote))


if __name__ == '__main__':
    # urllib_urlopen()
    # urllib_urlretrieve_urlcleanup()
    # file_info()
    # file_getcode_geturl()
    # quote_unquote()
    pass
