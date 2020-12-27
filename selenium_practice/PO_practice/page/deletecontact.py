#删除联系人的封装
from selenium.webdriver.common.by import By
# from test_po1.page.conttact import Contact
from selenium_practice.PO_practice.page.base import Base

class DeleContact(Base):
    def delete_con(self,name):
        self.find(By.ID,'memberSearchInput').send_keys(name)
        locat=(By.CSS_SELECTOR,'.qui_btn ww_btn js_del_member')
        self.wait_click(locat)
        self.find(By.CSS_SELECTOR,'.qui_btn ww_btn js_del_member').click()
        self.find(By.XPATH,'//*[@class="qui_btn ww_btn ww_btn_Blue"][1]').click()
        # return Contact()