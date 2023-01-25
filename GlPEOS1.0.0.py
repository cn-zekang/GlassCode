"""Corporation GlassComputer Studio"""

"""
此系统正在更新中。

GOS进化史：
2020：
0.0.1初版
功能：复读机
0.1.0汉化一版
功能简单，不足为奇
0.2.0汉化二版
功能简单，但是已有雏形
2021：
0.3.0-0.7.0汉化三版
功能中等，称赞连连
0.8.0英文一版
功能中等，称赞连连
2022：
0.9.0汉化四版
功能高级，好评如潮
2023：
1.0.0正式汉化一版
功能完整：非常舒服

"""

import time


def Log():
    file = open(r"E:\GlassOS\GlassCode-main\GlassCode-main\Log.txt", "w", encoding="utf-8")

    True_log = "Log" + """
System self-test: successful

Code filling: successful
Hardware detection: successful

Error code: 0x00000000 No error
Update error: 0x0000007b memory bit occupation not ended

Update hardware: USB flash drive
Update hardware: USB flash memory launched

System change: shutdown
    """

    file.write(True_log)
    file.close()


Log()


def system_start():
    try:
        f = open('disposition.txt')
        a = f.read()
        print(a)
        print('Self-test: OK\n')
        f.close()
    except IOError:
        f = open('disposition.txt', 'w')
        output = input('CPU :')
        f.write('GLASS COMPUTER start ui\n')
        f.write('CPU :' + str(output) + '\n')
        output = input('RAM :')
        f.write('RAM :' + str(output) + '\n')
        output = input('ROM :')
        f.write('ROM :' + str(output) + '\n')
        output = input('Graphics Card :')
        f.write('Graphics Card :' + str(output) + '\n')
        f.close()
        print('OK,restart you computer.')
        exit()
    print('User——password?')
    output = input('admin ~ USER $:')
    if output == '12345':
        print("欢迎来到", 'Glass', 'PythonEmbeddedOperatingSystem', '系统',
              ' 1.0.0')  # 欢迎进入 GLASS PythonEmbeddedOperatingSystem 操作系统(玻璃Python嵌入式操作系统)
        while True:  # 循环操作系统
            output = input("HD ~ administrator $:")
            if output == 'dir':
                print('1 ' 'Folder ' 'And ' '5 ' 'File\n'
                      'Folder ' 'Name is a ' 'glasspeos ''No.1~No.5 \n'
                      'Files ' 'Name is ' 'a ' 'BOOT1~BOOT5 ' 'Suffix ' 'Name ' 'is ' 'a ' '.BOT')  # 接受 dir 命令并执行
            elif output == 'open glasspeos':
                print('3', 'Files', '1', 'Folder\n'
                                         'No.1', 'File', 'Name is a', 'Command', 'Suffix', 'Name is a ', '.ode\n'
                                                                                                         'No.2', 'File',
                      'Name is', 'a', 'I/O', 'Suffix', 'Name is', '.ode\n'
                                                                  'No.3', 'File', 'Name is', 'a', 'Help', 'Suffix',
                      'Name is', 'a', '.ode'
                                      'No.1', 'Folder', 'Name', 'is', 'a', 'mods')  # 接受 open glass dos 命令并执行
            elif output == 'ver':
                print("     Glass Computer Glass PythonEmbeddedOperatingSystem 0.9.0\n"
                      "           Input   ", "  Command\n"
                                             "    Corporation GlassComputer Studio")  # 接受 omn 命令并执行
            elif output == 'shutdown':
                print("Shut downing......")  # 接受 shutdown 命令并执行
                exit()  # 执行关机操作
            elif output == 'help':
                print(
                    'dir是展示HD中的文件和文件夹\n'
                    'open glasspeos是展示系统文件夹里的文件和文件夹\n'
                    'ver是显示玻璃操作系统的版本\n'
                    'shutdown是关机\n'
                    'help是帮助\n'
                    'open glassdos/mods是打开系统文件夹里的mods文件夹并显示mods文件夹里的文件和文件夹\n'
                    'restart是彩蛋\n'
                    "timing是倒计时器\n"
                    "timer是计时器，在计时器运行中时输入qt可以退出计时器,但是计时器有BUG必需一直点击Enter键才可以计时\n"
                    'reciter是背诵器\n'
                    'calculator是计算器\n'
                    '用法：\n'
                    '第一个Enter the number before the operator symbol出现后输入运算符号前面的数，\n'
                    '第二个Enter an operator symbol出现后输入运算符号，\n'
                    '第三个Counts into the number after the operator symbol出现后输入运算符号后面的数。\n'
                    'readLog是阅读日志'
                    'newfile是创建文件')  # 接受help命令并执行
            elif output == 'open glasspeos/mods':
                print("3", 'File', '0', 'Folder\n'
                                        'NO.1', 'File', 'Name', 'is', 'a', 'Calculator', 'Suffix', 'Name', 'is', 'a',
                      '.mod\n' 'NO.2', 'File', 'Name', 'is', 'a', 'Timing', 'Suffix', 'Name', 'is', 'a',
                      '.mod\n' 'NO.3', 'File', 'Name', 'is', 'a', 'Timer', 'Suffix', 'Name', 'is', 'a',
                      '.mod')  # 接受open glassdos/mods 命令并执行
            elif output == 'calculator':
                print("Calculator 0.9.0")
                output = input("Enter the number before the operator symbol:")
                A = output
                output = input("Enter an operator symbol:")
                B = output
                output = input("Counts into the number after the operator symbol:")
                C = output
                if B == '*':
                    print(float(A) * float(C))
                if B == '/':
                    print(float(A) / float(C))
                if B == '-':
                    print(float(A) - float(C))
                if B == '+':
                    print(float(A) + float(C))
                if B == '^':
                    print(float(A) ** float(C))  # 接受calculator命令并执行
            elif output == 'restart':
                print(
                    '    EEEEEEEEEEE          _RRRRRRRRRRRRR_         _RRRRRRRRRRRRR_    _OOOOOOOOOOO_     _RRRRRRRRRRRRR_\n'
                    '    E                    R             R         R             R   O             O    R             R\n'
                    '    EEEEEEEEEEE          RRRRRRRRRRRRRR          RRRRRRRRRRRRRR    O             O    RRRRRRRRRRRRRR\n'
                    '    EEEEEEEEEEE          RR  RR                  RR  RR            O             O    RR  RR\n'
                    '    E                    RR    RR                RR    RR          O             O    RR    RR\n'
                    '    EEEEEEEEEEE          RR      RRR             RR      RRR        OOOOOOOOOOOOO     RR      RRR')  # 接受 restart 命令并执行
            elif output == 'timing':
                output = int(input('InputTime!:'))
                print("OK", 'Timing', output)
                Time_left = int(output)
                while Time_left > 0:
                    print('Timing(s):', int(Time_left))
                    time.sleep(1)
                    Time_left = Time_left - 1  # 接受 timing 命令并执行
            elif output == 'timer':
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
            elif output == 'reciter':
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
            elif output == 'readLog':
                file = open(r'E:\GlassOS\GlassCode-main\GlassCode-main\Log.txt', 'r', encoding='utf-8')
                e = file.read()
                print(e, 'Today log in this file,Please not write.')
            elif output == 'newfile':
                output = input('此时是只读模式，请输入您创建过的文本文档的名字，不用填后缀名(如果不需要，请输入Log)：')
                p = open('E:\GlassOS\GlassCode-main\GlassCode-main\%s.txt' % output, 'r', encoding='utf-8')
                f = p.read()
                print(f)
                outpute = input('输入想创建的TXT文本文档名称：')
                r = open('E:\GlassOS\GlassCode-main\GlassCode-main\%s.txt' % outpute, 'w', encoding='utf-8')
                output = input('输入您想写入的内容，且会自动改为追加模式：')
                r.write(output)
                r.close()
                k = open('E:\GlassOS\GlassCode-main\GlassCode-main\%s.txt' % outpute, 'a', encoding='utf-8')
                while True:
                    output = input('追加您刚刚创建的文本文档(qt退出)：')
                    if output == 'qt':
                        break
                    k.write(output)
            else:
                print(
                    "The Your Input a Command without\n"
                    'Command Error: Your Input a without Command\n'
                    '你输入的代码有问题！\n'
                    '代码 错误：你输入的代码有问题！\n'
                    'コマンドを入力しない\n'
                    'コマンド エラー: コマンドなしの入力\n'
                    '您的輸入命令沒有\n'
                    '命令錯誤：您的輸入沒有命令')  # 提示用户输入命令
    else:
        print('Shut downing......')
        exit()  # 验证是否是用户 是：进入操作系统 否：关机


system_start()
