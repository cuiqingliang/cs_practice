"""
用类和面向对象的思想，“描述”生活中任意接触到的东西
（比如动物、小说里面的人物，不做限制，随意发挥），数量为5个。
"""
#定义动物类
class Animal:

    def __init__(self,leibie,sex,age):
        self.leibie= leibie#物种属性
        self.sex=sex#性别属性
        self.age=age#年龄属性
    def run(self):#跑的方法
        print('跑得快')
#定义小说类
class XiaoShuo:

    def __init__(self,name,sex,age,power):
        self.name=name#名字属性
        self.sex=sex#性别属性
        self.age=age#年龄属性
        self.power=power#武功属性
    def xlsbz(self):#武功方法
        print('我会降龙十八掌')
#定义车类
class Car:
    def __init__(self,color,price):
        self.color=color#颜色属性
        self.price=price#价格属性
    def run(self):#开车的方法
        print('开的快')

#定义电脑类
class Computer:
    def __init__(self,price,pinpai,cpu,mem):
        self.price=price#价格属性
        self.pinpai=pinpai#品牌属性
        self.cpu=cpu#CPU属性
        self.mem=mem#内存属性
    def dazi(self):
        print('我能打字')
#定义帅哥属性
class SG:
    def __init__(self,height,rich,husdom):
        self.height=180#身高属性
        self.rich=10000000#财富属性
        self.husdom=100#颜值属性

    def LR(self):#帅哥的技能
        print('太帅不好')