'''
web企业微信练习，使用cookies绕过登录
'''

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class Test_wx:
    def setup(self):
        # option=Options()
        # option.debugger_address='127.0.0.1:9222'
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
    # def teardown(self):
    #     self.driver.quit()
    def test_cookes_wx(self):
        # cookes=self.driver.get_cookies()
        # print(cookes)
        cookes = ''
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        for cookie in cookes:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)
        self.driver.refresh()
        self.driver.find_element_by_css_selector('#menu_contacts > span').click()
        sleep(2)
        j=1
        while j <= 10:
            try:
                ele3=self.driver.find_element_by_xpath(f'//*[@id="member_list"]/tr[{j}]/td[2]/span[1]')
                result = ele3.text
                print(result)
                if result=='cs1':
                    assert result=='cs1'
                    break
            except Exception:
                ele1 = self.driver.find_element(By.XPATH, '//*[@class="ww_operationBar"]/a[1]')
                sleep(2)
                ele1.click()
                self.driver.find_element_by_id('username').send_keys('cs1')
                self.driver.find_element_by_id('memberAdd_acctid').send_keys('cs1')
                sleep(2)
                self.driver.find_element(By.ID, 'memberAdd_phone').send_keys('12345678911')
                sleep(2)
                ele2 = self.driver.find_element_by_xpath('//*[@class="js_member_editor_form"]/div[1]/a[2]')
                sleep(2)
                ele2.click()
                break
            j += 1

        sleep(2)
        i=1
        while True:
            ele4 = self.driver.find_element_by_xpath(f'//*[@id="member_list"]/tr[{i}]/td[2]/span[1]')
            result1 = ele4.text
            print(result1)
            if result1 == 'cs1':
                assert result1 == 'cs1'
                break
            i+=1
        # sleep(1)
        # result=ele3.text
        # print(result)
        # result=ele3.get_attribute('data-id')
        # assert result== '1688850201167003'
        # name=self.driver.find_element_by_css_selector('#member_lisst td:nth-child(2)')
        # name.get_property('title')
        # print(name)


