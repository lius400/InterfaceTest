#! /usr/bin/env python
# coding=utf-8

import logging

# 实现,让日志信息既在控制台,也在指定路径的文件中输出
# 日志级别等级 CRITICAL > ERROR > WARNING > INFO > DEBUG
class Log:
    def __init__(self,log_file):
        # 创建一个logger,顶级的根目录getlogger,有两个分支,一个是FileHander,一个是StreamHandler
        self.logger = logging.getLogger("Testlogger")
        self.logger.setLevel(logging.INFO)

        # 创建一个handler,将log写入文件
        fh = logging.FileHandler(log_file,mode='a')
        fh.setLevel(logging.INFO)

        # 再创建一个handler,将log输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 设置输出格式
        log_format = "%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s: %(message)s"
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

    '''
    log1 = Log('D:/接口自动化测试/logs/test.log')
    log1.info("测试") 
    '''
    '''
    logger.error('下雨了')
    logger.info('打雷了')
    logger.debug('收衣服了')
    '''