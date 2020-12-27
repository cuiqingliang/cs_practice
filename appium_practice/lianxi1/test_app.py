'''
企业微信app结合mumu模拟器练习
'''
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

class Test_App:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = "true"
        self.driver=webdriver.Remote('http://localhost:4723/wd/hub',caps)
        self.driver.implicitly_wait(5)
    def teardown(self):
        self.driver.quit()

    def test_delete(self):
        name='hh'
        #点击通讯录
        self.driver.find_element(MobileBy.XPATH,'//*[@text="通讯录"]').click()
        #点击搜索
        self.driver.find_element(MobileBy.ID,'com.tencent.wework:id/i6n').click()
        #搜索输入内容
        self.driver.find_element(MobileBy.ID,'com.tencent.wework:id/gpg').send_keys(name)
        #获取核查到的数据个数
        sum1=self.driver.find_elements(MobileBy.XPATH,'//*[contains(@class,"android.widget.TextView") and contains(@text,"hh")]')
        sum2= len(sum1)
        print(sum2)
        # 定位需要删除的数据
        self.driver.find_element(MobileBy.XPATH,'//*[contains(@class,"android.widget.TextView") and (@text="hh")]').click()
        #点击多操作
        self.driver.find_element(MobileBy.ID,'com.tencent.wework:id/i6d').click()
        #点击编辑成员
        self.driver.find_element(MobileBy.ID,'com.tencent.wework:id/b_x').click()
        #点击删除成员
        self.driver.find_element(MobileBy.ID,'com.tencent.wework:id/elh').click()
        #点击删除确认的确认按钮
        self.driver.find_element(MobileBy.ID,'com.tencent.wework:id/blx').click()
        #重新获取查到数据的个数
        sum3 = self.driver.find_elements(MobileBy.XPATH, '//*[contains(@class,"android.widget.TextView") and contains(@text,"hh")]')
        sum4 = len(sum3)
        print(sum4)
        assert sum4<sum2



