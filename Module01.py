# -*- coding:utf-8 -*-
# Module01.py
# 
from selenium import webdriver
import time

from HTMLTestRunner import HTMLTestRunner
import unittest
# 若不添加则在生成报告时会报错：UnicodeDecodeError: 'ascii' codec can't decode byte 0xe7 in position 211: or
import sys
reload(sys)
sys.setdefaultencoding('utf8')


class QA(unittest.TestCase):
    # 初始化浏览器驱动，并设置隐性等待
    def setUp(self):

        option = webdriver.ChromeOptions()
        option.add_argument('disable-infobars')
        
        self.driver = webdriver.Chrome(chrome_options=option)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

        # self.base_url = "http://www.baidu.com"

    # 测试用例001
    def case1(self):
        driver = self.driver
        url1 = "http://www.baidu.com"
        driver.get(url1)
        # driver.find_element_by_id("kw").send_keys("PS")
        # driver.find_element_by_id("su").click()
        time.sleep(3)
        driver.get('http://cn.bing.com')
        time.sleep(3)

        # 屏幕截图并保存
        current_time = time.strftime("%Y_%m_%d_%H_%M_%S")
        pic_path = 'E:\\Python_Files\\Selenium_Test000\\Case001\\P01_' + current_time +'.png'
        driver.save_screenshot(pic_path)
        time.sleep(1)

        #可继续其他操作
        time.sleep(2)

    # 测试用例002
    def case2(self):
        driver = self.driver
        driver.get("https://hao123.com")
        time.sleep(3)

        # 屏幕截图并保存
        current_time = time.strftime("%Y_%m_%d_%H_%M_%S")
        pic_path = 'E:\\Python_Files\\Selenium_Test000\\Case002\\P01_' + current_time +'.png'
        driver.save_screenshot(pic_path)
        time.sleep(1)

        #可继续其他操作
        time.sleep(2)

    # 测试用例003
	# 测试用例004

    # 关闭浏览器
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    # 设置测试套件
    testunit = unittest.TestSuite()
    testunit.addTest(QA("case1"))
    testunit.addTest(QA("case2"))
    # testunit.addTest(QA("case3"))
    # testunit.addTest(QA("case4"))

    # 生成报告名称并规定其存放路径
    current_time = time.strftime("%Y_%m_%d_%H_%M_%S")
    report_path = 'E:\\Python_Files\\Selenium_Test000\\Reports\\Report_'+ current_time +'.html'
    fp = open(report_path, 'wb')
    # 定义测试报告
    runner = HTMLTestRunner(stream=fp,
                            title="自动化测试报告",  # 浏览器及报告title
                            description='自动化测试用例执行情况：')  # 报告描述
    # 运行测试用例
    runner.run(testunit)
    # 关闭报告文件
    fp.close()

