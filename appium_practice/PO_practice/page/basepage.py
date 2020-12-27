

#基础信息配置初始化
import logging

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename='myapp.log',
                        filemode='w')
    def __init__(self, driver: WebDriver = None):
        self.driver=driver

    def find(self,by,locator):
        logging.info('find')
        logging.info(by)
        logging.info(locator)

        return self.driver.find_element(by,locator)

    def finds(self,by,locator):
        logging.info('finds')
        logging.info(by)
        logging.info(locator)
        return self.driver.find_elements(by,locator)

    def scoll_find(self,text):
        return  self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                        'new UiScrollable(new UiSelector()'
                                        '.scrollable(true).instance(0))'
                                        '.scrollIntoView(new UiSelector()'
                                        f'.text("{text}").instance(0));')
    def toast(self,by,locator):
        logging.info('taost：')
        logging.info(by)
        logging.info(locator)
        return self.find(by,locator).text
