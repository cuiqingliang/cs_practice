# from appium import webdriver
import logging
from appium import webdriver
from appium_practice.PO_practice.page.basepage import BasePage
from appium_practice.PO_practice.page.mainpage import MainPage

#基础配置信息
class App(BasePage):
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename='myapp1.log',
                        filemode='w')
    def start(self):
        if self.driver == None:
            logging.info('driver is None')
            caps = {}
            caps["platformName"] = "android"
            caps["deviceName"] = "127.0.0.1:7555"
            caps["appPackage"] = "com.tencent.wework"
            caps["appActivity"] = ".launch.LaunchSplashActivity"
            caps["noReset"] = "true"
            self.driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
            self.driver.implicitly_wait(5)
        else:
            logging.info('driver is not None')
            self.driver.launch_app()
        return self
    def stop(self):
        self.driver.quit()
    def go_mainpage(self):
        return MainPage(self.driver)