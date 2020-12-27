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
        cookes = [{'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
                   'value': 'IcltgJq0cV85ke7vtS_VywK4tXTGGGG9kVMAG1s1VgaqumX6hKevgqmz7V6KD0i1CIgdPpnuYvv7XTBnz6kBe1LuBkyZr8unsXzo_1zB4C3uoN6R4IHMFhidbMOYo-IbdmWSz82oOwAsNEpPZketnfvpl_DGg-3U4Pi9RxHc_2qkO3SKHJ7Rtvi-kkZyl6QEm21CFENWVNUDkve3HuAdcfE8KtdBGd0p6tt-l0EI6dXyNvCTdaAFveTGHRgNTclH-61bz7XozjEJX08As52cEg'},
                  {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/',
                   'secure': False,
                   'value': '1688850150592022'},
                  {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/',
                   'secure': False, 'value': '1970325119178384'},
                  {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/',
                   'secure': False, 'value': '1'},
                  {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
                   'value': 'qLqW4GtyYmsK7lrN_pK9BtPUW-Xmf1RPKNuV9r2THztguPahe3XJEK5UKUP0kytD'},
                  {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
                   'value': 'direct'},
                  {'domain': '.qq.com', 'expiry': 1604490453, 'httpOnly': False, 'name': '_gat', 'path': '/',
                   'secure': False, 'value': '1'},
                  {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/',
                   'secure': False, 'value': '6853574656'},
                  {'domain': 'work.weixin.qq.com', 'expiry': 1604521865, 'httpOnly': True, 'name': 'ww_rtkey',
                   'path': '/', 'secure': False, 'value': '5e1lh2m'},
                  {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/',
                   'secure': False, 'value': 'a8862253'},
                  {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/',
                   'secure': False, 'value': '02791834'},
                  {'domain': '.work.weixin.qq.com', 'expiry': 1635953589, 'httpOnly': False,
                   'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False,
                   'value': '1604417590'},
                  {'domain': '.qq.com', 'expiry': 1667562402, 'httpOnly': False, 'name': '_ga', 'path': '/',
                   'secure': False, 'value': 'GA1.2.2100406815.1604407369'},
                  {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/',
                   'secure': False,
                   'value': '1688850150592022'},
                  {'domain': '.qq.com', 'expiry': 2147483650, 'httpOnly': False, 'name': 'ptcz', 'path': '/',
                   'secure': False, 'value': 'c43e73d2a2aabca3e3b33e4ac560d1fd43bd10eae13cfbb0a016eea2308cf6f7'},
                  {'domain': '.work.weixin.qq.com', 'expiry': 1635943367, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
                   'path': '/', 'secure': False, 'value': '0'},
                  {'domain': '.qq.com', 'expiry': 1604576802, 'httpOnly': False, 'name': '_gid', 'path': '/',
                   'secure': False, 'value': 'GA1.2.350320512.1604407369'},
                  {'domain': '.work.weixin.qq.com', 'expiry': 1607082405, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
                   'path': '/', 'secure': False, 'value': 'zh'},
                  {'domain': '.qq.com', 'expiry': 1909219756, 'httpOnly': False, 'name': 'tvfe_boss_uuid', 'path': '/',
                   'secure': False, 'value': '95617963715dd1b0'},
                  {'domain': '.qq.com', 'expiry': 2147483649, 'httpOnly': False, 'name': 'RK', 'path': '/',
                   'secure': False, 'value': 'rViMvoOSa/'},
                  {'domain': '.qq.com', 'expiry': 2147385600.111, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
                   'secure': False, 'value': '445364620'}]
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


