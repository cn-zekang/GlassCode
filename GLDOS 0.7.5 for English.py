

import time

print("Welcome to", 'Glass', 'DOS', 'Operating System', ' 0.7.5') #Welcome to GLASS DOS Operating System (Glass Disk Operating System)
dir = 'dir' #Define the command
openglassdos = 'open glassdos' #Define the command
omn = 'omn' #Define the command
shutdown = 'shutdown' #Define the command
help = 'help' #Define the command
openglassdosmods = 'open glassdos/mods' #Define the command
Calculator = 'calculator' #Define the command
restart = 'restart' #Define the command
timing = 'timing' #Define the command
timer = 'timer' #Define the command
run = 5 #Define the run function
a = '*' #Defines an operator symbol function
b = '/' #Defines an operator symbol function
c = '-' #Defines an operator symbol function
d = '+' #Defines an operator symbol function
e = '^' #Defines an operator symbol function
while run >= 2: #Loop the operating system
    output = input("HD ~ $:")
    if output == dir:
        print('1 ' 'Folder ' 'And ' '5 ' 'File ')
        print('Folder ' 'Name is a ' 'glassdos ')
        print('No.1~No.5 ' 'Files ' 'Name is''a ''BOOT1~BOOT5 ' 'Suffix ' 'Name ' 'is ' 'a ' '.BOT')  # Accept the dir command and execute it
    elif output == openglassdos:
        print('3', 'Files', '1', 'Folder')
        print('No.1', 'File', 'Name is a', 'Command', 'Suffix', 'Name is a ', '.ode')
        print('No.2', 'File','Name is', 'a','I/O', 'Suffix', 'Name is', '.ode')
        print('No.3','File','Name is','a','Help','Suffix','Name is','a','.ode')
        print('No.1','Folder','Name','is','a','mods')  # Accept the open glass dos command and execute it
    elif output == omn:
        print("     Glass Computer Glass DOS 0.7.5")
        print("        Input   ", "  Command")  # Accept the omn command and execute it
    elif output == shutdown:
        print("Shut downing......")  # Accept the shutdown command and execute it
        exit()  # Perform a shutdown operation
    elif output == help:
        print('dir is a showcase of files and folders in HD')
        print('open glassdos are files and folders that display system folders')
        print('omn is a version of the display glass operating system')
        print('shutdown is shutdown')
        print('help is help')
        print('open glassdos/mods is the option folder that opens the system folder and displays the files and folders in the modes folder')
        print('Restart is an Easter egg')
        print("timing is a countdown timer")
        print("timer is a timer, when the timer is running, enter qt to exit the timer, but the timer has a bug that must always hit the Enter key to timer")
        print('calculator is the calculator')
        print('usage:')
        print('The first Enter the number before the operator symbol appears after entering the number before the operator symbol')
        print('The second Enter an operator symbol appears after entering the operator symbol')
        print('The third Counts into the number after the operator symbol appears, enter the number after the operator symbol.') # Accept the help command and execute it
    elif output == openglassdosmods:
        print("3",'File','0','Folder')
        print('NO.1','File','Name','is','a','Calculator','Suffix','Name','is','a','.mod')
        print('NO.2','File','Name','is','a','Timing','Suffix','Name','is','a','.mod')
        print('NO.3','File','Name','is','a','Timer','Suffix','Name','is','a','.mod') # Accept the open glassdos/mods command and execute it
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
            print(float(A) ^ float(C)) #Accept the calculator command and execute it
    elif output == restart:
            print('    EEEEEEEEEEE          _RRRRRRRRRRRRR_         _RRRRRRRRRRRRR_    _OOOOOOOOOOO_     _RRRRRRRRRRRRR_')
            print('    E                    R             R         R             R   O             O    R             R')
            print('    EEEEEEEEEEE          RRRRRRRRRRRRRR          RRRRRRRRRRRRRR    O             O    RRRRRRRRRRRRRR')
            print('    EEEEEEEEEEE          RR  RR                  RR  RR            O             O    RR  RR')
            print('    E                    RR    RR                RR    RR          O             O    RR    RR')
            print('    EEEEEEEEEEE          RR      RRR             RR      RRR        OOOOOOOOOOOOO     RR      RRR') #Accept the restart command and execute it
    elif output == timing:
        output = int(input('InputTime!:'))
        print("OK",'Timing',output)
        Time_left = int(output)
        while Time_left > 0:
            print('Timing(s):', int(Time_left))
            time.sleep(1)
            Time_left = Time_left - 1 #Accept the timing command and execute it
    elif output == timer:
        print("OK",'Timer')
        timers = 0
        while True:
            print('Timer(s):',int(timers))
            time.sleep(1)
            timers = timers + 1
            qt = 'qt'
            output = input()
            if output == qt:
                break #接受 timer 命令并执行
    else:
        print("Input command")  #Prompt the user for a command
