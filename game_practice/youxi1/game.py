'''一个回合制游戏，每个角色都有hp 和power，hp代表血量，power代表攻击力，
hp的初始值为1000，power的初始值为200。
定义一个fight方法：
my_final_hp = my_hp - enemy_power
enemy_final_hp = enemy_hp - my_power
两个hp进行对比，血量剩余多的人获胜
'''
#1、选择角色
#2、选择升级还是打怪
#3、判断输赢

import random
#定义一个玩家的角色的类方法
class Player():
    def __init__(self,play_hp=800,play_power=180):
        self.play_hp=play_hp
        self.play_power=play_power
#定义玩家升级函数
def update_play(play_hp,play_power):
    play_hp = play_hp+30
    play_power = play_power+10
    print(play_hp,play_power)
    return play_hp,play_power
#定义打怪兽函数
def fight(empt_hp,play_hp,play_power,empt_power):
    # empt_hp = empt_hp
    # play_hp = play_hp
    while True:
        empt_hp = empt_hp - play_power
        play_hp = play_hp - empt_power
        if empt_hp<=0:
            print('玩家获胜，游戏结束！')
            break
        elif play_hp<=0:
            print('对不起，挑战失败，游戏结束！')
            break

if __name__=='__main__':
    hp = [x for x in range(1100, 1250)]#血量列表
    print('==============欢迎来到帅哥美女打怪兽游戏======================')
    print('请选择以下玩家：')
    print('1、帅哥')
    print('2、美女')
    choose = int(input('请选择玩家1or2：'))
    play_sg=Player()#初始化玩家对象
    play_hp=play_sg.play_hp#初始化玩家血量
    play_power=play_sg.play_power#初始化玩家攻击力
    empt_hp = random.choice(hp)  # 初始化怪兽血量
    empt_power = random.randint(190, 230)  # 初始化怪兽攻击力
    #开始玩家选择角色
    while True:
        if choose==1:#判断帅哥角色
            print('选择帅哥角色成功！')
            print(f'您当前的血量为:{play_hp},攻击力为：{play_power}')
            break
        elif choose==2:#判断美女角色
            print('选择美女角色成功！')
            print(f'您当前的血量为:{play_hp},攻击力为：{play_power}')
            break
        else:
            choose =input('选择错误，请重新选择：')
    print('==========================================================')
    #玩家进行游戏选择
    while True:
        choose1=int(input('请选择1、玩家升级；2、打怪兽:'))
        if choose1 == 1:#玩家升级选择
            re=update_play(play_hp,play_power)
            play_hp=re[0]
            play_power=re[1]
            print(f'您当前的血量为:{play_hp},攻击力为：{play_power}')
        elif choose1 == 2:#玩家打怪兽选择
            fight(empt_hp,play_hp,play_power,empt_power)
            break
        else:
            choose1=int(input('请选择1、玩家升级；2、打怪兽:'))





