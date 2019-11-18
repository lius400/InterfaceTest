# -*- coding:utf-8 -*-

import unittest,os
from common.HTMLTestReportCN import HTMLTestRunner

class Mytestclass(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCase1(self):
        self.assertEqual(2,2,"testError")

    def testCase2(self):
        self.assertEqual(2,3,"testError")

    def testCase3(self):
        self.assertNotEqual(2,5,"测试错误")

    def testCase4(self):
        self.assertNotEqual(2,1,"测试错误")


class APITestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCase1(self):
        self.assertEqual(2, 2, "testError")

    def testCase2(self):
        self.assertEqual(3, 3, "testError")

    def testCase3(self):
        self.assertEqual(5, 5, "testError")

    def testCase4(self):
        self.assertNotEqual(2, 1, "测试错误")

    def testCase5(self):
        self.assertNotEqual(2, 9, "testError")

    def testCase6(self):
        pass

def Suite():
    suitetest = unittest.TestSuite()

    suitetest.addTest(Mytestclass("testCase1"))
    suitetest.addTest(Mytestclass("testCase2"))
    suitetest.addTest(Mytestclass("testCase3"))
    suitetest.addTest(Mytestclass("testCase4"))
    suitetest.addTest(APITestCase("testCase1"))
    suitetest.addTest(APITestCase("testCase2"))
    suitetest.addTest(APITestCase("testCase3"))
    suitetest.addTest(APITestCase("testCase4"))
    suitetest.addTest(APITestCase("testCase5"))
    suitetest.addTest(APITestCase("testCase6"))

    return suitetest

if __name__ == '__main__':

    filePath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))+"/result/HTMLTestReportCN.html"
    fp = open(filePath,'w+',encoding='utf-8')
    runner = HTMLTestRunner(stream=fp,title="自动化测试报告",tester='Liuchao')
    runner.run(Suite())
    fp.close()