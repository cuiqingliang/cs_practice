#主页面消息页
from appium.webdriver.common.mobileby import MobileBy

from appium_practice.PO_practice.page.basepage import BasePage
from appium_practice.PO_practice.page.contactpage import ContactPage


class MainPage(BasePage):
    def goto_contact(self):
        self.find(MobileBy.XPATH,'//*[@text="通讯录"]').click()
        return ContactPage(self.driver)