import os
import argparse

from engine import app


# 项目根目录地址
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
# debug日志位置
DEBUG_LOG = os.path.join(PROJECT_PATH, 'config/log/logs/debug.log')
# error日志位置
ERROR_LOG = os.path.join(PROJECT_PATH, 'config/log/logs/error.log')

def read_debug_log(*, tail=0):
    res = [line for id, line in enumerate(open(DEBUG_LOG, 'r', encoding='utf-8'))]
    if tail != 0:
        for r in res[len(res) - tail:]:
            print(r)
    else:
        [print(r) for r in res]

def read_error_log(*, tail=0):
    res = [line for id, line in enumerate(open(ERROR_LOG, 'r', encoding='utf-8'))]
    if tail != 0:
        for r in res[len(res) - tail:]:
            print(r)
    else:
        [print(r) for r in res]

def main():
    __usage__ = "中国知网并发爬虫"
    parser = argparse.ArgumentParser(description=__usage__)

    group = parser.add_mutually_exclusive_group()

    group.add_argument("-d", "--debug", type=int,
                       help="查看debug日志, 接一个整数表示查看日志末尾行数, 为-1则查看全部")
    group.add_argument("-e", "--error", type=int,
                       help="查看error日志, 接一个整数表示查看日志末尾行数, 为-1则查看全部")
    group.add_argument('-r', "--run", help="输入 runserver 开启爬虫", type=str)

    args = parser.parse_args()

    if args.debug:
        if args.debug > 0:
            read_debug_log(tail=args.debug)
        else:
            read_debug_log()
    elif args.error:
        if args.error > 0:
            read_error_log(tail=args.error)
        else:
            read_error_log()
    elif args.run == 'runserver':
        app.run()
    else:
        print('参数错误, 运行 python manage.py -h 查看帮助')

if __name__ == '__main__':
    main()