from appium.webdriver.common.mobileby import MobileBy

from appium_practice.PO_practice.page.app import App


class Test_Po_wx:
    def setup(self):
        self.main=App()
        self.main.start()

    def test_addmem(self):
        name='ww'
        phone='13212111111'
        self.main.go_mainpage().goto_contact().goto_addmem().goto_mualaddmem().add_mem(name,phone)
        result=self.main.toast(MobileBy.XPATH,'//*[@text="添加成功"]')
        assert result=='添加成功'
    def test_delemem(self):
        name='ww'
        ele=self.main.go_mainpage().goto_contact().serach_mem()
        sums1= len(ele.seach_mems(name))
        sums2= len(ele.goto_detail_mem(name).dele_mem().goto_editdele_mem().delemem().seach_mems(name))
        assert sums1-sums2 == 1