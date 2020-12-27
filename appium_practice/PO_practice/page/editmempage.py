#个人信息编辑页面
from appium.webdriver.common.mobileby import MobileBy

from appium_practice.PO_practice.page.basepage import BasePage
from appium_practice.PO_practice.page.editdelepage import EditDelepage


class EditMempage(BasePage):
    def goto_editdele_mem(self):
        self.find(MobileBy.ID, 'com.tencent.wework:id/b_x').click()
        return EditDelepage(self.driver)
