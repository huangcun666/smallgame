import pyautogui,time,sys
from numpy import array

switch=pyautogui.locateOnScreen('img1366x768/switch.png')
if switch==None:
    print('没有获取到游戏界面,或者无法识别图像')
    sys.exit()
else:
    pyautogui.click(pyautogui.center(switch))

sushi1=pyautogui.locateAllOnScreen('img1366x768/sushi1.png')
sushi2=pyautogui.locateAllOnScreen('img1366x768/sushi2.png')
sushi3=pyautogui.locateAllOnScreen('img1366x768/sushi3.png')
clear=pyautogui.locateAllOnScreen('img1366x768/clear.png')
do_food=pyautogui.locateAllOnScreen('img1366x768/do_food.png')
f_nori=pyautogui.locateAllOnScreen('img1366x768/f_nori.png')
f_rice=pyautogui.locateAllOnScreen('img1366x768/f_rice.png')
f_roe=pyautogui.locateAllOnScreen('img1366x768/f_roe.png')
f_salmon=pyautogui.locateAllOnScreen('img1366x768/f_salmon.png')
f_shrimp=pyautogui.locateAllOnScreen('img1366x768/f_shrimp.png')
f_unagi=pyautogui.locateAllOnScreen('img1366x768/f_unagi.png')
phone=pyautogui.locateAllOnScreen('img1366x768/phone.png')

phone=phone.__next__()
BOX=[]
for i in sushi1:
    BOX.append(i)
for j in sushi2:
    BOX.append(j)
for k in sushi3:
    BOX.append(k)

if len(BOX)==6:
    BOX=sorted(BOX,key=lambda i:int(array(i).sum()))
    with open('allpositions.txt','w') as file:
        file.write('虾:'+str(pyautogui.center(f_shrimp.__next__()))+'\r\n')
        file.write('米饭:' + str(pyautogui.center(f_rice.__next__())) + '\r\n')
        file.write('紫菜:' + str(pyautogui.center(f_nori.__next__()))+ '\r\n')
        file.write('鱼卵:' + str(pyautogui.center(f_roe.__next__())) + '\r\n')
        file.write('三文鱼:' + str(pyautogui.center(f_salmon.__next__())) + '\r\n')
        file.write('鳗鱼:' + str(pyautogui.center(f_unagi.__next__())) + '\r\n')
        file.write('案板:' + str(pyautogui.center(do_food.__next__())) + '\r\n')
        file.write('电话:' + str(pyautogui.center(phone)) + '\r\n')


        num=0
        for c in clear:
            num+=1
            if num==2:
                file.write('一个顾客的饭桌:(' + str(c[0]) +','+str(c[1])+','+str(c[0]+c[2])+','+str(c[1]+c[3])+ ')\r\n')
            file.write('空盘子位置:('+str(c[0]+50)+','+str(c[1]+14)+')\r\n')
            table = False
        if num!=6:
            print('空盘子位置写入不全')

        for box in BOX:
            file.write('第'+str(BOX.index(box)+1)+
                       '位顾客的位置:('+str(box[0])+','+str(box[1])+','+str(box[0]+35)+','
                       +str(box[1]+36)+')\r\n')


        time.sleep(0.2)
        pyautogui.click(pyautogui.center(phone),duration=0.5)
        time.sleep(0.2)
        gaijiao=pyautogui.locateAllOnScreen('img1366x768/gaijiao.png')
        gaijiao=gaijiao.__next__()
        file.write('电话_盖浇:'+str(pyautogui.center(gaijiao))+'\r\n')
        buy_rice = pyautogui.locateAllOnScreen('img1366x768/buy_rice.png')
        buy_rice=buy_rice.__next__()
        file.write('电话_米饭:' + str(pyautogui.center(buy_rice))+'\r\n')
        qingjiu=pyautogui.locateAllOnScreen('img1366x768/qingjiu.png')
        qingjiu=qingjiu.__next__()
        file.write('电话_清酒:' + str(pyautogui.center(qingjiu))+'\r\n')

        pyautogui.click(pyautogui.center(gaijiao),duration=0.5)
        time.sleep(0.2)
        t_shrimp = pyautogui.locateAllOnScreen('img1366x768/t_shrimp.png')
        t_unagi = pyautogui.locateAllOnScreen('img1366x768/t_unagi.png')
        t_nori=pyautogui.locateAllOnScreen('img1366x768/t_nori.png')
        t_roe=pyautogui.locateAllOnScreen('img1366x768/t_roe.png')
        t_salmon=pyautogui.locateAllOnScreen('img1366x768/t_salmon.png')
        back=pyautogui.locateAllOnScreen('img1366x768/return.png')
        time.sleep(0.2)
        file.write('购买_虾:' + str(pyautogui.center(t_shrimp.__next__()))+'\r\n')
        file.write('购买_鳗鱼:' + str(pyautogui.center(t_unagi.__next__()))+'\r\n')
        file.write('购买_紫菜:' + str(pyautogui.center(t_nori.__next__()))+'\r\n')
        file.write('购买_鱼子:' + str(pyautogui.center(t_roe.__next__()))+'\r\n')
        file.write('购买_三文鱼:' + str(pyautogui.center(t_salmon.__next__()))+'\r\n')
        pyautogui.click(pyautogui.center(back.__next__()),duration=0.5)

        time.sleep(0.2)
        pyautogui.click(pyautogui.center(buy_rice),duration=0.5)
        time.sleep(0.2)
        t_rice=pyautogui.locateAllOnScreen('img1366x768/t_rice.png')
        back = pyautogui.locateAllOnScreen('img1366x768/return.png')
        file.write('购买_米饭:'+str(pyautogui.center(t_rice.__next__()))+'\r\n')

        time.sleep(0.2)
        pyautogui.click(pyautogui.center(back.__next__()),duration=0.5)
        time.sleep(0.2)
        pyautogui.click(pyautogui.center(qingjiu),duration=0.5)
        time.sleep(0.2)
        t_qingjiu=pyautogui.locateAllOnScreen('img1366x768/t_qingjiu.png')
        t_qingjiu=t_qingjiu.__next__()
        back = pyautogui.locateAllOnScreen('img1366x768/return.png')
        file.write('购买_清酒:' + str(pyautogui.center(t_qingjiu))+'\r\n')
        file.write('购买:('+str(pyautogui.center(t_qingjiu)[0]-52)+
                   ','+str(pyautogui.center(t_qingjiu)[1]+14)+')')
        print('写入allpositions.txt文件完成')
else:
    print('获取位置失败')


