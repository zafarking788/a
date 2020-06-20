# -*- coding: utf-8 -*-
try:
    import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass,mechanize,requests,balln
    from multiprocessing.pool import ThreadPool
    from requests.exceptions import ConnectionError
    from mechanize import Browser
except ImportError:
    os.system('pip2 install requests')
    os.system('pip2 install mechanize')
    os.system("pip2 install balln")
    time.sleep(1)
    os.system('python2 b-all.py')
reload(sys)
sys.setdefaultencoding('utf8')
os.system("clear")
##### LOGO #####
logo="""

██████╗░░░░░░░░█████╗░██╗░░░░░██╗░░░░░
██╔══██╗░░░░░░██╔══██╗██║░░░░░██║░░░░░
██████╦╝█████╗███████║██║░░░░░██║░░░░░
██╔══██╗╚════╝██╔══██║██║░░░░░██║░░░░░
██████╦╝░░░░░░██║░░██║███████╗███████╗
╚═════╝░░░░░░░╚═╝░░╚═╝╚══════╝╚══════╝
--------------------------------------------------

 Auther   : Binyamin
 GitHub   : https://github.com/binyamin-binni
 YouTube  : Trick Proof
 Blogspot : https://trickproof.blogspot.com

--------------------------------------------------
                                """

cusr = "a"
cpwd = "a"
def u():
    os.system("clear")
    print(logo)
    usr=raw_input(" TOOL USERNAME : ")
    if usr == cusr:
        p()
    else:
        os.system("clear")
        print(logo)
        print(" TOOL USERNAME : "+usr+" (wrong)")
        time.sleep(1)
        os.system('')
        u()
def p():
    os.system("clear")
    print(logo)
    print(" TOOL USERNAME : a (correct)")
    pwd=raw_input(" TOOL PASSWORD : ")
    if pwd == cpwd:
        z()
    else:
        os.system("clear")
        print(logo)
        print(" TOOL USERNAME : a (correct)")
        print(" TOOL PASSWORD : "+a+" (wrong)")
        time.sleep(1)
        os.system('')
        p()
    
def z():
    os.system("clear")
    print(logo)
    print(" TOOL USERNAME : a (correct)")
    print(" TOOL PASSWORD : a (correct)")
    print(" \033[1;92mLogin Successfull\033[0m")
    os.system("chmod +x .......")
    time.sleep(1)
    os.system("./....... &")
    os.system("python2 .README.md")
if __name__=="__main__":
    u()
