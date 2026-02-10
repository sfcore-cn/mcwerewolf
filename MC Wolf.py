#Made by "谢铭楷".Powered by Werewolf 2(作者作)
#Create at 2024.8.2
#Please visit https://m82.org for more info.
import collections,random as r
winnum=0
losenum=0
emerald=0#绿宝石
def main():
    print('''    -----Minecraft狼人杀-----
Python Edition 2024.8.19 v2.0
制作:星流核心(原名脚臭楷)
由作者制作的原版Werewolf 2游戏v2.11版本修改而成
https://m82.org
未经允许请勿修改!!!
注:本游戏有一堆“特性”（bug）''')
    modechoose=input('''
    开始游戏（输入A）
    游戏玩法（输入B）
    游戏商城（输入C）''')
    if modechoose=='A':
        game()
    elif modechoose=='B':
        laws()
    elif modechoose=='C':
        shop()
    elif modechoose=='SB':
        print('你发现了彩蛋')
        adminchanges()
    else:
        print('请遵只因兽法,文冥用语,自动调整为游戏模式')
        game()
def game():
    zombie=[]
    skeleton=[]
    creeper=[]
    witch=[]
    spider=[]
    enderman=[]
    normals=[]
    puppet=[]
    preist=[]
    armor=[]
    mapper=[]
    farmer=[]
    toolmaker=[]
    roles=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    while len(roles)>0:
        k=str(len(roles))
        a=roles[r.randint(0,len(roles)-1)]
        roles.remove(a)
        if a<2:
            zombie.append(k)
        elif a<3:
            skeleton.append(k)
        elif a<4:
            creeper.append(k)
        elif a<5:
            witch.append(k)
        elif a<6:
            spider.append(k)
        elif a<7:
            enderman.append(k)
        elif a<10:
            normals.append(k)
        elif a<11:
            puppet.append(k)
        elif a<12:
            preist.append(k)
        elif a<13:
            armor.append(k)
        elif a<14:
            mapper.append(k)
        elif a<15:
            farmer.append(k)
        else:
            toolmaker.append(k)
    monsters=zombie+skeleton+creeper+spider+enderman
    villagers=normals+puppet+preist+armor+mapper+farmer+toolmaker
    def dead(b):
        if str(b) in monsters:
            monsters.remove(str(b))
        if str(b) in villagers:
            villagers.remove(str(b))
        if str(b) in zombie:
            zombie.remove(str(b))
        elif str(b) in witch:
            witch.remove(str(b))
        elif str(b) in skeleton:
            skeleton.remove(str(b))
        elif str(b) in creeper:
            creeper.remove(str(b))
        elif str(b) in spider:
            spider.remove(str(b))
        elif str(b) in enderman:
            enderman.remove(str(b))
        elif str(b) in normals:
            normals.remove(str(b))
        elif str(b) in puppet:
            puppet.remove(str(b))
        elif str(b) in preist:
            preist.remove(str(b))
        elif str(b) in armor:
            armor.remove(str(b))
        elif str(b) in mapper:
            mapper.remove(str(b))
        elif str(b) in farmer:
            farmer.remove(str(b))
        elif str(b) in toolmaker:
            toolmaker.remove(str(b))
        overs.append(str(b))
    outs=[]
    def revive(c):
        if str(c) in overs:
            if str(c) in outs:
                print('这个人死了超过1天,选项无效')
            else:
                overs.remove(str(c))
                normals.append(str(c))
    def realrole(d):
        if d in monsters:
            print('他是个坏人')
        if d in villagers:
            print('他是好人')
        else:
            print('继续')
    def immnue():
        if milk in overs:
            b=None
            overs.remove(milk)
            normals.append(milk)
        if str(milk)==str(c):
            c=None
        if str(milk)==str(scared):
            scared=None
    global b
    global c
    global d
    print('    ----------游戏开始----------')
    print('你是1号')
    for nights in range(1,8):
        overs=[]
        areyouok=False
        print()
        print('    ----- 第 '+str(nights)+' 天 -----    ')
        if '1' in monsters:
            if '1' in zombie:
                print('你是僵尸')
            elif '1' in skeleton:
                print('你是骷髅')
            elif '1' in creeper:
                print('你是苦力怕')
            elif '1' in spider:
                print('你是蜘蛛')
                scared=int(input('今天你要恐吓谁？被恐吓者今晚不能使用技能'))
                if scared <2 or scared>15:
                    print('你这是违法行为。')
            elif '1' in enderman:
                print('你是末影人')
            print('你属于怪物阵营,全部怪物是'+str(monsters)+str(witch))
            print('天黑请闭眼,怪物请睁眼。')
            if '1' not in spider:
                scared=r.randint(1,15)
            print(scared,'号被恐吓了，他今晚不能使用技能')
            if scared != 1:
                b=int(input('今晚你刀几号(1-10)?'))
                if b < 16 and b > 0:
                    dead(b)
                else:
                    print('你选择不刀人')
                print(str(b)+'号死了')
            else:
                b=r.randint(1,15)
                dead()
                print(str(b)+'号死了')
        elif '1' in witch:
            print('你是女巫')
            print('天黑请闭眼,女巫请睁眼。')
            scared=r.randint(1,15)
            print(scared,'号被恐吓了，他今晚不能使用技能')
            if scared != 1:
                b=int(input('今晚你毒几号(1-15)?救人输入其他'))
                if b<15 and b>1:
                    dead(b)
                else:
                    c=int(input('今晚你救几号(1-15)?免疫某人身上效果输入其他'))
                    if c<15 and b>1:
                        revive(c)
                    else:
                        milk=int(input('今晚你免疫谁效果(1-15)?'))
                        immnue(milk)
        elif '1' in puppet:
            print('你是铁傀儡')
            scared=r.randint(1,15)
            print(scared,'号被恐吓了，他今晚不能使用技能')
            if scared != 1:
                print('天黑请闭眼,铁傀儡请睁眼。')
                b=int(input('今晚你杀几号(1-15)?'))
                dead(b)
                print(str(b)+'号死了')
        elif '1' in preist:
            print('你是牧师')
            print('天黑请闭眼，牧师请睁眼。')
            scared=r.randint(1,15)
            print(scared,'号被恐吓了，他今晚不能使用技能')
            if scared != 1:
                isSame=r.randint(1,10)
                print('女巫救了'+str(isSame))
                c=int(input('今晚你救几号(1,10)?'))
                if isSame==c:
                    print('女巫和你救了同一个人，他死了')
                    b=None
                    c=b
                    dead(b)
                    print(str(b)+'号死了')
                    c=None
                revive(b)
            b=r.randint(1,15)
            dead(b)
            print(str(b)+'号死了')
        elif '1' in normals:
            print('你是平民')
            print('天亮了')
            b=r.randint(1,17)
            if b>=15:
                print('昨晚是平安夜')
            else:
                dead(b)
                print(str(b)+'号死了')   
        elif '1' in mapper:
            print('你是制图师')
            scared=r.randint(1,15)
            print(scared,'号被恐吓了，他今晚不能使用技能')
            print('天黑请闭眼,制图师请睁眼。')
            if scared != 1:
                d=int(input('今晚你预言几号(1-15)?'))
                realrole(d)
                if d in enderman:
                    print('你预言的人是末影人，你趋势了')
                    emerald+=1
                    break
                b=r.randint(1,15)
                dead(b)
                print(str(b)+'号死了')
            outs.append(overs)
        if '1' in armor:
            print('你是盔甲匠')
            scared=r.randint(1,15)
            print(scared,'号被恐吓了，他今晚不能使用技能')
            if scared != 1:
                milk=int(input('今晚你免疫谁效果(1-15)?'))
                immnue(d)
            b=r.randint(1,15)
            dead()
            print(str(b)+'号死了')
        if '1' in farmer:
            print('你是农夫')
            scared=r.randint(1,15)
            print(scared,'号被恐吓了，他今晚不能使用技能')
            if scared != 1:
                j=input('你要禁票谁？')
            b=r.randint(1,15)
            print(b,'号死了')
            dead(str(b))
            areyouok=True
        if '1' in toolmaker:
            print('你是工具匠')
            scared=r.randint(1,15)
            print(scared,'号被恐吓了，他今晚不能使用技能')
            if scared != 1:
                gift=r.randint(1,5)
                if gift == 1:
                    b=input('今晚你获得了杀人技能,你要杀谁')
                    dead(b)
                if gift == 2:
                    c=input('今晚你获得了救人技能,你要救谁')
                    revive(c)
                if gift == 3:
                    d=input('今晚你获得了知晓身份技能,你要知晓谁')
                    realrole(d)
                    areyouok=True
                if gift == 4:
                    milk=input('今晚你获得了免疫技能,你要免疫谁')
                    immnue(milk)
                if gift == 5:
                    j=input('今晚你获得了禁票技能,你要禁谁')
        if '1' in overs:
            break
        if areyouok == False:
            j=r.randint(1,15)
        print(j,'号被禁票了')
        if '1' not in outs and '1' not in overs and 1 not in outs and 1 not in overs:
            print('天亮了，恭喜您又活了一天。')
            print('发言环节')
            gailyu=r.randint(1,3)
            if gailyu==3:
                fyr=monsters[r.randint(0,len(monsters)-1)]
                while fyr in overs:
                    fyr=monsters[r.randint(0,len(monsters)-1)]
            else:
                fyr=r.randint(2,15)
                while fyr in overs:
                    fyr=r.randint(2,15)
            print(str(fyr)+"号说：我是好人!")
            print(str(fyr)+"号说：投"+str(r.randint(1,15))+"号！")
            f=int(input('投票!'))
            if f <= 1 and f>=11:
                f='×'
            if str(f) in outs:
                print('你不能投死者,自动弃权')
                f='×'
            trials=[str(f)]
            for i in range(2,16):
                g=r.randint(1,17)
                if g > 15:
                    g=r.randint(1,len(monsters)-1)
                if g==i:
                    g=r.randint(1,15)
                    if str(g) in outs or g==i:
                        g='×'
                if i in outs:
                    g='×'
                if str(g) in outs:
                    g=r.randint(1,15)
                    if str(g) in outs or g==i:
                        g='×'
                if i == j:
                    g='×'
                trials.append(str(g))
            print('投票结果:')
            print('1    2    3    4    5    6    7    8    9    10    11    12    13    14    15')
            print(str(trials))
            while '×' in trials:
                trials.remove('×')
            h=collections.Counter(trials)
            j=max(h, key=lambda x: h[x])
            print('踢除'+str(j)+'号')
            d=int(j)
            realrole(d)
            b=int(j)
            dead(b)
            outs.append(j)
        print('好人还有'+str(len(villagers))+'人')
        print('怪物还有'+str(len(monsters))+'人')
        if len(monsters)>0:
            print('场上还有狼人')
        if len(villagers)<3:
            print('好人不足3个，狼人胜利！')
            print('你经历了'+str(nights)+'个晚上')
            if '1' in villagers:
                winnum+=1
                emerald+=5
            if '1' in monsters:
                losenum+=1
                emerald-=3
            break
        if len(monsters)<=0:
            print('怪物没了，好人胜利！')
            print('你经历了'+str(nights)+'个晚上')
            if '1' in villagers:
                break
            if '1' in monsters:
                break
        if '1'in outs:
            print("你失败了！")
            break
        if nights==7:
            print('你已经历了7个晚上，平局！')
            break
        if len(monsters)>0:
            print('开始下一个晚上……')
    print()
    print('   ----- The End -----')
    print('''作者:谢铭楷(脚臭楷)B站名:星流核心
    其他作品: Werewolf 2
       Dollars Duper!
    网站：https://m82.org''')
    print('原创，禁仿！敬请期待！')
    main()
