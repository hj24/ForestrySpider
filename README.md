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

## 使用

两种方式：

1. 直接运行 `engine.app` 模块

2. 命令行进入项目目录

    `python manage.py -r runserver` 开启爬虫
    
    `python manage.py -d num` num为行数，打印末尾num行debug日志
    
    `python manage.py -e num` num为行数，打印末尾num行error日志
    
## 代理配置

- 为了爬虫的稳定运行，本项目使用了阿布云的动态IP代理

- 同时也实现了当阿布云账户余额不足时自动切换到本机爬取模式

- 如需使用代理，请在`config/proxy/conf/proxy.ini`文件中替换你自己的阿布云账号

关于阿布云，请看这里: https://www.abuyun.com/http-proxy/dyn-manual.html

PS: 个人觉得阿布云按小时收费一小时一元不算贵，随用随停，很方便。不建议自己搭建IP代理池，耗时且效果不大

## 数据库配置

- 将`config/db/conf/info.ini`中对应选项修改为自己的配置即可，无需修改其他代码

## Bug 记录

1. (2013, 'Lost connection to MySQL server during query ([Errno 54] Connection reset by peer)')

    一次存入数据量过大导致，把设置mysql的max_allow_packet的值设大一点(e.g: 32MB)
    
2. (2055, Broken Pipe)

    大意是这个，当时没来得及复制就改代码了，Broken Pipe一般是和数据库的通信出了问题，如果使用单一连接的话，在某个地方连接坏了，那后面的所有请求都坏了，
    一般解决办法是换用连接池

## 关于
中国银杏网，中国知网林业论文部分异步爬虫，目前采用协程，欢迎PR多线程版本。

欢迎一起维护。