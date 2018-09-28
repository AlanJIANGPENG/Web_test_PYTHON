# -*- coding:utf-8 -*-
# Module01.py

from selenium import webdriver
import time, unittest, sys

from HTMLTestRunner import HTMLTestRunner
# 若不添加则在生成报告时会报错：UnicodeDecodeError: 'ascii' codec can't decode byte 0xe7 in position 211: or

reload(sys)
sys.setdefaultencoding('utf8')


class QA(unittest.TestCase):
    # 初始化浏览器驱动，并设置隐性等待
    def setUp(self):
        option = webdriver.ChromeOptions()
        option.add_argument('disable-infobars')
        self.driver = webdriver.Chrome(chrome_options = option)
        self.driver.maximize_window()
        self.driver.implicitly_wait(4)

    # 测试用例001
    def case1(self):
        driver = self.driver
        url1 = "http://www.baidu.com"
        driver.get(url1)
        driver.find_element_by_id("kw").send_keys("PS")
        driver.find_element_by_id("su").click()
        time.sleep(2)
        driver.back()
        time.sleep(2)
        driver.forward()
        time.sleep(2)
        driver.refresh()
        time.sleep(3)

        # 屏幕截图并保存
        current_time = time.strftime("%Y_%m_%d_%H_%M_%S")
        pic_path = 'E:\\Python_Files\\Selenium_Test000\\case001\\P01_' + current_time +'.png'
        driver.save_screenshot(pic_path)
        time.sleep(1)

        # 可继续其他操作
        # time.sleep(2)
        driver.get('http://cn.bing.com')
        time.sleep(4)
        driver.close()

    # 测试用例002
    def case2(self):
        driver = self.driver
        driver.get("https://hao123.com")
        h0 = driver.current_window_handle
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='navrecommend-top']/div/a[2]/img").click()
        time.sleep(1)
        driver.find_element_by_id("search-input").clear()
        driver.find_element_by_name("word").send_keys(u"上海悠悠")
        time.sleep(1)
        driver.find_element_by_class_name("button-hook").click()
        time.sleep(5)
        h_all = driver.window_handles
        driver.switch_to_window(h_all[1])
        driver.close()
        driver.switch_to_window(h0)
        driver.find_element_by_link_text(u"网　易").click()
        time.sleep(5)
        h_all = driver.window_handles
        driver.switch_to_window(h_all[1])
        driver.close()
        driver.switch_to_window(h0)
        driver.find_element_by_partial_link_text(u"京东").click()
        time.sleep(5)

        h_all = driver.window_handles
        # print h_all
        # driver.switch_to_window(h_all[0])
        # print driver.title
        driver.switch_to_window(h_all[1])
        # print driver.title
        driver.close()

        driver.switch_to_window(h0)
        driver.get('https://music.163.com')
        time.sleep(3)
        driver.find_element_by_tag_name("input").send_keys(u"毛不易")
        time.sleep(2)

        # xpath定位学习 -> https://www.cnblogs.com/yoyoketang/p/6123938.html
        # find_element_by_css_selector() 没有研究 -> https://www.cnblogs.com/yoyoketang/p/6128580.html
        # find_elements 一次查找多个元素 -> https://www.cnblogs.com/yoyoketang/p/6128599.html
        # 更多键盘、鼠标事件 -> https://www.cnblogs.com/yoyoketang/p/6128607.html
        # 当前只能实现两个窗口（主窗口和新窗口）的切换，没有实现多窗口的自由切换 || 逐步打开的新窗口则生产为h_all列表

        # 屏幕截图并保存
        current_time = time.strftime("%Y_%m_%d_%H_%M_%S")
        pic_path = 'E:\\Python_Files\\Selenium_Test000\\case002\\P01_' + current_time +'.png'
        driver.save_screenshot(pic_path)
        time.sleep(1)

        # 可继续其他操作
        time.sleep(2)

        driver.get('https://www.hao123.com/')
        time.sleep(3)
        driver.find_element_by_id("search-input").clear()
        driver.find_element_by_name("word").send_keys(u"163邮箱")
        time.sleep(1)
        driver.find_element_by_class_name("button-hook").click()
        time.sleep(3)
        h_all = driver.window_handles
        driver.switch_to_window(h_all[1])
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='1']/h3/a[1]").click()
        time.sleep(4)
        h_all = driver.window_handles
        print (h_all)
        driver.switch_to_window(h_all[2])
        time.sleep(2)
        # 切换iframe
        driver.switch_to_frame('x-URS-iframe')
        # iframe = driver.find_element_by_tag_name("iframe")      # iframe的切换是默认支持id和name的方法的
        # driver.switch_to_frame(iframe)                          # 当然实际情况中会遇到没有id属性和name属性为空的情况
        time.sleep(1)
        driver.find_element_by_name('email').clear()
        time.sleep(1)
        driver.find_element_by_name("email").send_keys("15652076839")
        time.sleep(1)
        driver.find_element_by_id("dologin").click()
        # 释放iframe
        driver.switch_to.default_content()
        time.sleep(3)
        driver.close()
        driver.switch_to_window(h_all[1])
        time.sleep(2)
        driver.close()
        driver.switch_to_window(h_all[0])
        time.sleep(1)


    # # 测试用例003
    # def case3(self):
    #     driver = self.driver
    #     ######

    # 测试用例004
    # ######

    # 关闭浏览器
    def tearDown(self):
        time.sleep(5)
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
