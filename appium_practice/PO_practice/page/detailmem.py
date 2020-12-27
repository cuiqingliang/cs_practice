#联系人详情页面
from appium.webdriver.common.mobileby import MobileBy

from appium_practice.PO_practice.page.basepage import BasePage
from appium_practice.PO_practice.page.editmempage import EditMempage


class DetailMem(BasePage):
    def dele_mem(self):
        self.find(MobileBy.ID, 'com.tencent.wework:id/i6d').click()
        return EditMempage(self.driver)