## 环境
本项目基于Python3，如何安装Python？

Unix & Linux 平台安装 Python: [Unix/Linux安装](https://www.python.org/downloads/source/)

Windows 平台安装 Python: [Windows安装](https://www.python.org/downloads/windows/)

**此外，如果你的Python版本在3.4以下，你还需要安装pip，升级Python版本**

安装pip请参考: [菜鸟教程 安装pip](https://www.runoob.com/w3cnote/python-pip-install-usage.html)
## 安装依赖
- 运行`pip install -r requirements.txt`安装项目依赖环境

依赖:

解析网页:

> beautifulsoup4

> lxml

数据库连接: 

> PyMySQL

> mysql-connector

ORM:

> peewee

爬取网页:

> aiohttp

## Bug 记录

1. (2013, 'Lost connection to MySQL server during query ([Errno 54] Connection reset by peer)')

    一次存入数据量过大导致，把设置mysql的max_allow_packet的值设大一点(e.g: 32MB)
    
2. (2055, Broken Pipe)

    大意是这个，当时没来得及复制就改代码了，Broken Pipe一般是和数据库的通信出了问题，如果使用单一连接的话，在某个地方连接坏了，那后面的所有请求都坏了，
    一般解决办法是换用连接池

## 关于
中国银杏网，中国知网林业论文部分异步爬虫，目前采用协程，欢迎PR多线程版本。

欢迎一起维护。