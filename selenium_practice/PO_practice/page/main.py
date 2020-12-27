#主页的封装
from selenium.webdriver.common.by import By
# from test_po1.page.conttact import Contact
from selenium_practice.PO_practice.page.addcontact import AddContact
from selenium_practice.PO_practice.page.base import Base

class MianPage(Base):

    _urlss='https://work.weixin.qq.com/wework_admin/frame'

    def addcomtact_click(self):
        self.find(By.CSS_SELECTOR,'.index_service_cnt_item_title').click()
        return AddContact(self.driver)
    # def contact_click(self):
    #     self.find(By.CSS_SELECTOR,'#menu_contacts span:nth-child(1)').click()
    #     return Contact(self.driver)

