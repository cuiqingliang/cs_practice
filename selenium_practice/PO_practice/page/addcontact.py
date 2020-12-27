#添加联系人
from selenium.webdriver.common.by import By
# from test_po1.page.conttact import Contact
from selenium_practice.PO_practice.page.base import Base


class AddContact(Base):

    def addcon(self,name,account,phonenum):
        self.find(By.ID,'username').send_keys(name)
        self.find(By.ID,'memberAdd_acctid').send_keys(account)
        self.find(By.ID,'memberAdd_phone').send_keys(phonenum)
        self.find(By.CSS_SELECTOR,'.js_btn_save').click()
    def getcontact(self,name):
        locator=(By.CSS_SELECTOR,'.ww_checkbox')
        self.wait_click(locator)
        ele_lis=[]
        while True:
            ele1=self.finds(By.CSS_SELECTOR,'.member_colRight_memberTable_td:nth-child(2)')
            titles=[ele2.get_attribute('title') for ele2 in ele1]
            # for ele2 in ele1:
            #     ele2.get_attribute('title')
            ele_lis.extend(titles)

            if name in ele_lis:
                return True
            ele3 : str=self.find(By.CSS_SELECTOR,'.ww_pageNav_info_text').text
            num,total= ele3.split('/',1)
            if int(num)== int(total):
                return False
            else:
                self.find(By.CSS_SELECTOR,'.ww_commonImg ww_commonImg_PageNavArrowRightNormal').click()
        return ele_lis