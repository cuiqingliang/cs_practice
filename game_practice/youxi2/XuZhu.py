'''
定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。
所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
加入模块化改造
'''

#定义虚竹类继承童姥类
from game_practice.youxi2.TianS_TL import TongLao
class XuZhu(TongLao):
    #定义虚竹的念经方法
    def read(self):
        print('罪过罪过！')
if __name__=='__main__':
    xuzhu=XuZhu(1200,40)
    xuzhu.read()
    # print(__name__)
