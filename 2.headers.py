"""设置Headers信息，模拟成浏览器去访问网站"""
# ---方法1：使用build_opener()修改报头---------------------
import urllib.request


def use_build_opener_to_change_headers():
    # 定义一个变量url存储要爬取的网址
    url = "https://blog.csdn.net/bKMk01MZ3w/article/details/79549183"

    # 定义变量headers存储对应的User-Agent信息
    # 格式("User-Agent",具体信息)
    headers = ("User-Agent",
               "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36")

    # 创建opener对象，使用build_opener()修改报头
    opener = urllib.request.build_opener()

    # 设置opener对象的addheaders，即设置对应的头信息
    # 给事：opener对象名.addheaders = [头信息]
    opener.addheaders = [headers]

    # 具有头信息的操作(模仿浏览器去打开)
    # 格式：opener对象名.open(url地址)
    data = opener.open(url).read()

    # 将读取的内容写入文件
    fhandle = open("./doc/3.html", "wb")
    fhandle.write(data)
    fhandle.close()


# ---方法2：使用add_header()添加报头---------------------
def use_add_header_to_add_headers():
    # 定义一个变量url存储要爬取的网址
    url = "https://blog.csdn.net/bKMk01MZ3w/article/details/79549183"
    # 创建一个Request对象并赋值给变量req
    # 格式：urllib.request.Request(url地址)
    req = urllib.request.Request(url)
    # 添加报头信息，格式：Request对象名.add_header(字段名，字段值)
    req.add_header("User-Agent",
                   "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36")
    data = urllib.request.urlopen(req).read()
    # 将读取的内容写入文件
    fhandle = open("./doc/4.html", "wb")
    fhandle.write(data)
    fhandle.close()


if __name__ == '__main__':
    # use_build_opener_to_change_headers()
    use_add_header_to_add_headers()

    pass
