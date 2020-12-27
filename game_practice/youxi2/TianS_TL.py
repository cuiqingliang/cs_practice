'''
定义一个天山童姥类 ，类名为TongLao，
属性有血量，武力值（通过传入的参数得到）。TongLao类里面有2个方法，
see_people方法，需要传入一个name参数，如果传入”WYZ”（无崖子），
则打印，“师弟！！！！”，如果传入“李秋水”，打印“师弟是我的！”，
如果传入“丁春秋”，打印“叛徒！我杀了你”
fight_zms方法（天山折梅手），调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。
需要传入敌人的hp，power，进行一回合制对打，打完之后，比较双方血量。血多的一方获胜。
'''
#定义天山童姥类
class TongLao:
    #初始化血量和功力值属性
    def __init__(self,hp,power):
        self.hp=hp
        self.power=power

    #定义查看角色的方法
    def see_people(self,name):
        if name=='WYZ':
            print('师弟！！！！')
        elif name=='李秋水':
            print('师弟是我的！')
        elif name=='丁春秋':
            print('叛徒！我杀了你！')
        else:
            print('是不是想偷学北冥神功！')
    #定义天山折梅手武功
    def fight_zms(self,empt_hp,empt_power):
        self.hp = self.hp / 2#调用时自己血量减少两倍
        self.power=self.power * 10#调用时自己武力值提升10倍
        #回合对打
        self.hp=self.hp - empt_power
        empt_hp=empt_hp-self.power
        if self.hp > empt_hp:
            print('我赢了！')
        else:
            print('我输了！')
if __name__== '__main__':
    qiaofeng =TongLao(1000,30)
    qiaofeng.see_people('WYZ')
    qiaofeng.see_people('李秋水')
    qiaofeng.see_people('丁春秋')
    qiaofeng.see_people('hh')
    qiaofeng.fight_zms(500,200)
    # print(__name__)


