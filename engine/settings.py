"""
引擎配置文件

- 放置一些引擎的配置，不需修改主引擎代码，减小耦合
"""


# 控制协程的信号量
PARALLELS = 3

# 控制爬虫休眠时间
BOTTOM_SLEEP_TIME = 0
TOP_SLEEP_TIME = 1.2

# 控制数据库一次存入的量
DATA_BATCH = 1000