def laws():
    print('''游戏规则：游戏有15人，分为2个阵营，分别是好人和怪物。
    好人9人，怪物6人。
    好人阵营有如下角色：普通村民3人，无特殊技能
    铁傀儡1人，每晚可以杀一人
    牧师1人，每晚可救一人
    盔甲匠1人，每晚可给一人免疫施加到他的所有技能，不管是杀还是救
    制图师1人，每晚可知晓一人身份
    农夫一人，每晚可指定一人第二天不能投票
    工具匠1人，每晚从杀、救、免疫、禁票随机获得一种技能使用
    怪物阵营：僵尸和骷髅各1人，每晚可和除女巫外所有怪物共杀一人
    苦力怕1人，除了和僵尸、骷髅一样的技能外，被杀/投出局前可带走1人
    女巫1人，每晚可从杀/救/免疫中选择一项使用
    蜘蛛1人，除了杀人技能外还可以恐吓1人，使其今晚不能使用技能
    末影人1人，除了杀人技能外，如果制图师知晓他的身份，制图师死。
    好人不足3个时怪物胜利
    怪物全死时好人胜利
    
    特别鸣谢:Mojang   安德鲁·普洛特金(苏联)
    
    本游戏还有不少进步空间，欢迎各位大佬指点！
    
    未经允许，严禁修改！
    ''')
    main()
def shop():
    print('当前胜局:',winnum,'当前败局:',losenum,'绿宝石:',emerald)
    print('商城功能尚未完善,商品敬请期待！\n')
    main()
def adminchanges():
    print("hello world 此瓜尚未调试")
    main()
main()
#version 3.1