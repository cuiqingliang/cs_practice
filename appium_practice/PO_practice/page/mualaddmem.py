#手工维护添加成员信息
from appium.webdriver.common.mobileby import MobileBy

from appium_practice.PO_practice.page.basepage import BasePage


class MualAddmem(BasePage):
    def add_mem(self,name,phone):
        self.find(MobileBy.XPATH,'//*[contains(@text,"姓名")]/../android.widget.EditText').send_keys(name)
        self.find(MobileBy.XPATH,'//*[@text="手机号"]').send_keys(phone)
        self.find(MobileBy.XPATH,'//*[@text="设置部门"]').click()
        self.find(MobileBy.ID,'com.tencent.wework:id/gsh').click()
        self.find(MobileBy.ID,'com.tencent.wework:id/i6k').click()
        return MualAddmem(self.driver)

    def back_contact(self):
        from appium_practice.PO_practice.page.contactpage import ContactPage
        return ContactPage(self.driver)