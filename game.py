from PIL import ImageGrab,ImageOps,Image
from numpy.ma import array
import pyautogui,re,time,threading

positions=open('allpositions.txt')
bigbix=[]#用于存储位置
for line in positions.readlines():
    if re.search(r'\(.*?\)', line) is None:
        continue
    bigbix.append(eval(re.search(r'\(.*?\)',line).group()))

sushistyle={
    4057:'yuzijuan', #鱼子卷
    6952:'jialufu',#家路福
    5214:'zicaifantuan'#紫菜饭团
}

allfoodkinds= \
    {'shrimp':5,           #设定食材初始数量
       'rice':10,
        'nori':10,
        'roe':10,
        'salmon':5,
        'unagi':5}

boolen=[]#用于防止重复制做
for i in range(6):
    boolen.append(True)

repetition=[]#用于防止创建重复的线程
for j in range(6):
    repetition.append(False)

def makefood(food):
    if food=='yuzijuan':
        print('制作鱼子卷...')
        allfoodkinds['rice']-=1
        allfoodkinds['nori']-=1
        allfoodkinds['roe']-=2
        pyautogui.click(bigbix[1])
        time.sleep(0.5)
        pyautogui.click(bigbix[2])
        time.sleep(0.5)
        pyautogui.click(bigbix[3])
        time.sleep(0.5)
        pyautogui.click(bigbix[3])
        time.sleep(0.5)
        pyautogui.click(bigbix[6])
        time.sleep(1)

    elif food=='jialufu':
        print('制作加利福利亚卷...')
        allfoodkinds['rice']-=1
        allfoodkinds['nori']-=1
        allfoodkinds['roe']-=1
        pyautogui.click(bigbix[1])
        time.sleep(0.5)
        pyautogui.click(bigbix[2])
        time.sleep(0.5)
        pyautogui.click(bigbix[3])
        time.sleep(0.5)
        pyautogui.click(bigbix[6])
        time.sleep(1)

    elif food=='zicaifantuan':
        print('制作紫菜饭团...')
        allfoodkinds['rice']-=2
        allfoodkinds['nori']-=1
        pyautogui.click(bigbix[1])
        time.sleep(0.5)
        pyautogui.click(bigbix[1])
        time.sleep(0.5)
        pyautogui.click(bigbix[2])
        time.sleep(0.5)
        pyautogui.click(bigbix[6])
        time.sleep(1)

def get_onetable():
    box=bigbix[9]
    image=ImageOps.grayscale(ImageGrab.grab(box))
    a=array(image.getcolors())
    a=a.sum()
    return a

def clear_tables():#清理桌面
    pyautogui.click(bigbix[8])
    pyautogui.click(bigbix[10])
    pyautogui.click(bigbix[11])
    pyautogui.click(bigbix[12])
    pyautogui.click(bigbix[13])
    pyautogui.click(bigbix[14])


def get_seat_1():
    box=bigbix[15]
    image=ImageOps.grayscale(ImageGrab.grab(box))
    a=array(image.getcolors())
    a=a.sum()
    return a

def get_seat_2():
    box=bigbix[16]
    image=ImageOps.grayscale(ImageGrab.grab(box))
    a=array(image.getcolors())
    a=a.sum()
    return a

def get_seat_3():
    box=bigbix[17]
    image=ImageOps.grayscale(ImageGrab.grab(box))
    a=array(image.getcolors())
    a=a.sum()
    return a

def get_seat_4():
    box=bigbix[18]
    image=ImageOps.grayscale(ImageGrab.grab(box))
    a=array(image.getcolors())
    a=a.sum()
    return a

def get_seat_5():
    box=bigbix[19]
    image=ImageOps.grayscale(ImageGrab.grab(box))
    a=array(image.getcolors())
    a=a.sum()
    return a

def get_seat_6():
    box=bigbix[20]
    image=ImageOps.grayscale(ImageGrab.grab(box))
    a=array(image.getcolors())
    a=a.sum()
    return a

def buy_food(food):
    if food=='rice':
        pyautogui.click(bigbix[7],duration=0.5)
        time.sleep(0.5)
        pyautogui.click(bigbix[22],duration=0.5)
        time.sleep(0.5)
        pyautogui.click(bigbix[29],duration=0.5)
        time.sleep(0.5)
        pyautogui.click(bigbix[31], duration=0.5)
        allfoodkinds['rice']+=10
        time.sleep(1)

    if food=='nori':
        pyautogui.click(bigbix[7],duration=0.5)
        time.sleep(0.5)
        pyautogui.click(bigbix[21], duration=0.5)
        time.sleep(0.5)
        pyautogui.click(bigbix[26], duration=0.5)
        time.sleep(0.5)
        pyautogui.click(bigbix[31], duration=0.5)
        allfoodkinds['nori']+=10
        time.sleep(1)

    if food=='roe':
        pyautogui.click(bigbix[7],duration=0.5)
        time.sleep(0.5)
        pyautogui.click(bigbix[21], duration=0.5)
        time.sleep(0.5)
        pyautogui.click(bigbix[27], duration=0.5)
        time.sleep(0.5)
        pyautogui.click(bigbix[31], duration=0.5)
        allfoodkinds['roe']+=10
        time.sleep(1)

def check_food():
    for i,j in allfoodkinds.items():
        if i=='rice' or i=='nori' or i=='roe':
            if j<=3:
                print('购买%s中'%i)
                buy_food(i)
                print('购买完成')

def changetotrue(i):#为该顾客制作后一定时间不在制作
    time.sleep(14)
    repetition[i]=False
    boolen[i] = True

def runsleep():
    global boolen,repetition
    for i in range(6):
        if len(threading.enumerate())>6:
            continue
        if boolen[i]==False and repetition[i]==False:
            repetition[i]=True
            threading.Thread(target=changetotrue,args=(i,)).start()

def check_seat():
    s1=get_seat_1()
    if s1 in sushistyle.keys() and boolen[0]==True:
        check_food()
        makefood(sushistyle[s1])#制作食物
        boolen[0]=False
    clear_tables()

    s2 = get_seat_2()
    if s2 in sushistyle.keys() and boolen[1]==True:
        check_food()
        makefood(sushistyle[s2])
        boolen[1] = False

    s3 = get_seat_3()
    if s3 in sushistyle.keys() and boolen[2]==True:
        check_food()
        makefood(sushistyle[s3])
        boolen[2] = False
    clear_tables()

    s4=get_seat_4()
    if s4 in sushistyle.keys() and boolen[3]==True:
        check_food()
        makefood(sushistyle[s4])
        boolen[3] = False

    s5 = get_seat_5()
    if s5 in sushistyle.keys() and boolen[4]==True:
        check_food()
        makefood(sushistyle[s5])
        boolen[4] = False
    clear_tables()

    s6 = get_seat_6()
    if s6 in sushistyle.keys() and boolen[5]==True:
        check_food()
        makefood(sushistyle[s6])
        boolen[5] = False

def allthreads():
    check_seat()
    runsleep()

onetalble=[4845,3245]
def startgame():
    while True:
        if get_onetable() not in onetalble:
            print('退出')
            break
        allthreads()

if __name__ == '__main__':
    startgame()
