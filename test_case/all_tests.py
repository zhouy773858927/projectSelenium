import unittest
import HTMLTestRunner
import baidu,youdaoyongli

# 定义一个单元测试容器
testunit = unittest.TestSuite()

# 将测试用例加入测试容器中
testunit.addTest(unittest.makeSuite(baidu.Baidu))
testunit.addTest(unittest.makeSuite(youdaoyongli.Youdao))

# 定义报告存放路径
filename = 'E:\\requestsSelenium\\request.html'
fp = open(filename, 'wb')

# 定义测试报告
runner = HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title=u'测试报告',
    description=u'用例执行情况'
)

# 执行用例
runner.run(testunit)
fp.close()
