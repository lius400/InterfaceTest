#! /usr/bin/env python
#coding=utf-8
import sys,os

sys.path.append("./")
import unittest
from Common.BeautifulReport import BeautifulReport
from Common import logger


if __name__ == '__main__':
    test_suite = unittest.defaultTestLoader.discover('./case', pattern='Test*.py')
    result = BeautifulReport(test_suite)
    result.report(filename='接口测试报告', description='测试deafult报告', log_path='./result')