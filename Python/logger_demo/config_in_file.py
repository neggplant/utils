#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time    : 11/23/20 4:20 PM
@Author  : CQ
@Describe:
"""
import logging
from logging.handlers import RotatingFileHandler
from logging.handlers import TimedRotatingFileHandler


a = False
b = True
if a:
    # 不使用日志回滚
    logger = logging.getLogger(__name__)
    logger.setLevel(level=logging.INFO)
    handler = logging.FileHandler("log.log")
    formatter = logging.Formatter(
        fmt='%(asctime)s.%(msecs)05d %(levelname)s - %(filename)s - [line:%(lineno)d] - %(message)s',
        datefmt="%Y-%m-%d %H:%M:%S")

    handler.setLevel(logging.INFO)
    handler.setFormatter(formatter)
    # 添加到控制台
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(formatter)

    logger.addHandler(handler)
    logger.addHandler(console)
else:
    # 使用日志备份
    logger = logging.getLogger(__name__)
    logger.setLevel(level=logging.INFO)
    # 按文件大小备份，定义一个RotatingFileHandler，最多备份3个日志文件，每个日志文件最大1K，日志文件名后面加.1
    # rHandler = RotatingFileHandler("log.log", maxBytes=1 * 1024, backupCount=3)
    # 按文件大小备份，定义一个RotatingFileHandler，最多备份3个日志文件，日志文件名后面加."%Y-%m-%d"
    rHandler = TimedRotatingFileHandler("a.log", when="S", backupCount=3)
    rHandler.suffix = "-%Y-%m-%d_-%H-%M-%S.log"
    # rHandler.extMatch = r"^\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2}(\.\w+)?$"
    formatter = logging.Formatter(
        fmt='%(asctime)s.%(msecs)05d %(levelname)s - %(filename)s - [line:%(lineno)d] - %(message)s',
        datefmt="%Y-%m-%d %H:%M:%S")

    rHandler.setLevel(logging.INFO)
    rHandler.setFormatter(formatter)

    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(formatter)

    logger.addHandler(rHandler)
    logger.addHandler(console)

def main():
    logger.info("Start print log")
    logger.debug("Do something")
    logger.warning("Something maybe fail.")
    logger.info("Finish")

if __name__ == "__main__":
    import time
    for i in range(0, 5):
        main()
        time.sleep(2)