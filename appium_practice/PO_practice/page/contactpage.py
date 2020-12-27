from appium.webdriver.common.mobileby import MobileBy

from appium_practice.PO_practice.page.addmem import AddMem
from appium_practice.PO_practice.page.basepage import BasePage


class ContactPage(BasePage):
    #添加方法
    def goto_addmem(self):
        self.find(MobileBy.XPATH,'//*[@text="添加成员"]').click()
        return AddMem(self.driver)
    #查询方法
    def serach_mem(self):
        from appium_practice.PO_practice.page.searchmem import SearchMem
        self.find(MobileBy.ID,'com.tencent.wework:id/i6n').click()
        return SearchMem(self.driver)