#coding=utf-8 

from selenium import webdriver
import time

#########################启动Chrome浏览器#######################
# 加启动配置
option = webdriver.ChromeOptions()
option.add_argument('disable-infobars')
# option.add_argument('headless')  # 静默模式

# 打开chrome浏览器
driver = webdriver.Chrome(chrome_options=option)
#最大化
driver.maximize_window()

########################以下完善操作步骤########################

driver.get("https://www.baidu.com/")
#延迟2秒
time.sleep(2)
driver.close()



