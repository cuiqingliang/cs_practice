#基础配置封装
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Base():
    _urlss=''
    def __init__(self,driver: WebDriver =None):
        if driver == None:
            option=Options()
            option.debugger_address='127.0.0.1:9222'
            self.driver=webdriver.Chrome(options=option)
            self.driver.implicitly_wait(5)
        else:
            self.driver=driver
        if self._urlss !='':
            self.driver.get(self._urlss)

    def find(self,by,value):
        return self.driver.find_element(by,value)

    def finds(self,by,value):
        return self.driver.find_elements(by,value)

    def wait_click(self,locator,timeout=10):
        WebDriverWait(self.driver,timeout).until(expected_conditions.element_to_be_clickable(locator))


