#! /usr/bin/env python
# coding=utf-8

import logging,os


log_file = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + '/logs/test.log'
# 实现,让日志信息既在控制台,也在指定路径的文件中输出
# 日志级别等级 CRITICAL > ERROR > WARNING > INFO > DEBUG
class Log:
    def __init__(self,Current_class):
        # 创建一个logger,顶级的根目录getlogger,有两个分支,一个是FileHander,一个是StreamHandler
        self.logger = logging.getLogger(Current_class)
        self.logger.setLevel(logging.INFO)

        # 创建一个handler,将log写入文件
        fh = logging.FileHandler(log_file,mode='a')
        fh.setLevel(logging.INFO)

        # 再创建一个handler,将log输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 设置输出格式
        log_format = "%(asctime)s %(name)s [line:%(lineno)d] %(levelname)s: %(message)s"
        # 把格式添加进来
        formatter = logging.Formatter(log_format)
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 把handler添加到logger里
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def info(self, content):
            self.logger.info(content)

    def error(self, content):
            self.logger.error(content)
