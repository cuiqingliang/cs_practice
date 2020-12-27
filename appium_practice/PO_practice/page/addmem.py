from appium.webdriver.common.mobileby import MobileBy

#添加成员页面，点击手工添加
from appium_practice.PO_practice.page.basepage import BasePage
from appium_practice.PO_practice.page.mualaddmem import MualAddmem

class AddMem(BasePage):
    def goto_mualaddmem(self):
        self.find(MobileBy.XPATH,'//*[@text="手动输入添加"]').click()
        return MualAddmem(self.driver)