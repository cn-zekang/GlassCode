"""Corporation GlassComputer CO Ltd."""

import time

print('User?')
output = input('admin ~ USER $:')
ad = 'admin'
if output == ad:
    print("欢迎来到", 'Glass', 'DOS', '系统', ' 0.8.1')  # 欢迎进入 GLASS DOS 操作系统(玻璃磁盘操作系统)
    dir = 'dir'  # 定义命令
    openglassdos = 'open glassdos'  # 定义命令
    com = 'com'  # 定义命令
    shutdown = 'shutdown'  # 定义命令
    help = 'help'  # 定义命令
    openglassdosmods = 'open glassdos/mods'  # 定义命令
    Calculator = 'calculator'  # 定义命令
    restart = 'restart'  # 定义命令
    timing = 'timing'  # 定义命令
    timer = 'timer'  # 定义命令
    reciter = 'reciter'  # 定义命令
    a = '*'  # 定义运算符号函数
    b = '/'  # 定义运算符号函数
    c = '-'  # 定义运算符号函数
    d = '+'  # 定义运算符号函数
    e = '^'  # 定义运算符号函数
    while True:  # 循环操作系统
        output = input("HD ~ administrator $:")
        if output == dir:
            print('1 ' 'Folder ' 'And ' '5 ' 'File ')
            print('Folder ' 'Name is a ' 'glassdos ''No.1~No.5 ')
            print('Files ' 'Name is''a ''BOOT1~BOOT5 ' 'Suffix ' 'Name ' 'is ' 'a ' '.BOT')  # 接受 dir 命令并执行
        elif output == openglassdos:
            print('3', 'Files', '1', 'Folder')
            print('No.1', 'File', 'Name is a', 'Command', 'Suffix', 'Name is a ', '.ode')
            print('No.2', 'File', 'Name is', 'a', 'I/O', 'Suffix', 'Name is', '.ode')
            print('No.3', 'File', 'Name is', 'a', 'Help', 'Suffix', 'Name is', 'a', '.ode')
            print('No.1', 'Folder', 'Name', 'is', 'a', 'mods')  # 接受 open glass dos 命令并执行
        elif output == com:
            print("     Glass Computer Glass DOS 0.8.1")
            print("           Input   ", "  Command")
            print("    Corporation GlassComputer CO Ltd.")  # 接受 omn 命令并执行
        elif output == shutdown:
            print("Shut downing......")  # 接受 shutdown 命令并执行
            exit()  # 执行关机操作
        elif output == help:
            print('dir是展示HD中的文件和文件夹')
            print('open glassdos是展示系统文件夹里的文件和文件夹')
            print('omn是显示玻璃操作系统的版本')
            print('shutdown是关机')
            print('help是帮助')
            print('open glassdos/mods是打开系统文件夹里的mods文件夹并显示mods文件夹里的文件和文件夹')
            print('restart是彩蛋')
            print("timing是倒计时器")
            print("timer是计时器，在计时器运行中时输入qt可以退出计时器,但是计时器有BUG必需一直点击Enter键才可以计时")
            print('calculator是计算器')
            print('reciter是背诵器')
            print('用法：')
            print('第一个Enter the number before the operator symbol出现后输入运算符号前面的数，')
            print('第二个Enter an operator symbol出现后输入运算符号，')
            print('第三个Counts into the number after the operator symbol出现后输入运算符号后面的数。')  # 接受help命令并执行
        elif output == openglassdosmods:
            print("3", 'File', '0', 'Folder')
            print('NO.1', 'File', 'Name', 'is', 'a', 'Calculator', 'Suffix', 'Name', 'is', 'a', '.mod')
            print('NO.2', 'File', 'Name', 'is', 'a', 'Timing', 'Suffix', 'Name', 'is', 'a', '.mod')
            print('NO.3', 'File', 'Name', 'is', 'a', 'Timer', 'Suffix', 'Name', 'is', 'a',
                  '.mod')  # 接受open glassdos/mods 命令并执行
        elif output == Calculator:
            print("Calculator 0.9.0")
            output = input("Enter the number before the operator symbol:")
            A = output
            output = input("Enter an operator symbol:")
            B = output
            output = input("Counts into the number after the operator symbol:")
            C = output
            if B == a:
                print(float(A) * float(C))
            if B == b:
                print(float(A) / float(C))
            if B == c:
                print(float(A) - float(C))
            if B == d:
                print(float(A) + float(C))
            if B == e:
                print(float(A) ^ float(C))  # 接受calculator命令并执行
        elif output == restart:
            print('    EEEEEEEEEEE          _RRRRRRRRRRRRR_         _RRRRRRRRRRRRR_    _OOOOOOOOOOO_     _RRRRRRRRRRRRR_')
            print('    E                    R             R         R             R   O             O    R             R')
            print('    EEEEEEEEEEE          RRRRRRRRRRRRRR          RRRRRRRRRRRRRR    O             O    RRRRRRRRRRRRRR')
            print('    EEEEEEEEEEE          RR  RR                  RR  RR            O             O    RR  RR')
            print('    E                    RR    RR                RR    RR          O             O    RR    RR')
            print('    EEEEEEEEEEE          RR      RRR             RR      RRR        OOOOOOOOOOOOO     RR      RRR')  # 接受 restart 命令并执行
        elif output == timing:
            output = int(input('InputTime!:'))
            print("OK", 'Timing', output)
            Time_left = int(output)
            while Time_left > 0:
                print('Timing(s):', int(Time_left))
                time.sleep(1)
                Time_left = Time_left - 1  # 接受 timing 命令并执行
        elif output == timer:
            print("OK", 'Timer')
            timers = 0
            while True:
                print('Timer(s):', int(timers))
                time.sleep(1)
                timers = timers + 1
                qt = 'qt'
                output = input()
                if output == qt:
                    break  # 接受 timer 命令并执行
        elif output == reciter:
            citer = ['江畔独步寻花']
            print(citer)
            output = input('输入你想背诵的诗的名字:')
            if output == citer[0]:
                fir = input("第一句：")
                no1 = '黄师塔前江水东'
                no2 = '春光懒困倚微风'
                no3 = '桃花一簇开无主'
                no4 = '可爱深红爱浅红'
                if fir == no1:
                    print('No1:Win!')
                sec = input("第二句：")
                if sec == no2:
                    print('No2:Win!')
                third = input("第三句：")
                if third == no3:
                    print('No3:Win!')
                th4 = input("第四句：")
                if th4 == no4:
                    print('Your Win!')
                else:
                    print('Loser')
        else:
            print("The Your Input a Command without")  # 提示用户输入命令
            print('Command Error: Your Input a without Command')
            print('你输入的代码有问题！')
            print('代码 错误：你输入的代码有问题！')
            print('コマンドを入力しない')
            print('コマンド エラー: コマンドなしの入力')
            print('您的輸入命令沒有')
            print('命令錯誤：您的輸入沒有命令')   #验证是否是主人 是：进入操作系统 否：关机
else:
    print('Shut downing......')
    exit()