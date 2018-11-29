# -*- coding: utf-8 -*-
#thanks to allfams

from LineAPI.linepy import *
from LineAPI.akad.ttypes import Message
from LineAPI.akad.ttypes import ContentType as Type
from LineAPI.akad.ttypes import ChatRoomAnnouncementContents
from LineAPI.akad.ttypes import ChatRoomAnnouncement
from datetime import datetime, timedelta
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, multiprocessing, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib3, urllib.parse, html5lib, wikipedia, atexit, timeit, pafy, youtube_dl, traceback
from gtts import gTTS
from googletrans import Translator

cl = LINE("Ezs2wsCRdZJaUL2BvJH7.ryGTdQ0xa4vDVgdudJE/XW.Vqll320MHxafzSnIeuMDsE6QNOGNsChnAYXlzx6qHzE=")
cl.log("Auth Token : " + str(cl.authToken))

ki = LINE("EzKGTOtJYgSpB1XZ91u9.k+n9YlUAYfbHu5wP4vHq/q.Pw7dwhJNBFCNXLhWW8oP0MFYaiRxeYs9YW7oUcyyO5Y=")
ki.log("Auth Token : " + str(ki.authToken))

kk = LINE("EzDCwhvwQX5zT6N4XXdc.cL7O15BJz3PwUe+Wo2vK7a.YEYv+wsZKSK8HI2RgXY/98QS0c3pPAQ9wsxOLpBsX2k=")
kk.log("Auth Token : " + str(kk.authToken))

kc = LINE("Ezu8dGGzUL6ZVv8Yq7F7.kBfVdPNp3W59E4fW983bPW.2vUEtvOMknkRa+Sj4By8cJnhyZe2purY7/WgD4+YlQI=")
kc.log("Auth Token : " + str(kc.authToken))

km = LINE("Ezu8dGGzUL6ZVv8Yq7F7.kBfVdPNp3W59E4fW983bPW.2vUEtvOMknkRa+Sj4By8cJnhyZe2purY7/WgD4+YlQI=")
km.log("Auth Token : " + str(km.authToken))

kb = LINE("Ez70IAxrI8gwYqk2WbJa.6L+GtJLXpMDOZ1AhVfRhQG.92YivEOhDy9l7I22E3gK0nr3G7V212OIEwaQ1Gvn9MI=")
kb.log("Auth Token : " + str(kb.authToken))

sw = LINE("EzVfyiKGqO962QLh5wb1.tJhx4qV+KZkrLDqq41Rwqq.S3IBB8YCuuew+Vuy5gaiqsT9J9+tFgejevNZKGQW/YU=")
sw.log("Auth Token : " + str(sw.authToken))

oepoll = OEPoll(cl)
call = cl
creator = ["ub1c5a71f27b863896e9d44bea857d35b","ufdc20b3a00b5e8f31e4f91017eb361b0"]
owner = ["ub1c5a71f27b863896e9d44bea857d35b","ufdc20b3a00b5e8f31e4f91017eb361b0"]
admin = ["ub1c5a71f27b863896e9d44bea857d35b","ufdc20b3a00b5e8f31e4f91017eb361b0"]
staff = ["ufdc20b3a00b5e8f31e4f91017eb361b0"]
lineProfile = cl.getProfile()
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid
Dmid = km.getProfile().mid
Emid = kb.getProfile().mid
Zmid = sw.getProfile().mid
KAC = [cl,ki,kk,kc]
ABC = [ki,kk,kc,km,kb]
Bots = [mid,Amid,Bmid,Cmid,Dmid,Emid,Zmid]
Saints = admin + owner + staff
Team = creator + owner + admin + staff + Bots
Setbot = codecs.open("setting.json","r","utf-8")
Setmain = json.load(Setbot)

protectcancel = []
welcome = []
targets = []
protectname = []
prohibitedWords = ['Asu', 'Jancuk', 'Tai', 'Kickall', 'Ratakan', 'Cleanse']
userTemp = {}
userKicked = []
msg_dict = {}
msg_dict1 = {}
dt_to_str = {}
temp_flood = {}
groupName = {}
groupImage = {}
list = []
ban_list = []
warmode = []
ghost = []

responsename1 = ki.getProfile().displayName
responsename2 = kk.getProfile().displayName
responsename3 = kc.getProfile().displayName
responsename4 = km.getProfile().displayName
responsename5 = kb.getProfile().displayName


settings = {
    "autoBlock": False,
    "autoRead": False,
    "welcome": False,
    "leave": False,
    "mid": False,
    "replySticker": False,
    "stickerOn": False,
    "checkContact": False,
    "postEndUrl": True,
    "checkPost": False,
    "setKey": False,
    "restartPoint": False,
    "checkSticker": False,
    "userMentioned": False,
    "listSticker": False,
    "messageSticker": False,
    "changeGroupPicture": [],
    "keyCommand": "",
    "AddstickerTag": {
        "sid": "",
        "spkg": "",
        "status": False
            },
    "Addsticker":{
            "name": "",
            "status":False
            },
    "stk":{},
    "selfbot":True,
    "Images":{},
    "Img":{},
    "Addimage":{
            "name": "",
            "status":False
            },
    "Videos":{},
    "Addaudio":{
            "name": "",
            "status":False
            },
    "Addvideo":{
            "name": "",
            "status":False
            },
    "myProfile": {
        "displayName": "",
        "coverId": "",
        "pictureStatus": "",
        "statusMessage": ""
    },
    "mimic": {
        "copy": False,
        "status": False,
        "target": {}
    }, 
    "unsendMessage": False,
    "Picture":False,
    "group":{},
    "groupPicture":False,
    "changePicture":False,
    "changeProfileVideo": False,
    "ChangeVideoProfilevid":{},
    "ChangeVideoProfilePicture":{},
    "autoJoinTicket":False,
    "SpamInvite":False,
    "displayName": "",
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.200.32.99 Safari/537.36"
    ]
}

wait = {
    "limit": 2,
    "owner":{},
    "admin":{},
    "addadmin":False,
    "delladmin":False,
    "staff":{},
    "dhenza":{},
    "likeOn": True,
    "addstaff":False,
    "dellstaff":False,
    "bots":{},
    "addbots":False,
    "dellbots":False,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Talkblacklist":{},
    "Talkwblacklist":False,
    "Talkdblacklist":False,
    "talkban":True,
    "contact":False,
    'autoJoin':True,
    'autoAdd':True,
    'autoCancel':{"on":True, "members":1},
    'autoLeave':False,
    'autoLeave1':False,
    "detectMention":False,
    "Mentionkick":False,
    "welcomeOn":False,
    "sticker":False,
    "unsend":True,
    "selfbot":True,
    "mention":"Masuk say ngitip bacok",
    "Respontag":"Cuy ngrtag mele..",
    "welcome":"Wellcome to my Fams",
    "comment":"Auto like By S̶̭̗̞̙̿͑̽̆̃̒į̷̙̝̦̤̜̗́̉ͅl̸̛͓͋͋͆̍ę̶͇̮̦̣̖̙̘̪̉n̸͍̦͉̖̟͚̗̣̍̓̽̅̚ť̴̙͋ ̷̨̳̠͎̮̘͇̀̅̀͒̈́͊̕͝T̸̡̯̗̩̺͉̑́͛̌̒ͅé̶̡̱̯̮̯̊̏́̀̃͜a̴̭͓̫͚̐́̂̍̂̊̋̚m̸̨̨̹͎͍̳̥͆̓͗̿͐͗͑̿̓͠ ̴̠͐̂B̷̛̳͎̫̻̫̯̣͓̲͋̀͋̋͊̈͗͑o̵̲̾̈́͒͗t̴̢͍̫̰̠̞͖͍̬̑̊̽͒́̈́͗ͅ",
    "comment1":"Auto like By S̶̭̗̞̙̿͑̽̆̃̒į̷̙̝̦̤̜̗́̉ͅl̸̛͓͋͋͆̍ę̶͇̮̦̣̖̙̘̪̉n̸͍̦͉̖̟͚̗̣̍̓̽̅̚ť̴̙͋ ̷̨̳̠͎̮̘͇̀̅̀͒̈́͊̕͝T̸̡̯̗̩̺͉̑́͛̌̒ͅé̶̡̱̯̮̯̊̏́̀̃͜a̴̭͓̫͚̐́̂̍̂̊̋̚m̸̨̨̹͎͍̳̥͆̓͗̿͐͗͑̿̓͠ ̴̠͐̂B̷̛̳͎̫̻̫̯̣͓̲͋̀͋̋͊̈͗͑o̵̲̾̈́͒͗t̴̢͍̫̰̠̞͖͍̬̑̊̽͒́̈́͗ͅ",
    "message":"Ciee nge add kepo ye..\nThanks for add me..\n\nS̶̭̗̞̙̿͑̽̆̃̒į̷̙̝̦̤̜̗́̉ͅl̸̛͓͋͋͆̍ę̶͇̮̦̣̖̙̘̪̉n̸͍̦͉̖̟͚̗̣̍̓̽̅̚ť̴̙͋ ̷̨̳̠͎̮̘͇̀̅̀͒̈́͊̕͝T̸̡̯̗̩̺͉̑́͛̌̒ͅé̶̡̱̯̮̯̊̏́̀̃͜a̴̭͓̫͚̐́̂̍̂̊̋̚m̸̨̨̹͎͍̳̥͆̓͗̿͐͗͑̿̓͠ ̴̠͐̂B̷̛̳͎̫̻̫̯̣͓̲͋̀͋̋͊̈͗͑o̵̲̾̈́͒͗t̴̢͍̫̰̠̞͖͍̬̑̊̽͒́̈́͗ͅ"
}
protect = {
    "pqr":[],
    "pinv":[],
    "proall":[],
    "antijs":[],
    "protect":[]
}

read = {
    "readPoint":{},
    "readMember":{},
    "readTime":{},
    "ROM":{},
}

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}
myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}
try:
    with open("Log_data.json","r",encoding="utf_8_sig") as f:
        msg_dict = json.loads(f.read())
except:
    print("Couldn't read Log data")
    
dzProfile = cl.getProfile()
myProfile["displayName"] = dzProfile.displayName
myProfile["statusMessage"] = dzProfile.statusMessage
myProfile["pictureStatus"] = dzProfile.pictureStatus

    
imagesOpen = codecs.open("image.json","r","utf-8")
videosOpen = codecs.open("video.json","r","utf-8")
stickersOpen = codecs.open("sticker.json","r","utf-8")
audiosOpen = codecs.open("audio.json","r","utf-8")
images = json.load(imagesOpen)
videos = json.load(videosOpen)
stickers = json.load(stickersOpen)
audios = json.load(audiosOpen)

mulai = time.time()

tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def logError(text):
    cl.log("[ ERROR ] {}".format(str(text)))
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow,"(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = "{}, {} - {} - {} | {}".format(str(hasil), str(inihari.strftime('%d')), str(bln), str(inihari.strftime('%Y')), str(inihari.strftime('%H:%M:%S')))
    with open("logError.txt","a") as error:
        error.write("\n[ {} ] {}".format(str(time), text))
        
def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > timedelta(1):
            if "path" in msg_dict[data]:
                cl.deleteFile(msg_dict[data]["path"])
            del msg_dict[data]

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     
        import urllib,request
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"
            
def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > datetime.timedelta(1):
            del msg_dict[msg_id]
            
def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      
            time.sleep(0.1)        
            page = page[end_content:]
    return items
    
def downloadImageWithURL (mid):
    contact = cl.getContact(mid)
    if contact.videoProfile == None:
        cl.cloneContactProfile(mid)
    else:
        profile = cl.getProfile()
        profile.displayName, profile.statusMessage = contact.displayName, contact.statusMessage
        client.updateProfile(profile)
        pict = cl.downloadFileURL('http://dl.profile.line-cdn.net/' + contact.pictureStatus, saveAs="tmp/pict.bin")
        vids = cl.downloadFileURL( 'http://dl.profile.line-cdn.net/' + contact.pictureStatus + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = client.getProfileDetail(mid)['result']['objectId']
    cl.updateProfileCoverById(coverId)
    
def restartBot():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)
    
def sendImage(to, path, name="image"):
    try:
        if settings["server"] == "VPS":
            client.sendImageWithURL(to, str(path))
    except Exception as error:
        logError(error)

def delExpire():
    if temp_flood != {}:
        for tmp in temp_flood:
            if temp_flood[tmp]["expire"] == True:
                if time.time() - temp_flood[tmp]["time"] >= 3*10:
                    temp_flood[tmp]["expire"] = False
                    temp_flood[tmp]["time"] = time.time()
                    try:
                        cl.sendMessage(tmp, "Bot kembali aktif")
                    except Exception as error:
                        logError(error)
                        
def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
                        
def changeVideoAndPictureProfile(pict, vids):
    try:
        files = {'file': open(vids, 'rb')}
        obs_params = cl.genOBSParams({'oid': mid, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = cl.server.postContent('{}/talk/vp/upload.nhn'.format(str(cl.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return "Failed update profile"
        cl.updateProfilePicture(pict, 'vp')
        return "Success update profile"
    except Exception as e:
        raise Exception("Error change video and picture profile {}".format(str(e)))

def changeProfileVideo(to):
    if settings['changeProfileVideo']['picture'] == None:
        return cl.sendMessage(to, "Foto tidak ditemukan")
    elif settings['changeProfileVideo']['video'] == None:
        return cl.sendMessage(to, "Video tidak ditemukan")
    else:
        path = settings['changeProfileVideo']['video']
        files = {'file': open(path, 'rb')}
        obs_params = cl.genOBSParams({'oid': cl.getProfile().mid, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = cl.server.postContent('{}/talk/vp/upload.nhn'.format(str(cl.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return cl.sendMessage(to, "Gagal update profile")
        path_p = settings['changeProfileVideo']['picture']
        settings['changeProfileVideo']['status'] = False
        cl.updateProfilePicture(path_p, 'vp')

def cloneProfile(mid):
    contact = cl.getContact(mid)
    if contact.videoProfile == None:
        cl.cloneContactProfile(mid)
    else:
        profile = cl.getProfile()
        profile.displayName, profile.statusMessage = contact.displayName, contact.statusMessage
        cl.updateProfile(profile)
        pict = cl.downloadFileURL('http://dl.profile.line-cdn.net/' + contact.pictureStatus, saveAs="tmp/pict.bin")
        vids = cl.downloadFileURL( 'http://dl.profile.line-cdn.net/' + contact.pictureStatus + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = cl.getProfileDetail(mid)['result']['objectId']
    cl.updateProfileCoverById(coverId)

def restoreProfile():
    profile = cl.getProfile()
    profile.displayName = settings['myProfile']['displayName']
    profile.statusMessage = settings['myProfile']['statusMessage']
    if settings['myProfile']['videoProfile'] == None:
        profile.pictureStatus = settings['myProfile']['pictureStatus']
        cl.updateProfileAttribute(8, profile.pictureStatus)
        cl.updateProfile(profile)
    else:
        cl.updateProfile(profile)
        pict = cl.downloadFileURL('http://dl.profile.line-cdn.net/' + settings['myProfile']['pictureStatus'], saveAs="tmp/pict.bin")
        vids = cl.downloadFileURL( 'http://dl.profile.line-cdn.net/' + settings['myProfile']['pictureStatus'] + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = settings['myProfile']['coverId']
    cl.updateProfileCoverById(coverId)
    
def speedtest(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours,24)
    weaks, days = divmod(days,7)
    if days == 0:
        return '%02d' % (secs)
    elif days > 0 and weaks == 0:
        return '%02d' %(secs)
    elif days > 0 and weaks > 0:
        return '%02d' %(secs)

def backupProfile():
    profile = cl.getContact(mid)
    settings['myProfile']['displayName'] = profile.displayName
    settings['myProfile']['pictureStatus'] = profile.pictureStatus
    settings['myProfile']['statusMessage'] = profile.statusMessage
    settings['myProfile']['videoProfile'] = profile.videoProfile
    coverId = cl.getProfileDetail()['result']['objectId']
    settings['myProfile']['coverId'] = str(coverId)
def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "Mention User「{}」\n\n  [ Mention ]\n1. ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def siderMembers(to, mid):
    try:
        arrData = ""
        textx = "Sider User「{}」\nHaii ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["mention"]
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = "Member Masuk「{}」\nHaii  ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = cl.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["welcome"]+"\nNama grup : "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention(to, mid, firstmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x \n"
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        today = datetime.today()
        future = datetime(2018,3,1)
        hari = (str(future - today))
        comma = hari.find(",")
        hari = hari[:comma]
        teman = cl.getAllContactIds()
        gid = cl.getGroupIdsJoined()
        tz = pytz.timezone("Asia/Jakarta")
        timeNow = datetime.now(tz=tz)
        eltime = time.time() - mulai
        bot = runtime(eltime)
        text += mention+"\nJam : "+datetime.strftime(timeNow,'%H:%M:%S')+" Wib\nGroup : "+str(len(gid))+"\nTeman : "+str(len(teman))+"\nxpired : In "+hari+"\nVersion : Sempak Bot\nTanggal : "+datetime.strftime(timeNow,'%Y-%m-%d')+"\nRuntime : \n • "+bot
        cl.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention1(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        cl.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def command(text):
    pesan = text.lower()
    if pesan.startswith(Setmain['keyCommand']):
        cmd = pesan.replace(Setmain['keyCommand'],"")
    else:
        cmd = "command"
    return cmd

def help():
    num = 1
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage = "╭━━━━━━━━━━━━━━━\n"
    helpMessage += "┃ " + "╭──⍟ᴛᴇᴀᴍ ʙᴏᴛ ᴘʀᴏᴛᴇᴄᴛ⍟─\n"
    helpMessage += "┃" + " ├───༼ᴍᴇɴᴜ ʙᴏᴛ sɪʟᴇɴᴛ༽──\n"
    helpMessage += "┃" + " ├──────────────\n"
    helpMessage += "╠❂➣ %i. " % num + key + "Me\n"
    num = (num+1)
    helpMessage += "╠❂➣ %i. " % num + key + "Sp\n"
    num = (num+1)
    helpMessage += "╠❂➣ %i. " % num + key + "Kepo @\n"
    num = (num+1)
    helpMessage += "╠❂➣ %i. " % num + key + "Mybot\n"
    num = (num+1)
    helpMessage += "╠❂➣ %i. " % num + key + "Settings\n"
    num = (num+1)
    helpMessage += "╠❂➣ %i. " % num + key + "Name\n"
    num = (num+1)
    helpMessage += "╠❂➣ %i. " % num + key + "Get mid @\n"
    num = (num+1)
    helpMessage += "╠❂➣ %i. " % num + key + "About\n"
    num = (num+1)
    helpMessage += "╠❂➣ %i. " % num + key + "Sktime\n"
    num = (num+1)
    helpMessage += "╠❂➣ %i. " % num + key + "Creator\n"
    num = (num+1)
    helpMessage += "╠❂➣ %i. " % num + key + "Ginfo\n"
    num = (num+1)
    helpMessage += "╠❂➣ %i. " % num + key + "Open\n"
    num = (num+1)    
    helpMessage += "╠❂➣ %i. " % num + key + "Close\n"
    num = (num+1)
    helpMessage += "╠❂➣ %i ." % num + key + "Url grup\n"
    num = (num+1)
    helpMessage += "╠❂➣ %i. " % num + key + "Glist\n"
    num = (num+1)
    helpMessage += "╠❂➣ %i. " % num + key + "Stafflist\n"
    num = (num+1)
    helpMessage += "╠❂➣ %i. " % num + key + "Botlist\n"
    num = (num+1)
    helpMessage += "╠❂➣ %i. " % num + key + "Hapuschat\n"
    num = (num+1)
    helpMessage += "╠❂➣ %i. " % num + key + "Sider on/off\n"
    num = (num+1)
    helpMessage += "╠❂➣ %i. " % num + key + "Upfoto\n"
    num = (num+1)
    helpMessage += "╠❂➣ %i. " % num + key + "Upgrup\n"
    num = (num+1)
    helpMessage += "╠❂➣ %i. " % num + key + "Bcast:「Text」\n"
    num = (num+1)
    helpMessage += "╠❂➣ %i. " % num + key + "Set sname\n"
    num = (num+1)
    helpMessage += "╠❂➣ %i. " % num + key + "Sname\n"
    num = (num+1)
    helpMessage += "╠❂➣ %i. " % num + key + "Reset sname\n"
    num = (num+1)
    helpMessage += "╠❂➣ %i. " % num + key + "Ssider: text\n"
    num = (num+1)
    helpMessage += "╠❂➣ %i. " % num + key + "Spesan: text\n"
    num = (num+1)
    helpMessage += "╠❂➣ %i. " % num + key + "Swelcome: text\n"
    num = (num+1)
    helpMessage += "╠❂➣ %i. " % num + key + "Srepson: text\n"
    num = (num+1)
    helpMessage += "╠❂➣ %i. " % num + key + "Csider/off\n"
    num = (num+1)
    helpMessage += "╠❂➣ %i. " % num + key + "Cpesan/off\n"
    num = (num+1)
    helpMessage += "╠❂➣ %i. " % num + key + "Crespon\n"
    num = (num+1)
    helpMessage += "╠❂➣ %i. " % num + key + "Cwelcome\n"
    num = (num+1)
    helpMessage += "╠❂➣ %i. " % num + key + "Sticker「on/off\n"
    num = (num+1)
    helpMessage += "╠❂➣ %i. " % num + key + "Respon「on/off」\n"
    num = (num+1)
    helpMessage += "╠❂➣ %i. " % num + key + "Unsend「on/off」\n"
    num = (num+1)
    helpMessage += "╠❂➣ %i. " % num + key + "Autoblock「on/off」\n"
    num = (num+1)
    helpMessage += "╠❂➣ %i. " % num + key + "Welcome「on/off」\n"
    num = (num+1)
    helpMessage += "╠❂➣ %i. " % num + key + "Musik Judul lagu\n"
    num = (num+1)
    helpMessage += "╠❂➣ %i. " % num + key + "Ytmp3: Judul lagu\n"
    num = (num+1)
    helpMessage += "╠❂➣ %i. " % num + key + "Ytmp4: Judul Video\n"
    num = (num+1)
    helpMessage += "╠❂➣ %i. " % num + key + "Changedual \n"
    num = (num+1)
    helpMessage += "╠❂➣ %i. " % num + key + "Changedualurl: •link•\n"
    num = (num+1)
    helpMessage += "╠❂➣ %i. " % num + key + "Img food: produk\n"
    num = (num+1)
    helpMessage += "╠❂➣ %i. " % num + key + "Profilesmule: id\n"
    num = (num+1)
    helpMessage += "╠❂➣ %i. " % num + key + " Profileig: id\n"
    num = (num+1)
    helpMessage += "╠❂➣ %i. " % num + key + "Meme@nama@kata1@kata2\n"
    num = (num+1)
    helpMessage += "╠❂➣ %i. " % num + key + "Addimg •nama•\n"
    num = (num+1)
    helpMessage += "╠❂➣ %i. " % num + key + "Dellimg •nama•\n"
    num = (num+1)
    helpMessage += "╠❂➣ %i. " % num + key + "Listimg •nama•\n"
    num = (num+1)
    helpMessage += "╠❂➣ %i. " % num + key + "Addvideo •nama•\n"
    num = (num+1)
    helpMessage += "╠❂➣ %i. " % num + key + "Dellvideo •nama•\n"
    num = (num+1)
    helpMessage += "╠❂➣ %i. " % num + key + "Listvideo •nama•\n"
    num = (num+1)
    helpMessage += "╠❂➣ %i. " % num + key + "Addsticker •nama•\n"
    num = (num+1)
    helpMessage += "╠❂➣ %i. " % num + key + "Dellsticker •nama•\n"
    num = (num+1)
    helpMessage += "╠❂➣ %i. " % num + key + "Liststicker •nama•\n"
    num = (num+1)
    helpMessage += "╠❂➣ %i. " % num + key + "Addaudio •nama•\n"
    num = (num+1)
    helpMessage += "╠❂➣ %i. " % num + key + "Dellaudio •nama•\n"
    num = (num+1)
    helpMessage += "╠❂➣ %i. " % num + key + "Listaudio •nama•\n"
    num = (num+1)    
    helpMessage += "┃ " + "├──────────────\n"
    helpMessage += "┃ " + "╰──⍟ᴛᴇᴀᴍ ʙᴏᴛ ᴘʀᴏᴛᴇᴄᴛ⍟──\n"
    helpMessage += "╰━━━━━━━━━━━━━━━━"
    helpMessage += " Creator: https://line.me/ti/p/~teambotprotect \n"
    return helpMessage

def helpbot():
    num = 1
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage2 = "╭━━━━━━━━━━━━━━━━\n"
    helpMessage2 += "┃ " + "╭───⍟ᴛᴇᴀᴍ ʙᴏᴛ ᴘʀᴏᴛᴇᴄᴛ⍟─\n"
    helpMessage2 += "┃" + " ├───༼ᴄᴏᴍᴍᴀɴᴅ ᴋɪᴄᴋᴇʀ༽──\n"
    helpMessage2 += "┃" + " ├──────────────\n"
    helpMessage2 += "╠❂➣ %i. " % num + key + "Kicker @\n"
    num = (num+1)
    helpMessage2 += "╠❂➣ %i. " % num + key + "Vc @ \n"
    num = (num+1)
    helpMessage2 += "╠❂➣ %i. " % num + key + "Mainkan @\n"
    num = (num+1)
    helpMessage2 += "╠❂➣ %i. " % num + key + "Invite \n"
    num = (num+1)
    helpMessage2 += "╠❂➣ %i. " % num + key + "Bl \n"
    num = (num+1)
    helpMessage2 += "╠❂➣ %i. " % num + key + "Refresh \n"
    num = (num+1)
    helpMessage2 += "╠❂➣ %i. " % num + key + "Gas \n"
    num = (num+1)
    helpMessage2 += "╠❂➣ %i. " % num + key + "Killban \n"
    num = (num+1)
    helpMessage2 += "╠❂➣ %i. " % num + key + "Spaminvite on \n"
    num = (num+1)
    helpMessage2 += "╠❂➣ %i. " % num + key + "Spaminvite off \n"
    num = (num+1)
    helpMessage2 += "╠❂➣ %i. " % num + key + "Banlist\n"
    num = (num+1)
    helpMessage2 += "╠❂➣ %i. " % num + key + "Ban all\n"
    num = (num+1)
    helpMessage2 += "╠❂➣ %i. " % num + key + "Clearban\n"
    num = (num+1)
    helpMessage2 += "╠❂➣ %i. " % num + key + "Adminexpl:on\n"
    num = (num+1)
    helpMessage2 += "╠❂➣ %i. " % num + key + "Admin:on @\n"
    num = (num+1)
    helpMessage2 += "╠❂➣ %i. " % num + key + "Admin:on\n"
    num = (num+1)
    helpMessage2 += "╠❂➣ %i. " % num + key + "Adminexpl:on @\n"
    num = (num+1)
    helpMessage2 += "╠❂➣ %i. " % num + key + "Owner:on\n"
    num = (num+1)
    helpMessage2 += "╠❂➣ %i. " % num + key + "Staff:on\n"
    num = (num+1)
    helpMessage2 += "╠❂➣ %i. " % num + key + "Staff:on @\n"
    num = (num+1)
    helpMessage2 += "╠❂➣ %i. " % num + key + "Staffexpl:on\n"
    num = (num+1)
    helpMessage2 += "╠❂➣ %i. " % num + key + "Staffexpl:on @\n"
    num = (num+1)
    helpMessage2 += "╠❂➣ %i. " % num + key + "Bot:on\n"
    num = (num+1)
    helpMessage2 += "╠❂➣ %i. " % num + key + "Bot:on @\n"
    num = (num+1)
    helpMessage2 += "╠❂➣ %i. " % num + key + "Botexpl:on\n"
    num = (num+1)
    helpMessage2 += "╠❂➣ %i. " % num + key + "Botexpl:on @\n"
    num = (num+1)
    helpMessage2 += "╠❂➣ %i. " % num + key + "Ban:on @\n"
    num = (num+1)
    helpMessage2 += "╠❂➣ %i. " % num + key + "Ban:on\n"
    num = (num+1)
    helpMessage2 += "╠❂➣ %i. " % num + key + "Unban:on @\n"
    num = (num+1)
    helpMessage2 += "╠❂➣ %i. " % num + key + "Unban:on\n"
    num = (num+1)
    helpMessage2 += "╠❂➣ %i ." % num + key + "Talkban:on @\n"
    num = (num+1)
    helpMessage2 += "╠❂➣ %i. " % num + key + "Talkban:on\n"
    num = (num+1)
    helpMessage2 += "╠❂➣ %i. " % num + key + "Untalkban:on @\n"
    num = (num+1)
    helpMessage2 += "╠❂➣ %i. " % num + key + "Untalkban:on\n"
    num = (num+1)
    helpMessage2 += "╠❂➣ %i. " % num + key + "Talkbanlist\n"
    num = (num+1)    
    helpMessage2 += "╠❂➣ %i. " % num + key + "Allpro on/off\n"
    num = (num+1)
    helpMessage2 += "╠❂➣ %i. " % num + key + "Skurl on/off\n"
    num = (num+1)
    helpMessage2 += "╠❂➣ %i. " % num + key + "Protect on/off\n"
    num = (num+1)
    helpMessage2 += "╠❂➣ %i. " % num + key + "Proall on/off\n"
    num = (num+1)
    helpMessage2 += "╠❂➣ %i. " % num + key + "Skinvite on/off\n"
    num = (num+1)
    helpMessage2 += "╠❂➣ %i. " % num + key + "Procancel on/off\n"
    num = (num+1)
    helpMessage2 += "╠❂➣ %i. " % num + key + "Js on/off\n"
    num = (num+1)
    helpMessage2 += "╠❂➣ %i. " % num + key + ".Bye/Bye[1/4]\n"
    num = (num+1)
    helpMessage2 += "╠❂➣ %i. " % num + key + "Leave「Namagrup」\n"
    num = (num+1)    
    helpMessage2 += "╠❂➣ %i. " % num + key + "Kicker「in」\n"
    num = (num+1)  
    helpMessage2 += "╠❂➣ %i. " % num + key + "Kicker「lv」\n"
    num = (num+1)    
    helpMessage2 += "╠❂➣ %i. " % num + key + "Infogrup「angka」\n"
    num = (num+1)
    helpMessage2 += "╠❂➣ %i. " % num + key + "Infomem「angka」\n"
    num = (num+1) 
    helpMessage2 += "╠❂➣ %i. " % num + key + "Autojointicket on/off\n"
    num = (num+1)
    helpMessage2 += "╠❂➣ %i. " % num + key + "Silentkiller [kickall]\n"
    num = (num+1)
    helpMessage2 += "╠❂➣ %i. " % num + key + "Bubar [kickall]\n"
    num = (num+1)
    helpMessage2 += "╠❂➣ %i. " % num + key + "Silent \n"
    num = (num+1)
    helpMessage2 += "╠❂➣ %i. " % num + key + "Autojoin on/off\n"
    num = (num+1)
    helpMessage2 += "╠❂➣ %i. " % num + key + "Jointicket on/off\n"
    num = (num+1)
    helpMessage2 += "╠❂➣ %i. " % num + key + "Autoadd on/off\n"
    num = (num+1)
    helpMessage2 += "╠❂➣ %i. " % num + key + "leave on/off\n"
    num = (num+1)
    helpMessage2 += "┃ " + "├──────────────\n"
    helpMessage2 += "┃ " + "╰──⍟ᴛᴇᴀᴍ ʙᴏᴛ ᴘʀᴏᴛᴇᴄᴛ⍟──\n"
    helpMessage2 += "╰━━━━━━━━━━━━━━━━"
    helpMessage2 += " My ID LINE : 〘 https://line.me/ti/p/~teambotprotect 〙\n"
    return helpMessage2

def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            return
        
        if op.type == 11:
            if op.param1 in protect["pqr"]:
                try:
                    if cl.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                            cl.reissueGroupTicket(op.param1)
                            X = cl.getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            Ticket = cl.reissueGroupTicket(op.param1)
                            sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                            sw.kickoutFromGroup(op.param1,[op.param2])
                            sw.leaveGroup(op.param1)
                            cl.updateGroup(X)
                except:
                    try:
                        if ki.getGroup(op.param1).preventedJoinByTicket == False:
                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                ki.reissueGroupTicket(op.param1)
                                X = ki.getGroup(op.param1)
                                X.preventedJoinByTicket = True
                                Ticket = ki.reissueGroupTicket(op.param1)
                                sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                sw.kickoutFromGroup(op.param1,[op.param2])
                                sw.leaveGroup(op.param1)
                                ki.updateGroup(X)
                    except:
                        try:
                            if kk.getGroup(op.param1).preventedJoinByTicket == False:
                                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                    kk.reissueGroupTicket(op.param1)
                                    X = kk.getGroup(op.param1)
                                    X.preventedJoinByTicket = True
                                    Ticket = kk.reissueGroupTicket(op.param1)
                                    sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    sw.kickoutFromGroup(op.param1,[op.param2])
                                    kk.updateGroup(X)
                        except:
                            try:
                                if kc.getGroup(op.param1).preventedJoinByTicket == False:
                                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                        kc.reissueGroupTicket(op.param1)
                                        X = kc.getGroup(op.param1)
                                        X.preventedJoinByTicket = True
                                        Ticket = kc.reissueGroupTicket(op.param1)
                                        sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        sw.kickoutFromGroup(op.param1,[op.param2])
                                        kc.updateGroup(X)
                            except:
                                try:
                                    if km.getGroup(op.param1).preventedJoinByTicket == False:
                                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                            km.reissueGroupTicket(op.param1)
                                            X = km.getGroup(op.param1)
                                            X.preventedJoinByTicket = True
                                            Ticket = km.reissueGroupTicket(op.param1)
                                            sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            sw.kickoutFromGroup(op.param1,[op.param2])
                                            km.updateGroup(X)
                                except:
                                    try:
                                        if kb.getGroup(op.param1).preventedJoinByTicket == False:
                                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                kb.reissueGroupTicket(op.param1)
                                                X = kb.getGroup(op.param1)
                                                X.preventedJoinByTicket = True
                                                Ticket = kb.reissueGroupTicket(op.param1)
                                                sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                sw.kickoutFromGroup(op.param1,[op.param2])
                                                kb.updateGroup(X)
                                    except:
                                        pass
                      
        if op.type == 11:
            if op.param1 in warmode:
                try:
                    if cl.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                            wait["blacklist"][op.param2] = True
                            try:ki.kickoutFromGroup(op.param1,[op.param2])
                            except:
                            	try:kk.kickoutFromGroup(op.param1,[op.param2])
                            	except:
                            	    try:kc.kickoutFromGroup(op.param1,[op.param2])
                            	    except:
                            	        try:km.kickoutFromGroup(op.param1,[op.param2])
                            	        except:
                            	            try:kb.kickoutFromGroup(op.param1,[op.param2])
                            	            except:pass
                            warmode.remove(op.param1)
                except:pass
       
        if op.type == 17:
            if op.param2 in wait["blacklist"]:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                   try:ki.kickoutFromGroup(op.param1,[op.param2])
                   except:
                   	try:kk.kickoutFromGroup(op.param1,[op.param2])
                   	except:
                   	    try:kc.kickoutFromGroup(op.param1,[op.param2])
                   	    except:
                               try:km.kickoutFromGroup(op.param1,[op.param2])
                               except:
                                    try:kb.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                   	                 try:cl.reissueGroupTicket(op.param1);X = cl.getGroup(op.param1);X.preventedJoinByTicket = True;Ticket = cl.reissueGroupTicket(op.param1);sw.acceptGroupInvitationByTicket(op.param1,Ticket);sw.kickoutFromGroup(op.param1,[op.param2])
                   	                 except:pass
                   cl.reissueGroupTicket(op.param1)
                   X = cl.getGroup(op.param1)
                   X.preventedJoinByTicket = True
                   cl.updateGroup(X)
                   warmode.append(op.param1)
                else:
                   pass
#========================== PROTECTUPDATEGROUP                          
        if op.type == 13:
            if mid in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        cl.sendMessage(op.param1,"Sorry anda bukan admin kami\nSelamat tinggal " +str(ginfo.name))
                        cl.leaveGroup(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        cl.sendMessage(op.param1,"Im'coming " + str(ginfo.name))

        if op.type == 13:
            if mid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        cl.sendMessage(op.param1,"I'm coming " +str(ginfo.name))
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        cl.sendMessage(op.param1,"I'm coming " + str(ginfo.name))
            if Amid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        ki.acceptGroupInvitation(op.param1)
                        ginfo = ki.getGroup(op.param1)                        
                        ki.leaveGroup(op.param1)
                    else:
                        ki.acceptGroupInvitation(op.param1)                                             
            if Bmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kk.acceptGroupInvitation(op.param1)
                        ginfo = kk.getGroup(op.param1)                        
                        kk.leaveGroup(op.param1)
                    else:
                        kk.acceptGroupInvitation(op.param1)                       
            if Cmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kc.acceptGroupInvitation(op.param1)
                        ginfo = kc.getGroup(op.param1)                       
                        kc.leaveGroup(op.param1)
                    else:
                        kc.acceptGroupInvitation(op.param1)                      
            if Dmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        km.acceptGroupInvitation(op.param1)
                        ginfo = km.getGroup(op.param1)                        
                        km.leaveGroup(op.param1)
                    else:
                        km.acceptGroupInvitation(op.param1)                        
            if Emid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kb.acceptGroupInvitation(op.param1)
                        ginfo = kb.getGroup(op.param1)                        
                        kb.leaveGroup(op.param1)
                    else:
                        kb.acceptGroupInvitation(op.param1)                       
#____________________________________________________________________
        if op.type == 13:
            if op.param1 in protect['pinv']:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        group = cl.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            random.choice(ABC).cancelGroupInvitation(op.param1,[_mid])
                    except:
                        try:
                            group = ki.getGroup(op.param1)
                            gMembMids = [contact.mid for contact in group.invitee]
                            for _mid in gMembMids:
                                random.choice(ABC).cancelGroupInvitation(op.param1,[_mid])                                 
                        except:
                            try:
                               group = kk.getGroup(op.param1)
                               gMembMids = [contact.mid for contact in group.invitee]
                               for _mid in gMembMids:
                                   random.choice(ABC).cancelGroupInvitation(op.param1,[_mid])                                                                          
                            except:
                               try:
                                   group = kc.getGroup(op.param1)
                                   gMembMids = [contact.mid for contact in group.invitee]
                                   for _mid in gMembMids:
                                       random.choice(ABC).cancelGroupInvitation(op.param1,[_mid])
                               except:
                                   try:
                                      group = km.getGroup(op.param1)
                                      gMembMids = [contact.mid for contact in group.invitee]
                                      for _mid in gMembMids:
                                          random.choice(ABC).cancelGroupInvitation(op.param1,[_mid])
                                   except:
                                      try:
                                          group = kb.getGroup(op.param1)
                                          gMembMids = [contact.mid for contact in group.invitee]
                                          for _mid in gMembMids:
                                              random.choice(ABC).cancelGroupInvitation(op.param1,[_mid])
                                      except:
                                          pass
                                    
        if op.type == 13:
            if op.param2 in wait["blacklist"]:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True                    
                    try:
                        cl.cancelGroupInvitation(op.param1,[op.param2])
                    except:
                        try:
                            ki.cancelGroupInvitation(op.param1,[op.param2])
                        except:
                            try:
                                kk.cancelGroupInvitation(op.param1,[op.param2])
                            except:
                                try:
                                    kc.cancelGroupInvitation(op.param1,[op.param2])
                                except:
                                    try:
                                    	km.cancleGroupInvitation(op.param1,[op.param2])
                                    except:
                                        try:
                                        	kb.cancleGroupInvitation(op.param1,[op.param2])
                                        except:
                                        	pass
                return
                                            
#__________________________________ 
        if op.type == 17:
            if op.param2 in wait["blacklist"]:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True                    
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                    	km.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                        	kb.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                        	pass
                return
#____________________________________________________________________               
        if op.type == 19:
            if op.param2 in wait["blacklist"]:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True                    
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                    	km.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                        	kb.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                        	pass
                return
#________________________________                                            
        if op.type == 19:
            if mid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ki.inviteIntoGroup(op.param1,[op.param3])
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        cl.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kk.inviteIntoGroup(op.param1,[op.param3])
                            kk.kickoutFromGroup(op.param1,[op.param2])
                            cl.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kc.inviteIntoGroup(op.param1,[op.param3])
                                kc.kickoutFromGroup(op.param1,[op.param2])
                                cl.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    km.inviteIntoGroup(op.param1,[op.param3])
                                    km.kickoutFromGroup(op.param1,[op.param2])
                                    cl.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        kb.inviteIntoGroup(op.param1,[op.param3])
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                        cl.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            G = ki.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            ki.updateGroup(G)
                                            Ticket = ki.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            G = kk.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            kk.updateGroup(G)
                                            Ticket = kk.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.kickoutFromGroup(op.param1,[op.param2])
                return
            if Amid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kk.inviteIntoGroup(op.param1,[op.param3])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        ki.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kc.inviteIntoGroup(op.param1,[op.param3])
                            kc.kickoutFromGroup(op.param1,[op.param2])
                            ki.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kk.inviteIntoGroup(op.param1,[op.param3])
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                ki.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    kb.inviteIntoGroup(op.param1,[op.param3])
                                    kb.kickoutFromGroup(op.param1,[op.param2])
                                    ki.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        G = cl.getGroup(op.param1)
                                        G.preventedJoinByTicket = False
                                        cl.updateGroup(G)
                                        Ticket = cl.reissueGroupTicket(op.param1)
                                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        ki.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        pass
                return
            if Bmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kc.inviteIntoGroup(op.param1,[op.param3])
                        kc.kickoutFromGroup(op.param1,[op.param2])
                        kk.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            km.inviteIntoGroup(op.param1,[op.param3])
                            km.kickoutFromGroup(op.param1,[op.param2])
                            kk.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kb.inviteIntoGroup(op.param1,[op.param3])
                                kb.kickoutFromGroup(op.param1,[op.param2])
                                kk.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    ki.inviteIntoGroup(op.param1,[op.param3])
                                    ki.kickoutFromGroup(op.param1,[op.param2])
                                    kk.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        G = cl.getGroup(op.param1)
                                        G.preventedJoinByTicket = False
                                        cl.updateGroup(G)
                                        Ticket = cl.reissueGroupTicket(op.param1)
                                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        kk.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        pass
                return
            if Cmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        km.inviteIntoGroup(op.param1,[op.param3])
                        km.kickoutFromGroup(op.param1,[op.param2])
                        kc.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kb.inviteIntoGroup(op.param1,[op.param3])
                            kb.kickoutFromGroup(op.param1,[op.param2])
                            kc.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                ki.inviteIntoGroup(op.param1,[op.param3])
                                ki.kickoutFromGroup(op.param1,[op.param2])
                                kc.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    kk.inviteIntoGroup(op.param1,[op.param3])
                                    kk.kickoutFromGroup(op.param1,[op.param2])
                                    kc.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        G = cl.getGroup(op.param1)
                                        G.preventedJoinByTicket = False
                                        cl.updateGroup(G)
                                        Ticket = cl.reissueGroupTicket(op.param1)
                                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        kc.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        pass
                return
            if Dmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kb.inviteIntoGroup(op.param1,[op.param3])
                        kb.kickoutFromGroup(op.param1,[op.param2])
                        kb.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            ki.inviteIntoGroup(op.param1,[op.param3])
                            kc.kickoutFromGroup(op.param1,[op.param2])
                            km.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kk.inviteIntoGroup(op.param1,[op.param3])
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                km.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    kc.inviteIntoGroup(op.param1,[op.param3])
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    km.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        G = cl.getGroup(op.param1)
                                        G.preventedJoinByTicket = False
                                        cl.updateGroup(G)
                                        Ticket = cl.reissueGroupTicket(op.param1)
                                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        km.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        pass
                return
            if Emid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ki.inviteIntoGroup(op.param1,[op.param3])
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        kb.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kk.inviteIntoGroup(op.param1,[op.param3])
                            kk.kickoutFromGroup(op.param1,[op.param2])
                            kb.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kc.inviteIntoGroup(op.param1,[op.param3])
                                kc.kickoutFromGroup(op.param1,[op.param2])
                                kb.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    km.inviteIntoGroup(op.param1,[op.param3])
                                    km.kickoutFromGroup(op.param1,[op.param2])
                                    kb.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        G = cl.getGroup(op.param1)
                                        G.preventedJoinByTicket = False
                                        cl.updateGroup(G)
                                        Ticket = cl.reissueGroupTicket(op.param1)
                                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        pass
#____________________________________________________________________
        if op.type == 17:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = cl.getGroup(op.param1)
                contact = cl.getContact(op.param2).picturePath
                image = 'http://dl.profile.line.naver.jp'+contact
                welcomeMembers(op.param1, [op.param2])
                cl.sendImageWithURL(op.param1, image)
             
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                if op.param2 not in Bots and op.param2 not in owner:
                    if (wait["message"] in [" "," ","\n",None]):
                        pass
                    else:
                        cl.sendMessage(op.param1, wait["message"])

        if op.type == 32:
            if op.param1 in protectcancel:
                if op.param3 in Bots:
                    if op.param2 not in Bots and op.param2 not in Team:
                        wait["blacklist"][op.param2] = True
                        try:
                            if op.param3 not in wait["blacklist"]:
                                random.coice(ABC).findAndAddContactsByMid(op.param1,[Zmid])
                                random.coice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                random.coice(ABC).inviteIntoGroup(op.param1,[Zmid])
                        except:
                            pass

        if op.type == 32:
            if op.param3 in Zmid:
              if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                  wait["blacklist"][op.param2] = True
                  try:
                      if op.param3 not in wait["blacklist"]:
                          ki.kickoutFromGroup(op.param1,[op.param2])
                          ki.inviteIntoGroup(op.param1,[Zmid])
                          cl.sendMessage(op.param1, "🇦🇱JΔΠGΔΠ DI CΔΠCΣL CUΨ ҜPΔҜSΔ ΔIM CIPΩҜ🇦🇱")
                  except:
                      try:
                          if op.param3 not in wait["blacklist"]:
                              kk.kickoutFromGroup(op.param1,[op.param2])
                              kk.inviteIntoGroup(op.param1,[Zmid])
                              cl.sendMessage(op.param1, "🇦🇱JΔΠGΔΠ DI CΔΠCΣL CUΨ ҜPΔҜSΔ ΔIM CIPΩҜ🇦🇱")
                      except:
                          try:
                              if op.param3 not in wait["blacklist"]:
                                  kc.kickoutFromGroup(op.param1,[op.param2])
                                  kc.inviteIntoGroup(op.param1,[Zmid])
                                  cl.sendMessage(op.param1, "🇦🇱JΔΠGΔΠ DI CΔΠCΣL CUΨ ҜPΔҜSΔ ΔIM CIPΩҜ🇦🇱")
                          except:
                              try:
                                  if op.param3 not in wait["blacklist"]:
                                      km.kickoutFromGroup(op.param1,[op.param2])
                                      km.inviteIntoGroup(op.param1,[Zmid])
                                      cl.sendMessage(op.param1, "🇦🇱JΔΠGΔΠ DI CΔΠCΣL CUΨ ҜPΔҜSΔ ΔIM CIPΩҜ🇦🇱")
                              except:
                                  try:
                                      if op.param3 not in wait["blacklist"]:
                                          kb.kickoutFromGroup(op.param1,[op.param2])
                                          kb.inviteIntoGroup(op.param1,[Zmid])
                                          cl.sendMessage(op.param1, "🇦🇱JΔΠGΔΠ DI CΔΠCΣL CUΨ ҜPΔҜSΔ ΔIM CIPΩҜ🇦🇱")
                                  except:
                                     pass
              return
#___________________________________________________________________
        if op.type == 19:
            if op.param1 in protect["proall"]:
                if op.param2 in Bots:
                    pass
                elif op.param2 in Bots:
                    pass
                elif op.param2 in owner:
                    pass
                elif op.param2 in admin:
                    pass
                elif op.param2 in staff:
                    pass
                else:
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                    if op.param3 in wait["blacklist"]:
                        pass
                    else:
                        random.coice(ABC).findAndAddContactsByMid(op.param3)                       
                        wait["blacklist"][op.param2] = True

            if op.param1 in protect["protect"]:
                if op.param2 in Bots:
                    pass
                elif op.param2 in owner:
                    pass
                elif op.param2 in admin:
                    pass
                elif op.param2 in staff:
                    pass
                elif op.param2 in Bots:
                    pass
                else:
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                    wait["blacklist"][op.param2] = True
                    
            if op.param1 in protect["antijs"]:
                if mid in op.param3:
                    if op.param2 in Bots:
                        pass
                    elif op.param2 in Bots:
                        pass
                    elif op.param2 in owner:
                        pass
                    elif op.param2 in admin:
                        pass
                    elif op.param2 in staff:
                        pass
                    else:
                        sw.acceptGroupInvitation(op.param1)
                        G = sw.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        sw.updateGroup(G)
                        Ticket = sw.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        km.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                        sw.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = True
                        sw.updateGroup(G)
                        wait["blacklist"][op.param2] = True
                        sw.leaveGroup(op.param1)
                        cl.inviteIntoGroup(op.param1,[Zmid])
                        cl.inviteIntoGroup(op.param1,[admin])
            try:
                if op.param3 in owner:
                    if op.param2 in Bots:
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                    elif op.param2 in owner:
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                    elif op.param2 in admin:
                        pass
                    else:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                        if op.param2 in Bots:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                if op.param3 in admin:
                    if op.param2 in Bots:
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                    elif op.param2 in owner:
                        pass
                    elif op.param2 in admin:
                        pass
                    elif op.param2 in Bots:
                        pass
                    else:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                        if op.param2 in Bots:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                if op.param3 in staff:
                    if op.param2 in Bots:
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                    elif op.param2 in staff:
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                    elif op.param2 in owner:
                        pass
                    elif op.param2 in admin:
                        pass
                    elif op.param2 in staff:
                        pass
                    elif op.param2 in Bots:
                        pass
                    else:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                        if op.param2 in Bots:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True              
            except:
                pass
                
        if op.type == 25 or op.type == 26:
          if settings['SpamInvite'] == True:
            msg = op.message
            sender = msg._from
            receiver = msg.to
            if msg.contentType == 13:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    korban = msg.contentMetadata["displayName"]
                    invite = msg.contentMetadata["mid"]
                    groups = cl.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for x in groups.members:
                        if korban in x.displayName:
                            cl.sendMessage(msg.to, korban + " Sudah Berada DiGrup Ini")
                        else:
                            targets.append(invite)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                ki.findAndAddContactsByMid(target)                                
                                ki.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                ki.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT                                
                                ki.sendMessage(msg.to, "Spam Invite ke " + korban + "\nSUCCESS..")
                                settings['SpamInvite'] = False
                            except:             
                                 cl.sendMessage(msg.to, 'Contact error')
                                 settings['SpamInvite'] = False
                                 break
                
        if op.type in [25, 26]:           
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            cmd = command(text)
            isValid = True
            setKey = settings["keyCommand"].title()
            if settings["setKey"] == False: setKey = ''
            if isValid != False:
                if msg.toType == 0 and sender != mid: to = sender
                else: to = receiver
                if receiver in temp_flood:
                    if temp_flood[receiver]["expire"] == True:
                        if cmd == "open" and sender == mid:
                            temp_flood[receiver]["expire"] = False
                            temp_flood[receiver]["time"] = time.time()
                            cl.sendMessage(to, "Bot kembali aktif")
                        return
                    elif time.time() - temp_flood[receiver]["time"] <= 5:
                        temp_flood[receiver]["flood"] += 1
                        if temp_flood[receiver]["flood"] >= 20:
                            temp_flood[receiver]["flood"] = 0
                            temp_flood[receiver]["expire"] = True
                            ret_ = "Spam terdeteksi, Bot akan silent selama 30 detik pada ruangan ini atau ketik {}Open untuk mengaktifkan kembali.".format(setKey)
                            cl.sendMessage(to, str(ret_))
                    else:
                         temp_flood[receiver]["flood"] = 0
                         temp_flood[receiver]["time"] = time.time()
                else:
                    temp_flood[receiver] = {
    	                "time": time.time(),
    	                "flood": 0,
    	                "expire": False
                    }
#____________________________________________________________________                
        if op.type == 55:
            if op.param2 in wait["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass

        if op.type == 55:            
            try:
                if op.param1 in read["readPoint"]:
                    if op.param2 in read["readMember"][op.param1]:
                        pass
                    else:
                        read["readMember"][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                    backupData()
                else:
                   pass
            except:
                pass
    
            if cctv['cyduk'][op.param1]==True:
                if op.param1 in cctv['point']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n~ " + Name
                        siderMembers(op.param1, [op.param2])
                        contact = cl.getContact(op.param2)
                        image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                        cl.sendImageWithURL(op.param1, image)
                        cl.sendMessage(op.param1, None, contentMetadata={"STKID":"13162615","STKPKGID":"1326453","STKVER":"1"}, contentType=7)

            if msg.contentType == 16:
                       url = msg.contentMetadata["postEndUrl"]
                       cl.like(url[25:58], url[66:], likeType=1001)
                       ki.like(url[25:58], url[66:], likeType=1001)
                       kk.like(url[25:58], url[66:], likeType=1001)
                       cl.comment(url[25:58], url[66:], wait["comment"])
                       ki.comment(url[25:58], url[66:], wait["comment"])
                       kk.comment(url[25:58], url[66:], wait["comment"])                 
        
                                                        
        if op.type == 26:
           if wait["selfbot"] == True:
               msg = op.message
               if msg._from not in Bots:
                 if wait["talkban"] == True:
                   if msg._from in wait["Talkblacklist"]:
                      try:
                          cl.kickoutFromGroup(msg.to, [msg._from])
                      except:
                          try:
                              ki.kickoutFromGroup(msg.to, [msg._from])
                          except:
                              try:
                                  kk.kickoutFromGroup(msg.to, [msg._from])
                              except:
                                  try:
                                  	kc.kickoutFromGroup(msg.to, [msg._from])
                                  except:
                                      pass
               if 'MENTION' in msg.contentMetadata.keys() != None:
                if msg._from not in Bots:
                 if wait["detectMention"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           saints = cl.getContact(msg._from)
                           sendMention1(msg.to, saints.mid, "", wait["Respontag"])
                           cl.sendMessage(op.param1, None, contentMetadata={"STKID":"13162615","STKPKGID":"1326453","STKVER":"1"}, contentType=7)
                           break
               if 'MENTION' in msg.contentMetadata.keys() != None:
                if msg._from not in Bots:
                 if wait["Mentionkick"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           cl.mentiontag(msg.to,[msg._from])
                           cl.sendMessage(msg.to, "No tag me....")
                           cl.kickoutFromGroup(msg.to, [msg._from])
                           break
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,"Cek ID Sticker\n\nSTKID : " + msg.contentMetadata["STKID"] + "\nSTKPKGID : " + msg.contentMetadata["STKPKGID"] + "\nSTKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        cl.sendMessage(msg.to,"Nama : " + msg.contentMetadata["displayName"] + "\nMID : " + msg.contentMetadata["mid"] + "\nStatus Msg : " + contact.statusMessage + "\nPicture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        cl.sendImageWithURL(msg.to, image)
#=======================================================================
        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,"STKID : " + msg.contentMetadata["STKID"] + "\nSTKPKGID : " + msg.contentMetadata["STKPKGID"] + "\nSTKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        cl.sendMessage(msg.to,"Nama : " + msg.contentMetadata["displayName"] + "\nMID : " + msg.contentMetadata["mid"] + "\nStatus Msg : " + contact.statusMessage + "\nPicture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        cl.sendImageWithURL(msg.to, image)
#ADD Bots&media
               if msg.contentType == 7:
                  if msg._from in mid:
                     if settings["AddstickerTag"]["status"] == True:
                         settings["AddstickerTag"]["sid"] = msg.contentMetadata["STKID"]
                         settings["AddstickerTag"]["spkg"] = msg.contentMetadata["STKPKGID"]
                         cl.sendMessage(msg.to, "Sticker respon hasben changed")
                         settings["AddstickerTag"]["status"] = False
                         
               if msg.contentType == 2:
                   if msg._from in admin:
                       if msg._from in settings["ChangeVideoProfilevid"]:
                            settings["ChangeVideoProfilePicture"][msg._from] = True
                            del settings["ChangeVideoProfilevid"][msg._from]
                            cl.downloadObjectMsg(msg_id,'path','video.mp4')
                            cl.sendMessage(msg.to,"Send gambarnya...")
                            
               if msg.contentType == 1:
                   if msg._from in admin:
                       if msg._from in settings["ChangeVideoProfilePicture"]:
                            del settings["ChangeVideoProfilePicture"][msg._from]
                            cl.downloadObjectMsg(msg_id,'path','image.jpg')
                            cl.nadyacantikimut('video.mp4','image.jpg')
                            cl.sendMessage(msg.to,"Change Video Profile Success!!!")
                            
               if msg.contentType == 1:
                  if msg._from in mid:
                     if settings["Addimage"]["status"] == True:
                         path = cl.downloadObjectMsg(msg.id)
                         images[settings["Addimage"]["name"]] = str(path)
                         f = codecs.open("image.json","w","utf-8")
                         json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                         cl.sendMessage(msg.to, "Berhasil menambahkan gambar {}".format(str(settings["Addimage"]["name"])))
                         settings["Addimage"]["status"] = False
                         settings["Addimage"]["name"] = ""
               if msg.contentType == 2:
                  if msg._from in mid:
                     if settings["Addvideo"]["status"] == True:
                         path = cl.downloadObjectMsg(msg.id)
                         videos[settings["Addvideo"]["name"]] = str(path)
                         f = codecs.open("video.json","w","utf-8")
                         json.dump(videos, f, sort_keys=True, indent=4, ensure_ascii=False)
                         cl.sendMessage(msg.to, "Berhasil menambahkan video {}".format(str(settings["Addvideo"]["name"])))
                         settings["Addvideo"]["status"] = False
                         settings["Addvideo"]["name"] = ""
               if msg.contentType == 7:
                  if msg._from in mid:
                     if settings["Addsticker"]["status"] == True:
                         stickers[settings["Addsticker"]["name"]] = {"STKID":msg.contentMetadata["STKID"],"STKPKGID":msg.contentMetadata["STKPKGID"]}
                         f = codecs.open("sticker.json","w","utf-8")
                         json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                         cl.sendMessage(msg.to, "Berhasil menambahkan sticker {}".format(str(settings["Addsticker"]["name"])))
                         settings["Addsticker"]["status"] = False
                         settings["Addsticker"]["name"] = ""
               if msg.contentType == 3:
                  if msg._from in mid:
                     if settings["Addaudio"]["status"] == True:
                         path = cl.downloadObjectMsg(msg.id)
                         audios[settings["Addaudio"]["name"]] = str(path)
                         f = codecs.open("audio.json","w","utf-8")
                         json.dump(audios, f, sort_keys=True, indent=4, ensure_ascii=False)
                         cl.sendMessage(msg.to, "Berhasil menambahkan mp3 {}".format(str(settings["Addaudio"]["name"])))
                         settings["Addaudio"]["status"] = False
                         settings["Addaudio"]["name"] = ""
               if msg.contentType == 0:
                  if settings["autoRead"] == True:
                      cl.sendChatChecked(msg.to, msg_id)
                      print ("Read")
                  if text is None:
                      return
                  else:
                         for sticker in stickers:
                          if msg._from in mid:
                            if text.lower() == sticker:
                               sid = stickers[text.lower()]["STKID"]
                               spkg = stickers[text.lower()]["STKPKGID"]
                               cl.sendSticker(to, spkg, sid)
                         for image in images:
                          if msg._from in mid:
                            if text.lower() == image:
                               cl.sendImage(msg.to, images[image])
                         for audio in audios:
                          if msg._from in mid:
                            if text.lower() == audio:
                               cl.sendAudio(msg.to, audios[audio])
                         for video in videos:
                          if msg._from in mid:
                            if text.lower() == video:
                               cl.sendVideo(msg.to, videos[video])
               if msg.contentType == 13:
                 if msg._from in owner:
                  if wait["addbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        cl.sendMessage(msg.to,"Already in bot")
                        wait["addbots"] = True
                    else:
                        Bots.append(msg.contentMetadata["mid"])
                        wait["addbots"] = True
                        cl.sendMessage(msg.to,"Succes add bot")
                 if wait["dellbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        Bots.remove(msg.contentMetadata["mid"])
                        cl.sendMessage(msg.to,"Succes delete bot")
                    else:
                        wait["dellbots"] = True
                        cl.sendMessage(msg.to,"Nothing in bot")
#ADD STAFF
                 if msg._from in owner or msg._from in admin:
                  if wait["addstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        cl.sendMessage(msg.to,"Already in stafflist")
                        wait["addstaff"] = True
                    else:
                        staff.append(msg.contentMetadata["mid"])
                        wait["addstaff"] = True
                        cl.sendMessage(msg.to,"Succes add to staff")
                 if wait["dellstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        staff.remove(msg.contentMetadata["mid"])
                        cl.sendMessage(msg.to,"Succes expel to staff")
                        wait["dellstaff"] = True
                    else:
                        wait["dellstaff"] = True
                        cl.sendMessage(msg.to,"Nothing in staff")
#ADD ADMIN
                 if msg._from in owner:
                  if wait["addadmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        cl.sendMessage(msg.to,"Already in Admin")
                        wait["addadmin"] = True
                    else:
                        admin.append(msg.contentMetadata["mid"])
                        wait["addadmin"] = True
                        cl.sendMessage(msg.to,"Succes Add to Admin")
                 if wait["delladmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        admin.remove(msg.contentMetadata["mid"])
                        cl.sendMessage(msg.to,"Succes to expel admin")
                    else:
                        wait["delladmin"] = True
                        cl.sendMessage(msg.to,"Contact itu bukan admin")
#ADD BLACKLIST
                 if msg._from in owner:
                  if wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendMessage(msg.to,"Already in blacklist")
                        wait["wblacklist"] = True
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = True
                        cl.sendMessage(msg.to,"Succes add to blacklist")
                  if wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendMessage(msg.to,"Succes delete blacklist")
                    else:
                        wait["dblacklist"] = True
                        cl.sendMessage(msg.to,"Nothing in blacklist")
#TALKBAN
                 if msg._from in owner:
                  if wait["Talkwblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        cl.sendMessage(msg.to,"Already in Talkban")
                        wait["Talkwblacklist"] = True
                    else:
                        wait["Talkblacklist"][msg.contentMetadata["mid"]] = True
                        wait["Talkwblacklist"] = True
                        cl.sendMessage(msg.to,"Succes add to Talkban")
                  if wait["Talkdblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        del wait["Talkblacklist"][msg.contentMetadata["mid"]]
                        cl.sendMessage(msg.to,"Succes delete Talkban")
                    else:
                        wait["Talkdblacklist"] = True
                        cl.sendMessage(msg.to,"Nothing in Talkban")
#UPDATE FOTO
               if msg.contentType == 1:
                 if msg._from in owner:
                    if Setmain["Addimage"] == True:
                        msgid = msg.id
                        fotoo = "https://obs.line-apps.com/talk/m/download.nhn?oid="+msgid
                        headers = cl.Talk.Headers
                        r = requests.get(fotoo, headers=headers, stream=True)
                        if r.status_code == 200:
                            path = os.path.join(os.path.dirname(__file__), 'dataPhotos/%s.jpg' % Setmain["Img"])
                            with open(path, 'wb') as fp:
                                shutil.copyfileobj(r.raw, fp)
                            cl.sendMessage(msg.to, "Succes add picture")
                        Setmain["Img"] = {}
                        Setmain["Addimage"] = False

               if msg.toType == 2:
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   if settings["groupPicture"] == True:
                     path = cl.downloadObjectMsg(msg_id)
                     settings["groupPicture"] = False
                     cl.updateGroupPicture(msg.to, path)
                     cl.sendMessage(msg.to, "Succes change pict group")

               if msg.contentType == 1:
                 if msg._from in admin:
                        if Amid in Setmain["RAfoto"]:
                            path = ki.downloadObjectMsg(msg_id)
                            del Setmain["RAfoto"][Amid]
                            ki.updateProfilePicture(path)
                            ki.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Bmid in Setmain["Bfoto"]:
                            path = kk.downloadObjectMsg(msg_id)
                            del Setmain["RAfoto"][Bmid]
                            kk.updateProfilePicture(path)
                            kk.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Cmid in Setmain["RAfoto"]:
                            path = kc.downloadObjectMsg(msg_id)
                            del Setmain["RAfoto"][Cmid]
                            kc.updateProfilePicture(path)
                            kc.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Dmid in Setmain["RAfoto"]:
                            path = km.downloadObjectMsg(msg_id)
                            del Setmain["RAfoto"][Dmid]
                            km.updateProfilePicture(path)
                            km.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Emid in Setmain["RAfoto"]:
                            path = kb.downloadObjectMsg(msg_id)
                            del Setmain["RAfoto"][Emid]
                            kb.updateProfilePicture(path)
                            kb.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Zmid in Setmain["RAfoto"]:
                            path = sw.downloadObjectMsg(msg_id)
                            del Setmain["RAfoto"][Zmid]
                            sw.updateProfilePicture(path)
                            sw.sendMessage(msg.to,"Foto berhasil dirubah")
                            
               if msg.contentType == 1:
                 if msg._from in admin:
                   if settings["changePicture"] == True:
                     path1 = ki.downloadObjectMsg(msg_id)
                     path2 = kk.downloadObjectMsg(msg_id)
                     path3 = kc.downloadObjectMsg(msg_id)
                     path4 = km.downloadObjectMsg(msg_id)
                     path5 = kb.downloadObjectMsg(msg_id)
                     settings["changePicture"] = False
                     ki.updateProfilePicture(path1)
                     ki.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     kk.updateProfilePicture(path2)
                     kk.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     kc.updateProfilePicture(path3)
                     kc.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     km.updateProfilePicture(path4)
                     km.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     kb.updateProfilePicture(path5)
                     kb.sendMessage(msg.to, "Berhasil mengubah foto profile bot")

               if msg.contentType == 0:
                    if Setmain["autoRead"] == True:
                        cl.sendChatChecked(msg.to, msg_id)
                    if text is None:
                        return
                    else:
                        cmd = command(text)
                        if cmd == "help":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                               helpMessage = help()
                               cl.sendMessage(msg.to, str(helpMessage))
                                                                                       
                        if cmd == "on":
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                wait["selfbot"] = True
                                cl.sendMessage(msg.to, "Bot telah di aktifkan")
                                
                        elif cmd == "off":
                            if msg._from in owner or msg._from in admin:
                                wait["selfbot"] = False
                                cl.sendMessage(msg.to, "Bot off smentara waktu")
                                
                        elif cmd == 'vp':
                        	if msg._from in owner or msg._from in admin:
                                 me = cl.getContact(mid)
                                 cl.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
                                            
                        elif cmd == "help2":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                               helpMessage2 = helpbot()
                               cl.sendMessage(msg.to, str(helpMessage2))

                        elif cmd == "settings":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = "   ⏣⎊ S̶̭̗̞̙̿͑̽̆̃̒į̷̙̝̦̤̜̗́̉ͅl̸̛͓͋͋͆̍ę̶͇̮̦̣̖̙̘̪̉n̸͍̦͉̖̟͚̗̣̍̓̽̅̚ť̴̙͋ ̷̨̳̠͎̮̘͇̀̅̀͒̈́͊̕͝T̸̡̯̗̩̺͉̑́͛̌̒ͅé̶̡̱̯̮̯̊̏́̀̃͜a̴̭͓̫͚̐́̂̍̂̊̋̚m̸̨̨̹͎͍̳̥͆̓͗̿͐͗͑̿̓͠ ̴̠͐̂B̷̛̳͎̫̻̫̯̣͓̲͋̀͋̋͊̈͗͑o̵̲̾̈́͒͗t̴̢͍̫̰̠̞͖͍̬̑̊̽͒́̈́͗ͅ ⎊⏣\n\n"
                                if wait["sticker"] == True: md+="【✔】Sticker\n"
                                else: md+="【✘】Sticker\n"
                                if wait["contact"] == True: md+="【✔】Contact\n"
                                else: md+="【✘】Contact\n"
                                if wait["detectMention"] == True: md+="【✔】Respon\n"
                                else: md+="【✘】Respon\n"
                                if wait["autoJoin"] == True: md+="【✔】Autojoin\n"
                                else: md+="【✘】Autojoin\n"
                                if settings["autoJoinTicket"] == True: md+="【✔】Jointicket\n"
                                else: md+="【✘】Jointicket\n"
                                if settings["unsendMessage"] == True: md+="【✔】Unsend\n"
                                else: md+="【✘】Unsend\n"
                                if wait["autoAdd"] == True: md+="【✔】Autoadd\n"
                                else: md+="【✘】Autoadd\n"
                                if msg.to in welcome: md+="【✔】Welcome\n"
                                else: md+="【✘】Welcome\n"
                                if wait["autoLeave"] == True: md+="【✔】Autoleave\n"
                                else: md+="【✘】Autoleave\n"
                                if msg.to in protect["pqr"]: md+="【✔】Skurl\n"
                                else: md+="【✘】Skurl\n"
                                if msg.to in protect["proall"]: md+="【✔】Proall\n"
                                else: md+="【✘】Proall\n"
                                if msg.to in protect["protect"]: md+="【✔】Protect\n"
                                else: md+="【✘】Protect\n"
                                if msg.to in protect["pinv"]: md+="【✔】Skinvite\n"
                                else: md+="【✘】Skinvite\n"
                                if msg.to in protect["antijs"]: md+="【✔】Js\n"
                                else: md+="【✘】Js\n"
                                if msg.to in protectcancel: md+="【✔】Procancel\n"
                                else: md+="【✘】Procancel\n"
                                cl.sendMessage(msg.to, md+"\nDate : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nTime  "+ datetime.strftime(timeNow,'%H:%M:%S')+" ")                              
                                
                        elif cmd == "creator" or text.lower() == 'creator':
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                cl.sendText(msg.to,"Creator Kami")
                                ma = ""
                                for i in creator:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "about" or cmd == "informasi":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               sendMention(msg.to, sender, "🔴My Creator\n\n")
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': mid}, contentType=13)

                        elif cmd == "me" or text.lower() == 'me':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:                                               
                                msg.contentType = 13
                                msg.contentMetadata = {'mid': msg._from}
                                cl.sendMessage(msg.to, None, contentMetadata={'mid': msg._from}, contentType=13)
                                path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                                image = 'http://dl.profile.line.naver.jp'+path
                                cl.sendImageWithURL(msg.to, image)
                                                                       
                        elif text.lower() == "midku":
                               cl.sendMessage(msg.to, msg._from)
                        elif text.lower() == 'ass':
                               cl.sendMessage(msg.to, "Assalamu'alaikum Wr. Wb")
                               cl.sendMessage(msg.to, "السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                        elif text.lower() == 'wss':
                               cl.sendMessage(msg.to, "Wa'alaikumsallam.Wr,Wb")
                               cl.sendMessage(msg.to, "ُوَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ  ")
                        elif text.lower() == 'bot':
                               cl.sendMessage(msg.to, "On bos siap hajar😈")

                        elif ("Get id " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               cl.sendMessage(msg.to, "Nama : "+str(mi.displayName)+"\nMID : " +key1)
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)

                        elif ("Kepo " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               cl.sendMessage(msg.to, "Nama : "+str(mi.displayName)+"\nMid : " +key1+"\nStatus Msg"+str(mi.statusMessage))
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
                               if "videoProfile='{" in str(cl.getContact(key1)):
                                   cl.sendVideoWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath)+'/vp.small')
                               else:
                                   cl.sendImageWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath))

                        elif cmd  == "mybot":
                          if msg._from in admin:
                              cl.sendContact(to, mid)
                              cl.sendContact(to, Amid)
                              cl.sendContact(to, Bmid)
                              cl.sendContact(to, Cmid)
                              cl.sendContact(to, Dmid)
                              cl.sendContact(to, Emid)
                              cl.sendContact(to, Zmid)
                               
                        elif cmd  == "midbot":
                          if msg._from in admin:
                              cl.sendMessage(msg.to,mid)
                              ki.sendMessage(msg.to,Amid)
                              kk.sendMessage(msg.to,Bmid)
                              kc.sendMessage(msg.to,Cmid)
                              kb.sendMessage(msg.to,Dmid)
                              cl.sendMessage(msg.to,Emid)
                              cl.sendMessage(msg.to,Zmid)
                               
                        elif cmd == "reject":
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                              ginvited = cl.getGroupIdsInvited()
                              if ginvited != [] and ginvited != None:
                                  for gid in ginvited:
                                      cl.rejectGroupInvitation(gid)
                                      ki.rejectGroupInvitation(gid)
                                      ka.rejectGroupInvitation(gid)
                                  cl.sendMessage(to, "Succes reject {} ".format(str(len(ginvited))))
                                  ki.sendMessage(to, "Succes reject {} ".format(str(len(ginvited))))
                                  kk.sendMessage(to, "Succes reject {} ".format(str(len(ginvited))))
                                  kc.sendMessage(to, "Succes reject {} ".format(str(len(ginvited))))
                                  km.sendMessage(to, "Succes reject {} ".format(str(len(ginvited))))
                                  kb.sendMessage(to, "Succes reject {} ".format(str(len(ginvited))))
                              else:
                                  cl.sendMessage(to, "sᴇᴍᴜᴀ ɢʀᴜᴘ sᴜᴅᴀʜ ᴅɪʙᴀᴛᴀʟᴋᴀɴ")
                                  ki.sendMessage(to, "sᴇᴍᴜᴀ ɢʀᴜᴘ sᴜᴅᴀʜ ᴅɪʙᴀᴛᴀʟᴋᴀɴ")
                                  kk.sendMessage(to, "sᴇᴍᴜᴀ ɢʀᴜᴘ sᴜᴅᴀʜ ᴅɪʙᴀᴛᴀʟᴋᴀɴ")
                                  kc.sendMessage(to, "sᴇᴍᴜᴀ ɢʀᴜᴘ sᴜᴅᴀʜ ᴅɪʙᴀᴛᴀʟᴋᴀɴ")
                                  km.sendMessage(to, "sᴇᴍᴜᴀ ɢʀᴜᴘ sᴜᴅᴀʜ ᴅɪʙᴀᴛᴀʟᴋᴀɴ")
                                  kb.sendMessage(to, "sᴇᴍᴜᴀ ɢʀᴜᴘ sᴜᴅᴀʜ ᴅɪʙᴀᴛᴀʟᴋᴀɴ")

                        elif text.lower() == "hapuschat":
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               try:
                                   cl.removeAllMessages(op.param2)
                                   ki.removeAllMessages(op.param2)
                                   kk.removeAllMessages(op.param2)
                                   kc.removeAllMessages(op.param2)
                                   km.removeAllMessages(op.param2)
                                   kb.removeAllMessages(op.param2)
                                   cl.sendMessage(msg.to,"Bersih bos")
                                   ki.sendMessage(msg.to,"Bersih bos")
                                   kk.sendMessage(msg.to,"Bersih bos")
                                   kc.sendMessage(msg.to,"Bersih bos")
                                   km.sendMessage(msg.to,"Bersih bos")
                                   kb.sendMessage(msg.to,"Bersih bos")
                               except:
                                   pass

                        elif cmd.startswith("bcast: "):
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = cl.getGroupIdsJoined()
                               for group in saya:
                                   cl.sendMessage(group,"🔴Broadcast \n\n" + str(pesan))

                        elif text.lower() == "sname":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               cl.sendMessage(msg.to, "🔴 Sname \n\n" + str(Setmain["keyCommand"]) + " ")
                               
                        elif cmd.startswith("setsname "):
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   cl.sendMessage(msg.to, "Succes change Sname")
                               else:
                                   Setmain["keyCommand"] = str(key).lower()
                                   cl.sendMessage(msg.to, "🔴Sname change \n\nSname succes change to {}".format(str(key).lower()))

                        elif text.lower() == "reset sname":
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               Setmain["keyCommand"] = ""
                               cl.sendMessage(msg.to, "Succes Reset Sname ")

                        elif cmd == "restart":
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               cl.sendMessage(msg.to, "please wait")
                               Setmain["restartPoint"] = msg.to
                               restartBot()
                               cl.sendMessage(msg.to, "Done...")
                            
                        elif cmd == "time":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               eltime = time.time() - mulai
                               bot = "Active " +waktu(eltime)
                               cl.sendMessage(msg.to,bot)
                            
                        elif cmd == "ginfo":
                          if msg._from in owner or msg._from in admin or msg._from in staff:
                            try:
                                G = cl.getGroup(msg.to)
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                cl.sendMessage(msg.to, "Group Info\n\nNama Group : {}".format(G.name)+ "\nID Group : {}".format(G.id)+ "\nPembuat : {}".format(G.creator.displayName)+ "\nWaktu Dibuat : {}".format(str(timeCreated))+ "\nJumlah Member : {}".format(str(len(G.members)))+ "\nJumlah Pending : {}".format(gPending)+ "\nGroup Qr : {}".format(gQr)+ "\nGroup Ticket : {}".format(gTicket))
                                cl.sendMessage(msg.to, None, contentMetadata={'mid': G.creator.mid}, contentType=13)
                                cl.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)
                            except Exception as e:
                                cl.sendMessage(msg.to, str(e))

                        elif cmd.startswith("infogrup "):
                          if msg._from in owner or msg._from in admin:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                try:
                                    gCreator = G.creator.displayName
                                except:
                                    gCreator = "Tidak ditemukan"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += "Team Sempak Grup Info\n"
                                ret_ += "\nNama Group : {}".format(G.name)
                                ret_ += "\nID Group : {}".format(G.id)
                                ret_ += "\nPembuat : {}".format(gCreator)
                                ret_ += "\nWaktu Dibuat : {}".format(str(timeCreated))
                                ret_ += "\nJumlah Member : {}".format(str(len(G.members)))
                                ret_ += "\nJumlah Pending : {}".format(gPending)
                                ret_ += "\nGroup Qr : {}".format(gQr)
                                ret_ += "\nGroup Ticket : {}".format(gTicket)
                                ret_ += ""
                                cl.sendMessage(to, str(ret_))
                            except:
                                pass

                        elif cmd.startswith("infomem "):
                          if msg._from in owner or msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                no = 0
                                ret_ = ""
                                for mem in G.members:
                                    no += 1
                                    ret_ += "\n " ""+ str(no) + ". " + mem.displayName
                                cl.sendMessage(to,"Group Name : " + str(G.name) + " \n\nMember List \n" + ret_ + "\n\nTotal %i Members" % len(G.members))
                            except: 
                                pass

                        elif cmd.startswith("leave "):
                          if msg._from in owner or msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            group = groups[int(number)-1]
                            for i in group:
                                ginfo = cl.getGroup(i)
                                if ginfo == group:
                                    cl.leaveGroup(i)
                                    cl.sendMessage(msg.to,"Leave in groups " +str(ginfo.name))

                        elif cmd == "flist":
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               ma = ""
                               a = 0
                               gid = cl.getAllContactIds()
                               for i in gid:
                                   G = cl.getContact(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "" + str(a) + ". " +G.displayName+ "\n"
                               cl.sendMessage(msg.to,"🔴FRIEND LIST\n\n"+ma+"\nTotal"+str(len(gid))+"Friends")

                        elif cmd == "glist":
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               ma = ""
                               a = 0
                               gid = cl.getGroupIdsJoined()
                               for i in gid:
                                   G = cl.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "" + str(a) + ". " +G.name+ "\n"
                               cl.sendMessage(msg.to,"🔴GROUP LIST\n\n"+ma+"\nTotal"+str(len(gid))+" Groups")

                        elif cmd == "curl":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   cl.updateGroup(X)
                                   cl.sendMessage(msg.to, "Url Closed")

                        elif cmd == "ourl":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                if msg.toType == 2:
                                   x = cl.getGroup(msg.to)
                                   if x.preventedJoinByTicket == True:
                                      x.preventedJoinByTicket = False
                                      cl.updateGroup(x)
                                   gurl = cl.reissueGroupTicket(msg.to)
                                   cl.sendMessage(msg.to, "Nama : "+str(x.name)+ "\nUrl grup : http://line.me/R/ti/g/"+gurl)

#===========BOT UPDATE============#
                        elif cmd == "upgrup":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                              if msg.toType == 2:
                                settings["groupPicture"] = True
                                cl.sendMessage(msg.to,"Send Picture")                     
                                
                        elif cmd == "upfoto":
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                settings["RAfoto"][mid] = True
                                cl.sendMessage(msg.to,"Send picture")
                                
                        elif cmd == "updatefoto":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["RAfoto"][mid] = True
                                cl.sendMessage(msg.to,"Send picture")
                      
                        elif cmd == "1up":
                            if msg._from in admin:
                                settings["RAfoto"][Amid] = True
                                cl.sendMessage(msg.to,"Send picture")
                                
                        elif cmd == "2up":
                            if msg._from in admin:
                                settings["RAfoto"][Bmid] = True
                                cl.sendMessage(msg.to,"Send picture")
                                
                        elif cmd == "3up":
                            if msg._from in admin:
                                settings["RAfoto"][Cmid] = True
                                cl.sendMessage(msg.to,"Send picture")
                                
                        elif cmd == "4up":
                            if msg._from in admin:
                                settings["RAfoto"][Dmid] = True
                                cl.sendMessage(msg.to,"Send picture")

                        elif cmd == "5up":
                            if msg._from in admin:
                                settings["RAfoto"][Emid] = True
                                cl.sendMessage(msg.to,"Send picture")

                        elif cmd == "6up":
                            if msg._from in admin:
                                settings["RAfoto"][Zmid] = True
                                cl.sendMessage(msg.to,"Send picture")

#===========BOT UPDATE============#
                        elif cmd == "mention" or text.lower() == 'cek jones':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                               group = cl.getGroup(msg.to)
                               nama = [contact.mid for contact in group.members]
                               nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                               if jml <= 20:
                                   mentionMembers(msg.to, nama)
                               if jml > 20 and jml < 20:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, len(nama)-1):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                               if jml > 20 and jml < 40:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, len(nama)-1):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                               if jml > 40 and jml < 60:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 60):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, len(nama)-1):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                               if jml > 60 and jml < 80:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 60):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 80):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, len(nama)-1):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                               if jml > 80 and jml < 100:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 60):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 80):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 100):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)

                        elif cmd == "botlist":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                ma = ""
                                a = 0
                                for m_id in Bots:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"🔴Botlist🔴\n\n\n"+ma+"\n%s Bots" %(str(len(Bots))))

                        elif cmd == "silent":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    ginfo = cl.getGroup(msg.to)
                                    cl.inviteIntoGroup(msg.to, [Zmid])
                                    cl.sendMessage(msg.to,"Redy stay "+str(ginfo.name)+" Siap Backup")
                                except:
                                    pass

                        elif cmd == "stafflist":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                ma = ""
                                mb = ""
                                mc = ""
                                a = 0
                                b = 0
                                c = 0
                                for m_id in owner:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                for m_id in admin:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +cl.getContact(m_id).displayName + "\n"
                                for m_id in staff:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"🔴Adminlist🔴\n\n🔴Owner\n"+ma+"\n🔴Admin\n"+mb+"\n🔴Staff:\n"+mc+"\n%s Adminlist" %(str(len(owner)+len(admin)+len(staff))))

                        elif cmd == "protectlist":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                md = ""
                                mg = ""
                                mf = ""
                                a = 0
                                b = 0
                                c = 0
                                d = 0
                                g = 0
                                f = 0
                                gid = protect["pqr"]
                                for group in gid:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getGroup(group).name + "\n"
                                gid = protect["protect"]
                                for group in gid:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +cl.getGroup(group).name + "\n"
                                gid = protect["proall"]
                                for group in gid:
                                    d = d + 1
                                    end = '\n'
                                    md += str(d) + ". " +cl.getGroup(group).name + "\n"
                                gid = protectcancel
                                for group in gid:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +cl.getGroup(group).name + "\n"
                                gid = protect["pinv"]
                                for group in gid:
                                    f = f + 1
                                    end = '\n'
                                    mf += str(f) + ". " +cl.getGroup(group).name + "\n"
                                gid = protect["antijs"]
                                for group in gid:
                                    g = g + 1
                                    end = '\n'
                                    mg += str(g) + ". " +cl.getGroup(group).name + "\n"
                                cl.sendMessage(msg.to,"Settings Protection\n\nProurl :\n"+ma+"\nProall:\n"+mb+"\nProtect:\n"+mf+"\nProtect Cancel:\n"+mc+"\nProinvite:\n"+md+"\nProtectJS:\n"+mg+"\nProtectlist %s Grup protect" %(str(len(protect["pqr"])+len(protect["protect"])+len(protect["antijs"])+len(protect["proall"])+len(protectcancel)+len(protect["pinv"]))))

                        elif cmd == "skname":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                ki.sendMessage(msg.to,responsename1)
                                kk.sendMessage(msg.to,responsename2)
                                kc.sendMessage(msg.to,responsename3)
                                km.sendMessage(msg.to,responsename4)
                                kb.sendMessage(msg.to,responsename5)
                                
                                
                        elif cmd == "masuk":
                         if msg._from in admin:
                           if msg.toType == 2:
                               group = cl.getGroup(to)
                               group.preventedJoinByTicket = False
                               cl.updateGroup(group)
                               invsend = 0
                               ticket = cl.reissueGroupTicket(to)
                               ki.acceptGroupInvitationByTicket(to,format(str(ticket)))
                               time.sleep(0.01)
                               kk.acceptGroupInvitationByTicket(to,format(str(ticket)))
                               time.sleep(0.01)
                               kc.acceptGroupInvitationByTicket(to,format(str(ticket)))
                               time.sleep(0.01)
                               km.acceptGroupInvitationByTicket(to,format(str(ticket)))
                               time.sleep(0.01)
                               kb.acceptGroupInvitationByTicket(to,format(str(ticket)))
                               time.sleep(0.01)
                               
                        elif cmd == "name":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ki.sendMessage(msg.to, "۞❂✪₷ιlΣƬ ₭ιll₠₹ ⋮➲➤➤")
                               kk.sendMessage(msg.to, "۞❂✪₷ιlΣƬ ₭ιll₠₹ ⋮➲➤➤")
                               kc.sendMessage(msg.to, "۞❂✪₷ιlΣƬ ₭ιll₠₹ ⋮➲➤➤")
                               km.sendMessage(msg.to, "۞❂✪₷ιlΣƬ ₭ιll₠₹ ⋮➲➤➤")
                               kb.sendMessage(msg.to, "۞❂✪₷ιlΣƬ ₭ιll₠₹ ⋮➲➤➤")
                 
                        elif cmd == "bye":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ki.sendMessage(msg.to, "Pulang dulu "+str(G.name))
                                ki.leaveGroup(msg.to)
                                
                        elif cmd == "bye1":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                kk.sendMessage(msg.to, "Pulang dulu "+str(G.name))
                                kk.leaveGroup(msg.to)
                                
                        elif cmd == "bye2":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                kc.sendMessage(msg.to, "Pulang dulu "+str(G.name))
                                kc.leaveGroup(msg.to)
                                
                        elif cmd == "bye3":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                km.sendMessage(msg.to, "Pulang dulu "+str(G.name))
                                km.leaveGroup(msg.to)
                                
                        elif cmd == "bye4":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                kb.sendMessage(msg.to, "Pulang dulu "+str(G.name))
                                kb.leaveGroup(msg.to)
                                
                        elif cmd == "kicker lv":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                sw.sendMessage(msg.to, "Pulang dulu "+str(G.name))
                                sw.leaveGroup(msg.to)
                                
                        elif cmd == "kicker in":
                          if msg._from in admin:
                           if msg.toType == 2:
                               group = cl.getGroup(to)
                               group.preventedJoinByTicket = False
                               cl.updateGroup(group)
                               invsend = 0
                               ticket = cl.reissueGroupTicket(to)
                               sw.acceptGroupInvitationByTicket(to,format(str(ticket)))
                               time.sleep(0.01)
                          

                        elif cmd == ".bye":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                G = cl.getGroup(msg.to)
                                cl.sendMessage(msg.to, "Makasih sudah invit\nketemu lain waktu... "+str(G.name))
                                cl.leaveGroup(msg.to)
                                
                        elif cmd == "pulang":
                           if wait["selfbot"] == True:
                            if msg._from in admin:
                               ki.leaveGroup(msg.to)
                               kk.leaveGroup(msg.to)
                               kc.leaveGroup(msg.to)
                               km.leaveGroup(msg.to)
                               kb.leaveGroup(msg.to)
                               

                        elif cmd.startswith("leave "):
                            if msg._from in admin or msg._from in owner:
                                proses = text.split(" ")
                                ng = text.replace(proses[0] + " ","")
                                gid = cl.getGroupIdsJoined()
                                for i in gid:
                                    h = cl.getGroup(i).name
                                    if h == ng:
                                        cl.sendMessage(i, " Silahkan invite Ownernya ")
                                        cl.leaveGroup(i)
                                        cl.sendMessage(to,"Succes leave group " +h)

                        elif cmd == "timerespon":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                get_group_time_start = time.time()
                                get_group = cl.getGroupIdsJoined()
                                get_group_time = time.time() - get_group_time_start
                                get_contact_time_start = time.time()
                                get_contact = cl.getContact(mid)
                                get_contact_time = time.time() - get_contact_time_start
                                cl.sendMessage(msg.to, "●Time Respon●\n\n ●Get Profile\n   %.10f\n ●Get Contact\n   %.10f\n ●Get Group\n   %.10f" % (get_profile_time/3,get_contact_time/3,get_group_time/3))

                        elif cmd == "speed" or cmd == "sp":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               start = time.time()                               
                               cl.sendMessage(msg.to, "Prosess....")                               
                               elapsed_time = time.time() - start
                               cl.sendMessage(msg.to, "Time:\n{}".format(str(elapsed_time)))
                               
                        elif cmd == "lurk:on":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 Setmain['RAreadPoint'][msg.to] = msg_id
                                 Setmain['RAreadMember'][msg.to] = {}
                                 cl.sendMessage(msg.to, "Lurking berhasil diaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "lurk:off":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 del Setmain['RAreadPoint'][msg.to]
                                 del Setmain['RAreadMember'][msg.to]
                                 cl.sendMessage(msg.to, "Lurking berhasil dinoaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "lurkers":
                          if msg._from in admin:
                            if msg.to in Setmain['RAreadPoint']:
                                if Setmain['RAreadMember'][msg.to] != {}:
                                    aa = []
                                    for x in Setmain['RAreadMember'][msg.to]:
                                        aa.append(x)
                                    try:
                                        arrData = ""
                                        textx = "  [ Result {} member ]    \n\n  [ Lurkers ]\n1. ".format(str(len(aa)))
                                        arr = []
                                        no = 1
                                        b = 1
                                        for i in aa:
                                            b = b + 1
                                            end = "\n"
                                            mention = "@x\n"
                                            slen = str(len(textx))
                                            elen = str(len(textx) + len(mention) - 1)
                                            arrData = {'S':slen, 'E':elen, 'M':i}
                                            arr.append(arrData)
                                            tz = pytz.timezone("Asia/Jakarta")
                                            timeNow = datetime.now(tz=tz)
                                            textx += mention
                                            if no < len(aa):
                                                no += 1
                                                textx += str(b) + ". "
                                            else:
                                                try:
                                                    no = "[ {} ]".format(str(cl.getGroup(msg.to).name))
                                                except:
                                                    no = "  "
                                        msg.to = msg.to
                                        msg.text = textx+"\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"
                                        msg.contentMetadata = {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}
                                        msg.contentType = 0
                                        cl.sendMessage1(msg)
                                    except:
                                        pass
                                    try:
                                        del Setmain['RAreadPoint'][msg.to]
                                        del Setmain['RAreadMember'][msg.to]
                                    except:
                                        pass
                                    Setmain['RAreadPoint'][msg.to] = msg.id
                                    Setmain['RAreadMember'][msg.to] = {}
                                else:
                                    cl.sendMessage(msg.to, "User kosong...")
                            else:
                                cl.sendMessage(msg.to, "Ketik lurking on dulu")

                        elif cmd == "sider on":
                          if wait["selfbot"] == True:
                           if msg._from in owner or msg._from in admin or msg._from in staff:
                              try:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cl.sendMessage(msg.to, "Cek sider diaktifkan\n\nDate "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nTime  "+ datetime.strftime(timeNow,'%H:%M:%S')+" ")
                                  del cctv['point'][msg.to]
                                  del cctv['sidermem'][msg.to]
                                  del cctv['cyduk'][msg.to]
                              except:
                                  pass
                              cctv['point'][msg.to] = msg.id
                              cctv['sidermem'][msg.to] = ""
                              cctv['cyduk'][msg.to]=True

                        elif cmd == "sider off":
                          if wait["selfbot"] == True:
                           if msg._from in owner or msg._from in admin or msg._from in staff:
                              if msg.to in cctv['point']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cctv['cyduk'][msg.to]=False
                                  cl.sendMessage(msg.to, "Cek sider dinonaktifkan\n\nDate "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nTime  "+ datetime.strftime(timeNow,'%H:%M:%S')+" ")
                              else:
                                  cl.sendMessage(msg.to, "Sudak tidak aktif")

#===========add img============#                                                        
                        elif cmd == "changedual":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["ChangeVideoProfilevid"][msg._from] = True
                                cl.sendMessage(msg.to,"Send Videonya...")
                                
                        elif cmd.startswith("changedualurl: "):
                            if msg._from in admin:
                                sep = msg.text.split(" ")
                                url = msg.text.replace(sep[0] + " ","")                            
                                cl.downloadFileURL(url,'path','video.mp4')
                                settings["ChangeVideoProfilePicture"][msg._from] = True
                                cl.sendMessage(msg.to, "Send Gambarnya.....")
                                
                        elif cmd.startswith("addimg"):
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name not in images:
                                    settings["Addimage"]["status"] = True
                                    settings["Addimage"]["name"] = str(name.lower())
                                    images[str(name.lower())] = ""
                                    f = codecs.open("image.json","w","utf-8")
                                    json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    cl.sendMessage(to, "Silahkan kirim fotonya...")
                                else:
                                    cl.sendMessage(to, "Foto itu sudah dalam list")
                        elif cmd.startswith("dellimg "):
                               sep = text.split(" ")
                               name = text.replace(sep[0] + " ","")
                               name = name.lower()
                               if name in images:
                                   cl.deleteFile(images[str(name.lower())])
                                   del images[str(name.lower())]
                                   f = codecs.open("image.json","w","utf-8")
                                   json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                   cl.sendMessage(to, "Berhasil menghapus {}".format( str(name.lower())))
                               else:
                                   cl.sendMessage(to, "Foto itu tidak ada dalam list")

                        elif cmd == "listimage":
                                no = 0
                                ret_ = "Daftar Image\n\n"
                                for image in images:
                                    no += 1
                                    ret_ += str(no) + ". " + image.title() + "\n"
                                ret_ += "\nTotal {} Images".format(str(len(images)))
                                cl.sendMessage(to, ret_)
#==============add video==========================================================================
                        elif cmd.startswith("addvideo"):
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name not in images:
                                    settings["Addvideo"]["status"] = True
                                    settings["Addvideo"]["name"] = str(name.lower())
                                    images[str(name.lower())] = ""
                                    f = codecs.open("video.json","w","utf-8")
                                    json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    cl.sendMessage(to, "Silahkan kirim video nya...")
                                else:
                                    cl.sendMessage(to, "video itu sudah dalam list")
                        elif cmd.startswith("dellvideo "):
                               sep = text.split(" ")
                               name = text.replace(sep[0] + " ","")
                               name = name.lower()
                               if name in images:
                                   cl.deleteFile(images[str(name.lower())])
                                   del images[str(name.lower())]
                                   f = codecs.open("video.json","w","utf-8")
                                   json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                   cl.sendMessage(to, "Berhasil menghapus {}".format( str(name.lower())))
                               else:
                                   cl.sendMessage(to, "video itu tidak ada dalam list")

                        elif cmd == "listvideo":
                                no = 0
                                ret_ = "Daftar video\n\n"
                                for image in images:
                                    no += 1
                                    ret_ += str(no) + ". " + image.title() + "\n"
                                ret_ += "\nTotal {} video".format(str(len(images)))
                                cl.sendMessage(to, ret_)
#=========== [ Add Audio] ============#
                        elif cmd.startswith("addmp3 "):
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name not in audios:
                                    settings["Addaudio"]["status"] = True
                                    settings["Addaudio"]["name"] = str(name.lower())
                                    audios[str(name.lower())] = ""
                                    f = codecs.open("audio.json","w","utf-8")
                                    json.dump(audios, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    cl.sendMessage(to, "Silahkan kirim mp3 nya...") 
                                else:
                                    cl.sendMessage(to, "Mp3 itu sudah dalam list") 
                                
                        elif cmd.startswith("dellmp3 "):
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name in audios:
                                    cl.deleteFile(audios[str(name.lower())])
                                    del audios[str(name.lower())]
                                    f = codecs.open("audio.json","w","utf-8")
                                    json.dump(audios, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    cl.sendMessage(to, "Berhasil menghapus mp3 {}".format( str(name.lower())))
                                else:
                                    cl.sendMessage(to, "Mp3 itu tidak ada dalam list") 
                                 
                        elif cmd == "listmp3":
                                no = 0
                                ret_ = "? Daftar Lagu ?\n\n"
                                for audio in audios:
                                    no += 1
                                    ret_ += str(no) + ". " + audio.title() + "\n"
                                ret_ += "\nTotal {} Lagu".format(str(len(audios)))
                                cl.sendMessage(to, ret_)
 #=========== [ Add sticker] ============#                   
                        elif cmd.startswith("addsticker "):
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name not in stickers:
                                    settings["Addsticker"]["status"] = True
                                    settings["Addsticker"]["name"] = str(name.lower())
                                    stickers[str(name.lower())] = ""
                                    f = codecs.open("sticker.json","w","utf-8")
                                    json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    cl.sendMessage(to, "Silahkan kirim stickernya...") 
                                else:
                                    cl.sendMessage(to, "Sticker itu sudah dalam list") 
                                
                        elif cmd.startswith("dellsticker "):
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name in stickers:
                                    del stickers[str(name.lower())]
                                    f = codecs.open("sticker.json","w","utf-8")
                                    json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    cl.sendMessage(to, "Berhasil menghapus sticker {}".format( str(name.lower())))
                                else:
                                    cl.sendMessage(to, "Sticker itu tidak ada dalam list") 
                                                   
                        elif cmd == "liststicker":
                                no = 0
                                ret_ = " Daftar Sticker \n\n"
                                for sticker in stickers:
                                    no += 1
                                    ret_ += str(no) + ". " + sticker.title() + "\n"
                                ret_ += "\nTotal {} Stickers".format(str(len(stickers)))
                                cl.sendMessage(to, ret_)
#=========== [ Hiburan] ============#  
                        elif 'lc ' in text.lower():
                                try:
                                    typel = [1001,1002,1003,1004,1005,1006]
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    a = cl.getContact(u).mid
                                    s = cl.getContact(u).displayName
                                    hasil = cl.getHomeProfile(mid=a)
                                    st = hasil['result']['feeds']
                                    for i in range(len(st)):
                                        test = st[i]
                                        result = test['post']['postInfo']['postId']
                                        cl.likePost(str(sender), str(result), likeType=random.choice(typel))
                                        cl.createComment(str(sender), str(result), 'Auto Like by dhenza')
                                    cl.sendMessage(msg.to, 'Done Like+Comment '+str(len(st))+' Post From' + str(s))
                                except Exception as e:
                                    cl.sendMessage(receiver, str(e))
                                                                                 
                        elif text.lower().startswith("!music "):
                            try:
                                search = text.lower().replace("!musik","")
                                r = requests.get("https://rest.farzain.com/api/joox.php?apikey=rambu&id={}".format(urllib.parse.quote(search)))
                                data = r.text
                                data = json.loads(data)
                                info = data["info"]
                                audio = data["audio"]
                                hasil = "「 Hasil Musik 」\n"
                                hasil += "\nPenyanyi : {}".format(str(info["penyanyi"]))
                                hasil += "\nJudul : {}".format(str(info["judul"]))
                                hasil += "\nAlbum : {}".format(str(info["album"]))
                                hasil += "\n\nLink : \n1. Image : {}".format(str(data["gambar"]))
                                hasil += "\n\nLink : \n2. MP3 : {}".format(str(audio["mp3"]))
                                cl.sendImageWithURL(msg.to, str(data["gambar"]))
                                cl.sendMessage(msg.to, str(hasil))
                                cl.sendAudioWithURL(msg.to, str(audio["mp3"]))
                                cl.sendMessage(msg.to, "Searching mp3 done..")
                            except Exception as error:
                            	cl.sendMessage(msg.to, "「 Result Error 」\n" + str(error))
                        
                        elif cmd.startswith("profilesmule: "):
                          if msg._from in admin:    
                            try:
                                separate = msg.text.split(" ")
                                smule = msg.text.replace(separate[0] + " ","")
                                links = ("https://smule.com/"+smule)
                                ss = ("http://api2.ntcorp.us/screenshot/shot?url={}".format(urllib.parse.quote(links)))
                                cl.sendMessage(msg.to, "Sedang Mencari...")
                                time.sleep(2)
                                cl.sendMessage(msg.to, "ID Smule : "+smule+"\nLink : "+links)
                                cl.sendImageWithURL(msg.to, ss)
                            except Exception as error:
                                pass
                                
                        elif cmd.startswith("meme"):
                          if msg._from in admin:    
                            txt = msg.text.split("@")
                            image = ("http://memegen.link/"+txt[1].replace(" ","_")+"/"+txt[2].replace(" ","_")+"/"+txt[3].replace(" ","_")+".jpg?watermark=none")
                            cl.sendImageWithURL(msg.to, image)
                            
                        elif cmd.startswith("profileig: "):
                          if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                instagram = msg.text.replace(sep[0] + " ","")
                                html = requests.get('https://www.instagram.com/' + instagram + '/?')
                                soup = BeautifulSoup(html.text, 'html.parser')
                                data = soup.find_all('meta', attrs={'property':'og:description'})
                                text = data[0].get('content').split()
                                data1 = soup.find_all('meta', attrs={'property':'og:image'})
                                text1 = data1[0].get('content').split()
                                AR = text1[0].replace("s150x150/","")
                                user = "Name: " + text[-2] + "\n"
                                user1 = "Username: " + text[-1] + "\n"
                                followers = "Followers: " + text[0] + "\n"
                                following = "Following: " + text[2] + "\n"
                                post = "Post: " + text[4] + "\n"
                                link = "Link: " + "https://www.instagram.com/" + instagram
                                detail = "========INSTAGRAM INFO ========\n"
                                details = "\n========INSTAGRAM INFO ========"
                                cl.sendMessage(msg.to, detail + user + user1 + followers + following + post + link + details)
                                cl.sendImageWithURL(msg.to, AR)
                            except Exception as njer:
                                cl.sendMessage(msg.to, str(njer))
                                                                                    
                        elif cmd.startswith("ytmp4: "):
                          if msg._from in owner or msg._from in admin or msg._from in staff:
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = msg.text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                search_url="https://www.youtube.com/results?search_query="
                                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                sb_url = search_url + query
                                sb_get = requests.get(sb_url, headers = mozhdr)
                                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                x = (yt_links[1])
                                yt_href =  x.get("href")
                                yt_href = yt_href.replace("watch?v=", "")
                                qx = "https://youtu.be" + str(yt_href)
                                vid = pafy.new(qx)
                                stream = vid.streams
                                best = vid.getbest()
                                best.resolution, best.extension
                                for s in stream:
                                    me = best.url
                                    hasil = ""
                                    title = "Judul [ " + vid.title + " ]"
                                    author = '\n\nAuthor : ' + str(vid.author)
                                    durasi = '\nDuration : ' + str(vid.duration)
                                    suka = '\nLikes : ' + str(vid.likes)
                                    rating = '\nRating : ' + str(vid.rating)
                                    deskripsi = '\nDeskripsi : ' + str(vid.description)
                                cl.sendVideoWithURL(msg.to, me)
                                cl.sendMessage(msg.to,title+ author+ durasi+ suka+ rating+ deskripsi)
                            except Exception as e:
                                cl.sendMessage(msg.to,str(e))
                                
                        elif cmd.startswith("img food: "):
                          if msg._from in admin:
                                query = msg.text.replace("img food: ","")
                                r = requests.get("https://cryptic-ridge-9197.herokuapp.com/api/imagesearch/" + query + "?offset=1")
                                data=r.text
                                data=json.loads(r.text)
                                if data != []:
                                    for food in data:
                                        cl.sendImageWithURL(msg.to, str(food["url"]))
                        
                        elif cmd.startswith("cekdate: "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            tanggal = msg.text.replace(sep[0] + " ","")
                            r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                            data=r.text
                            data=json.loads(data)
                            lahir = data["data"]["lahir"]
                            usia = data["data"]["usia"]
                            ultah = data["data"]["ultah"]
                            zodiak = data["data"]["zodiak"]
                            cl.sendMessage(msg.to,"Informasi™\n\n"+"Date Of Birth : "+lahir+"\nAge : "+usia+"\nUltah : "+ultah+"\nZodiak : "+zodiak)

                        elif cmd.startswith("clone "):
                           if msg._from in admin:
                             if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                for mention in mentionees:
                                    contact = mention["M"]
                                    break
                                try:
                                    cl.cloneContactProfile(contact)
                                    ryan = cl.getContact(contact)
                                    zx = ""
                                    zxc = ""
                                    zx2 = []
                                    xpesan =  "「 Clone Profile 」\nTarget nya "
                                    ret_ = "Berhasil clone profile target"
                                    ry = str(ryan.displayName)
                                    pesan = ''
                                    pesan2 = pesan+"@x \n"
                                    xlen = str(len(zxc)+len(xpesan))
                                    xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    text = xpesan + zxc + ret_ + ""
                                    cl.sendMessage(to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                except:
                                    cl.sendMessage(msg.to, "Gagal clone profile")
                            
                        elif text.lower() == 'restore':
                           if msg._from in admin:
                              try:
                                  lineProfile.displayName = str(myProfile["displayName"])
                                  lineProfile.statusMessage = str(myProfile["statusMessage"])
                                  lineProfile.pictureStatus = str(myProfile["pictureStatus"])
                                  cl.updateProfileAttribute(8, lineProfile.pictureStatus)
                                  cl.updateProfile(lineProfile)
                                  sendMention(msg.to, sender, "「 Restore Profile 」\nNama ", " \nBerhasil restore profile")
                              except:
                                  cl.sendMessage(msg.to, "Gagal restore profile")

                        elif cmd.startswith("jumlah: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                wait["limit"] = num
                                cl.sendMessage(msg.to,"Spamtag change to " +strnum)

                        elif cmd.startswith("spamcall: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                wait["limit"] = num
                                cl.sendMessage(msg.to,"Total Spamcall Diubah Menjadi " +strnum)

                        elif cmd.startswith("spamtag "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    zx = ""
                                    zxc = " "
                                    zx2 = []
                                    pesan2 = "@a"" "
                                    xlen = str(len(zxc))
                                    xlen2 = str(len(zxc)+len(pesan2)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':key1}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    msg.contentType = 0
                                    msg.text = zxc
                                    lol = {'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                                    msg.contentMetadata = lol
                                    jmlh = int(wait["limit"])
                                    if jmlh <= 1000:
                                        for x in range(jmlh):
                                            try:
                                                cl.sendMessage(msg)
                                            except Exception as e:
                                                cl.sendMessage(msg.to,str(e))
                                    else:
                                        cl.sendMessage(msg.to,"Jumlah melebihi 1000")
                        
                        elif cmd == "spamcall":
                          if wait["selfbot"] == True:
                           if msg._from in owner:
                             if msg.toType == 2:
                                group = cl.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                cl.sendMessage(msg.to, "Berhasil mengundang {} undangan Call Grup".format(str(wait["limit"])))
                                call.acquireGroupCallRoute(to)
                                call.inviteIntoGroupCall(to, contactIds=members)
                                        
                        elif cmd == "spamcall":
                          if wait["selfbot"] == True:
                           if msg._from in owner:
                             if msg.toType == 2:
                                group = cl.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                jmlh = int(wait["limit"])
                                cl.sendMessage(msg.to, "Berhasil mengundang {} undangan Call Grup".format(str(wait["limit"])))
                                if jmlh <= 1000:
                                  for x in range(jmlh):
                                     try:
                                        call.acquireGroupCallRoute(to)
                                        call.inviteIntoGroupCall(to, contactIds=members)
                                     except Exception as e:
                                        cl.sendMessage(msg.to,str(e))
                                else:
                                    cl.sendMessage(msg.to,"Jumlah melebihi batas")
                                    
                        elif cmd.startswith("spaminvid"):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    dan = text.split("|")
                                    userid = dan[1]
                                    namagrup = dan[2]
                                    jumlah = int(dan[3])
                                    grups = cl.groups
                                    tgb = cl.findContactsByUserid(userid)
                                    cl.findAndAddContactsByUserid(userid)
                                    if jumlah <= 1000:
                                        for var in range(0,jumlah):
                                            try:
                                                cl.createGroup(str(namagrup), [tgb.mid])
                                                for i in grups:
                                                	grup = cl.getGroup(i)
                                                	if grup.name == namagrup:
                                                	    cl.inviteIntoGroup(grup.id, [tgb.mid])
                                                	    cl.leaveGroup(grup.id)
                                                	    cl.sendText(to,"@! sukses spam grup!\n\nkorban: @!\njumlah: {}\nnama grup: {}".format(jumlah, str(namagrup)), [sender, tgb.mid])
                                            except Exception as e:
                                                cl.sendText(msg.to,str(e))

                        elif 'Gift: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Gift: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      cl.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)

                        elif 'Spam: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Spam: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      cl.sendMessage(midd, str(Setmain["RAmessage1"]))

                        elif 'ID line: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              msgs = msg.text.replace('ID line: ','')
                              conn = cl.findContactsByUserid(msgs)
                              if True:
                                  cl.sendMessage(msg.to, "http://line.me/ti/p/~" + msgs)
                                  cl.sendMessage(msg.to, None, contentMetadata={'mid': conn.mid}, contentType=13)

#===========Protection============#
                        elif 'Welcome ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Welcome ','')
                              if spl == 'on':
                                  if msg.to in welcome:
                                       msgs = "Welcome Msg sudah aktif"
                                  else:
                                       welcome.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Welcome Msg diaktifkan\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in welcome:
                                         welcome.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Welcome Msg dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Welcome Msg sudah tidak aktif"
                                    cl.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Skurl ' in msg.text:
                           if msg._from in owner or msg._from in admin:
                              spl = msg.text.replace('Skurl ','')
                              if spl == 'on':
                                  if msg.to in protect["pqr"]:
                                       msgs = "SKurl has been active"
                                  else:
                                       protect["pqr"].append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Skurl telah active\n\ndi group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "Activated\n\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protect["pqr"]:
                                         protect["pqr"].remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Skurl deactive\n\nIn Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Skurl has been deactive"
                                    cl.sendMessage(msg.to, "Nonactive\n\n" + msgs)

                        elif 'Protect ' in msg.text:
                           if msg._from in owner or msg._from in admin:
                              spl = msg.text.replace('Protect ','')
                              if spl == 'on':
                                  if msg.to in protect["protect"]:
                                       msgs = "Protect has been active"
                                  else:
                                       protect["protect"].append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect Active\n\nIn group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "Activated\n\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protect["protect"]:
                                         protect["protect"].remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect deactive\n\nIn group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect has been disable"
                                    cl.sendMessage(msg.to, "Nonactive\n\n" + msgs)

                        elif 'Proall ' in msg.text:
                           if msg._from in owner or msg._from in admin:
                              spl = msg.text.replace('Proall ','')
                              if spl == 'on':
                                  if msg.to in protect["proall"]:
                                       msgs = "Proall has been active"
                                  else:
                                       protect["proall"].append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect all active\n\nIn group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "Activated \n\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protect["proall"]:
                                         protect["proall"].remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect all deactive\n\nIn group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect all has been disable"
                                    cl.sendMessage(msg.to, "Nonactive\n\n" + msgs)

                        elif 'Procancel ' in msg.text:
                           if msg._from in owner or msg._from in admin:
                              spl = msg.text.replace('Procancel ','')
                              if spl == 'on':
                                  if msg.to in protectcancel:
                                       msgs = "Protect cancel has been active "
                                  else:
                                       protectcancel.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect cancel active\n\nIn group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "Activated\n\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect cancel deactive\n\nIn group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect cancel has been disable"
                                    cl.sendMessage(msg.to, "Nonactive\n\n" + msgs)

                        elif 'Skinvite ' in msg.text:
                           if msg._from in owner or msg._from in admin:
                              spl = msg.text.replace('Skinvite ','')
                              if spl == 'on':
                                  if msg.to in protect["pinv"]:
                                       msgs = "skinvite has been active"
                                  else:
                                       protect["pinv"].append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "skurl active\n\nIn group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "Activated \n\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protect["pinv"]:
                                         protect["pinv"].remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "skinvite deactive\nIn group : " +str(ginfo.name)
                                    else:
                                         msgs = "skinvite has been disable"
                                    cl.sendMessage(msg.to, "Nonactive\n\n" + msgs)

                        elif 'Js ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Js ','')
                              if spl == 'on':
                                  if msg.to in protect["antijs"]:
                                       msgs = "Protectjs has been active"
                                  else:
                                       protect["antijs"].append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Anti kicker \n\naktif di group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "active\n\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protect["antijs"]:
                                         protect["antijs"].remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Anti kicker off\n\ndi group : " +str(ginfo.name)
                                    else:
                                         msgs = "Anti kicker off "
                                    cl.sendMessage(msg.to, "nonactive\n" + msgs)

                        elif 'Allpro ' in msg.text:
                           if msg._from in owner or msg._from in admin:
                              spl = msg.text.replace('Allpro ','')
                              if spl == 'on':
                                  if msg.to in protect["pqr"]:
                                       msgs = ""
                                  else:
                                       protect["pqr"].append(msg.to)
                                  if msg.to in protect["protect"]:
                                      msgs = ""
                                  else:
                                      protect["protect"].append(msg.to)
                                  if msg.to in protect["pinv"]:
                                      msgs = ""
                                  else:
                                      protect["pinv"].append(msg.to)
                                  if msg.to in protect["antijs"]:
                                      msgs = ""
                                  else:
                                      protect["antijs"].append(msg.to)
                                  if msg.to in protect["proall"]:
                                      msgs = ""
                                  else:
                                      protect["proall"].append(msg.to)
                                  if msg.to in protectcancel:
                                      ginfo = cl.getGroup(msg.to)
                                      msgs = "Semua protect on \n\ndi group : " +str(ginfo.name)
                                  else:
                                      protectcancel.append(msg.to)
                                      ginfo = cl.getGroup(msg.to)
                                      msgs = "Succes\nIn group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "Activated\n\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protect["pqr"]:
                                         protect["pqr"].remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protect["protect"]:
                                         protect["protect"].remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protect["pinv"]:
                                         protect["pinv"].remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protect["antijs"]:
                                         protect["antijs"].remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protect["proall"]:
                                         protect["proall"].remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Succes Nonactive Allpro\n\nIn group : " +str(ginfo.name)
                                    else:
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Allpro has been deactive\nDi Group : " +str(ginfo.name)
                                    cl.sendMessage(msg.to, "Nonactive\n" + msgs)

#===========KICKOUT============#       
                        elif ("Kicker " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           random.choice(ABC).kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass
                                           
                        elif ("Vc " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           G = cl.getGroup(msg.to)
                                           G.preventedJoinByTicket = False
                                           cl.updateGroup(G)
                                           invsend = 0
                                           Ticket = cl.reissueGroupTicket(msg.to)
                                           sw.acceptGroupInvitationByTicket(msg.to,Ticket)
                                           sw.kickoutFromGroup(msg.to, [target])
                                           sw.leaveGroup(msg.to)
                                           X = cl.getGroup(msg.to)
                                           X.preventedJoinByTicket = True
                                           cl.updateGroup(X)
                                       except:
                                           pass
                                           
                        elif ("Bubar" in msg.text):
                            if msg._from in admin:
                             if msg.toType == 2:
                                 print ("[ 19 ] KICK ALL MEMBER")
                                 _name = msg.text.replace("Bubar","")                                 
                                 gs = ki.getGroup(msg.to)
                                 gs = kk.getGroup(msg.to)
                                 gs = kc.getGroup(msg.to)
                                 gs = km.getGroup(msg.to)
                                 gs = kb.getGroup(msg.to)
                                 cl.sendMessage(msg.to,"「 Papay Sayang 😚😚😚」")
                                 cl.sendMessage(msg.to,"「 Sorry r̸o̸o̸m̸ n̸y̸a̸ k̸a̸m̸i̸ s̸i̸t̸a̸ s̸e̸e̸ y̸o̸u̸ s̸l̸a̸m̸ d̸a̸r̸i̸ TΣΔM SILΣΠT βΩT」")
                                 targets = []
                                 for g in gs.members:
                                     if _name in g.displayName:
                                         targets.append(g.mid)
                                 if targets == []:
                                     cl.sendMessage(msg.to,"Limit boss")
                                 else:
                                     for target in targets:
                                       if not target in Bots:
                                          if not target in admin:
                                             if not target in staff:
                                               try:
                                                   dhenza= [ki,kk,kc,km,kb]
                                                   kicker=random.choice(dhenza)
                                                   kicker.kickoutFromGroup(msg.to,[target])
                                                   print (msg.to,[g.mid])
                                               except Exception as error:
                                                   cl.sendMessage(msg.to, str(error))

                        elif text.lower() == 'silentkiller':
                           if msg._from in owner or msg._from in admin or msg._from in staff:
                           	if msg.toType == 2:
                                  ginfo = cl.getGroup(msg.to)
                                  cl.sendMessage(msg.to, "Proses Cleanse....")
                                  cl.sendMessage(msg.to, "「 silentkiller 」\nmember : " +str(len(ginfo.members)) + " \nFuck you...")
                                  G = cl.getGroup(msg.to)
                                  G.preventedJoinByTicket = False
                                  cl.updateGroup(G)
                                  Ticket = cl.reissueGroupTicket(msg.to)
                                  ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                                  kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                                  kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                                  km.acceptGroupInvitationByTicket(msg.to,Ticket)
                                  kb.acceptGroupInvitationByTicket(msg.to,Ticket)
                                  sw.acceptGroupInvitationByTicket(msg.to,Ticket)
                                  _name = text.lower().replace('silentkiller','')
                                  gs = ki.getGroup(msg.to)
                                  gs = kk.getGroup(msg.to)
                                  gs = kc.getGroup(msg.to)
                                  gs = km.getGroup(msg.to)
                                  gs = kb.getGroup(msg.to)
                                  gs = sw.getGroup(msg.to)
                                  targets = []
                                  for g in gs.members:
                                  	if _name in g.displayName:
                                  	   targets.append(g.mid)
                                  if targets == []:
                                  	cl.sendMessage(msg.to, "Nothing member")
                                  else:
                                       for target in targets:
                                        if not target in Bots:
                                           if not target in admin:
                                              if not target in staff:
                                                 try:
                                                      random.choice(ABC).kickoutFromGroup(msg.to,[target])
                                                      G = cl.getGroup(msg.to)
                                                      G.preventedJoinByTicket = True
                                                      cl.updateGroup(G)
                                                      G.preventedJoinByTicket(G)
                                                      cl.updateGroup(G)
                                                 except:
                                                      pass
                                                      
                        elif text.lower() == 'killban':
                           if msg._from in owner or msg._from in admin or msg._from in staff:
                              gid = cl.getGroupIdsJoined()
                              group = cl.getGroup(to)
                              gMembMids = [contact.mid for contact in group.members]
                              ban_list = []
                              for tag in wait["blacklist"]:
                                    ban_list += filter(lambda str: str == tag, gMembMids)
                              if ban_list == []:
                                    cl.sendMessage(to, "Limit bos")
                                    return
                              else:
                                    for i in gid:
                                    	for jj in ban_list:
                                         if jj in admin:
                                                pass
                                         elif jj in staff:
                                                pass
                                         elif jj in Bots:
                                                pass
                                         else:
                                                cl.kickoutFromGroup(i, [jj])
                                                
                        elif "Mainkan " in msg.text:
                           if msg._from in admin:
                              key = eval(msg.contentMetadata["MENTION"])
                              key["MENTIONEES"][0]["M"]                                                                                                                                
                              targets = []
                              for x in key["MENTIONEES"]:
                                  targets.append(x["M"])
                              for target in targets:                                                                                                                                       
                                  try:
                                      ki.kickoutFromGroup(msg.to,[target])
                                      ki.findAndAddContactsByMid(target)
                                      ki.inviteIntoGroup(msg.to,[target])
                                      ki.cancelGroupInvitation(msg.to,[target])
                                      ki.inviteIntoGroup(msg.to,[target])
                                      ki.cancelGroupInvitation(msg.to,[target])
                                      ki.inviteIntoGroup(msg.to,[target])
                                      ki.cancelGroupInvitation(msg.to,[target])
                                      ki.inviteIntoGroup(msg.to,[target])
                                      ki.cancelGroupInvitation(msg.to,[target])
                                      ki.inviteIntoGroup(msg.to,[target])
                                      ki.cancelGroupInvitation(msg.to,[target])
                                      ki.inviteIntoGroup(msg.to,[target])
                                      ki.cancelGroupInvitation(msg.to,[target])
                                      ki.inviteIntoGroup(msg.to,[target])
                                      ki.cancelGroupInvitation(msg.to,[target])
                                      ki.inviteIntoGroup(msg.to,[target])
                                      ki.cancelGroupInvitation(msg.to,[target])
                                      ki.inviteIntoGroup(msg.to,[target])
                                      ki.cancelGroupInvitation(msg.to,[target])
                                      ki.inviteIntoGroup(msg.to,[target])
                                      ki.cancelGroupInvitation(msg.to,[target])
                                      ki.inviteIntoGroup(msg.to,[target])
                                      ki.cancelGroupInvitation(msg.to,[target])
                                      ki.inviteIntoGroup(msg.to,[target])
                                      ki.cancelGroupInvitation(msg.to,[target])
                                  except:
                                      pass
                                      
                        elif "Invite " in msg.text:
                            if msg._from in admin:                                                                                                                                       
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]                                                                                                                                
                               targets = []
                               for x in key["MENTIONEES"]:                                                                                                                                  
                                   targets.append(x["M"])
                               for target in targets:                                                                                                                                       
                                   try:
                                      cl.findAndAddContactsByMid(target)
                                      cl.inviteIntoGroup(msg.to,[target])
                                   except:
                                       pass 
                                       
                        elif cmd == "gas":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "ASSALAMUALAIKUM \nHALLOOO!!! SORRY ROOM KALIAN \n\nKEBANYAKAN ANU\nSILENT DATANG\nMAU SAPU ROOM GJ\nNO COMEND \nNO BAPER \nNO BACOT \nNO DESAH \nNO SPONSOR \nNO HATTERS\nROOM OKEP \nROOM JUDI\nROOM GAJELAS\SIAP KAMI BANTAII \n\n\n\n FUCK YOU...\nKENAPE LU PADA DIEM\nTANGKIS SU JANGAN CUMA NYIMAK\n\n\nDASAR ROOM PEA KAGAK JELAS\nSORRY BOS!!!\nGC LU MAU GUA SITA...!!!\n\n\n SALAM DARI KAMI S̴̬̦̈͛̈́̇̈́̈́͂͒I̴̡͈͓̖͉̟̲͚̮͚̾͌̂̅̈́̍̀͗̕͝L̴̯̝̣̉͜ͅḚ̵̻͆N̷̡̛͎̗̮̤̩̟̮̏̄́̔̄̀T̵̪̭͇̘̳̚ ̸̲̪̱͒́̂̀ͅK̶̨̟̥͊͑̍̆͌̎Ḯ̸̧̺͖͔̹̞̿͗̚Ļ̶̧̨̫̤͈̖͆͆̈̕̚L̵̖̤͈̜̳̉̽͋͛̈́E̸̡̖̠̦͛͜R̵͖̬̯̞̝̪̳̙̙̋͑̒͊̎̕̚͜\n\nHADIR DI ROOM ANDA\n\nRATA GAK RATA YANG PENTING KIBAR \nRATA KAMI SENANG\nGAKRATA TUNGGU KEDATANGAN KAMI LAGI\n\n\n  <<<SLAM CIAK S̴̬̦̈͛̈́̇̈́̈́͂͒I̴̡͈͓̖͉̟̲͚̮͚̾͌̂̅̈́̍̀͗̕͝L̴̯̝̣̉͜ͅḚ̵̻͆N̷̡̛͎̗̮̤̩̟̮̏̄́̔̄̀T̵̪̭͇̘̳̚ ̸̲̪̱͒́̂̀ͅK̶̨̟̥͊͑̍̆͌̎Ḯ̸̧̺͖͔̹̞̿͗̚Ļ̶̧̨̫̤͈̖͆͆̈̕̚L̵̖̤͈̜̳̉̽͋͛̈́E̸̡̖̠̦͛͜R̵͖̬̯̞̝̪̳̙̙̋͑̒͊̎̕̚͜>>> \n\n\n>>>>>>GO!!! <<<<<<\n\n\nCREATOR\n\n<<<<<<<<<<S̴̬̦̈͛̈́̇̈́̈́͂͒I̴̡͈͓̖͉̟̲͚̮͚̾͌̂̅̈́̍̀͗̕͝L̴̯̝̣̉͜ͅḚ̵̻͆N̷̡̛͎̗̮̤̩̟̮̏̄́̔̄̀T̵̪̭͇̘̳̚ ̸̲̪̱͒́̂̀ͅK̶̨̟̥͊͑̍̆͌̎Ḯ̸̧̺͖͔̹̞̿͗̚Ļ̶̧̨̫̤͈̖͆͆̈̕̚L̵̖̤͈̜̳̉̽͋͛̈́E̸̡̖̠̦͛͜R̵͖̬̯̞̝̪̳̙̙̋͑̒͊̎̕̚͜>>>>>>>>>>\n\nhttp://line.me/ti/p/~pxj5094s\nhttp://line.me/ti/p/~dhenz415")
                               cl.sendContact(to, mid)
                               cl.sendContact(to, Amid)
                               cl.sendContact(to, Bmid)
                               cl.sendContact(to, Amid)
                               cl.sendContact(to, Bmid)
                               cl.sendContact(to, Amid)
                               cl.sendContact(to, Bmid)
                               cl.sendContact(to, Amid)
                               cl.sendContact(to, Bmid)
                               cl.sendContact(to, Amid)
                               cl.sendContact(to, Bmid)
                               cl.sendContact(to, Amid)
                               cl.sendContact(to, Bmid)
                               cl.sendContact(to, Amid)
                               cl.sendContact(to, Bmid)
                               cl.sendContact(to, Amid)
                               cl.sendContact(to, Bmid)
                               cl.sendContact(to, Amid)
                               cl.sendContact(to, Bmid)
                               cl.sendContact(to, Amid)
                               cl.sendContact(to, Bmid)
                               cl.sendContact(to, Amid)
                               cl.sendContact(to, Bmid)
                               cl.sendContact(to, Amid)
                               cl.sendContact(to, Bmid)                          
                               cl.sendMessage(to, None, contentMetadata={"STKID":"406","STKPKGID":"1","STKVER":"100"}, contentType=7)
                               cl.sendMessage(to, None, contentMetadata={"STKID":"406","STKPKGID":"1","STKVER":"100"}, contentType=7)
#===========ADMIN ADD============
                        elif ("Staff:on " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           staff.append(target)
                                           cl.sendMessage(msg.to,"Berhasil menambahkan staff")
                                       except:
                                           pass

                        elif ("Bot:on " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           Bots.append(target)
                                           cl.sendMessage(msg.to,"Succes Addbot")
                                       except:
                                           pass

                        elif ("Adminexpl:on " in msg.text):
                            if msg._from in owner or msg_from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           admin.remove(target)
                                           cl.sendMessage(msg.to,"Succes expel admin")
                                       except:
                                           pass

                        elif ("Staffexpl:on " in msg.text):
                            if msg._from in owner or msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           staff.remove(target)
                                           cl.sendMessage(msg.to,"Succes expel staff")
                                       except:
                                           pass

                        elif ("Botexpl:on " in msg.text):
                            if msg._from in owner:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           Bots.remove(target)
                                           cl.sendMessage(msg.to,"Succes expel Bots")
                                       except:
                                           pass
  #====================================#                                         
                        elif cmd == "autojoin on":
                            if msg._from in owner:
                                settings["autoJoin"] = True
                                cl.sendMessage(to, "Berhasil mengaktifkan auto join")
                        elif cmd == "autojoin off":
                            if msg._from in owner:	
                                settings["autoJoin"] = False
                                cl.sendMessage(to, "Berhasil menonaktifkan auto join")
                        elif cmd == "autoblock on":
                           if msg._from in owner:
                                settings["autoBlock"] = True
                                cl.sendMessage(to, "Berhasil mengaktifkan auto Block")
                        elif cmd == "autoblock off":    
                            if msg._from in owner: 	
                                settings["autoBlock"] = False
                                cl.sendMessage(to, "Berhasil menonaktifkan auto Block")                        
                        elif cmd == "checkpost on":
                           if msg._from in owner:
                                 settings["checkPost"] = True
                                 cl.sendMessage(to, "Berhasil mengaktifkan check details post")
                        elif cmd == "checkpost off":
                           if msg._from in owner:
                                settings["checkPost"] = False
                                cl.sendMessage(to, "Berhasil menonaktifkan check details post")                        
                        elif cmd == "unsend on":
                       	 if msg._from in owner:
                                 settings["unsendMessage"] = True
                                 cl.sendMessage(to, "Berhasil mengaktifkan unsend message")
                        elif cmd == "unsend off":
                            if msg._from in owner:
                                 settings["unsendMessage"] = False
                                 cl.sendMessage(to, "Berhasil menonaktifkan unsend message")
#==================================#
                        elif cmd == "admin:on" or text.lower() == 'admin:on':
                            if msg._from in owner:
                                wait["addadmin"] = True
                                cl.sendMessage(msg.to,"Send Contact")

                        elif cmd == "adminexpl:on" or text.lower() == 'adminexpl:on':
                            if msg._from in owner:
                                wait["delladmin"] = True
                                cl.sendMessage(msg.to,"Send contact")

                        elif cmd == "staff:on" or text.lower() == 'staff:on':
                            if msg._from in owner or msg._from in admin:
                                wait["addstaff"] = True
                                cl.sendMessage(msg.to,"Send contact")

                        elif cmd == "staffexpl:on" or text.lower() == 'staffexpl:on':
                            if msg._from in owner or msg._from in admin:
                                wait["dellstaff"] = True
                                cl.sendMessage(msg.to,"Send contact")

                        elif cmd == "bot:on" or text.lower() == 'bot:on':
                            if msg._from in owner or msg._from in admin:
                                wait["addbots"] = True
                                cl.sendMessage(msg.to,"Send contact")

                        elif cmd == "botexpl:on" or text.lower() == 'botexpl:on':
                            if msg._from in owner:
                                wait["dellbots"] = True
                                cl.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "fresh" or text.lower() == 'refresh':
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                wait["addadmin"] = False
                                wait["delladmin"] = False
                                wait["addstaff"] = False
                                wait["dellstaff"] = False
                                wait["addbots"] = False
                                wait["dellbots"] = False
                                wait["wblacklist"] = False
                                wait["dblacklist"] = False
                                wait["Talkwblacklist"] = False
                                wait["Talkdblacklist"] = False
                                cl.sendMessage(msg.to,"Clean..")
                                cl.sendMessage(msg.to,"Refresh done 💯")

                        elif cmd == "admin" or text.lower() == 'contact admin':
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                ma = ""
                                for i in admin:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "staff" or text.lower() == 'contact staff':
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                ma = ""
                                for i in staff:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)
                     
                        elif cmd == "spaminvite on" or text.lower == 'spaminvite on':
                            if msg._from in admin:
                                settings["SpamInvite"] = True
                                cl.sendMessage(msg.to, "Send Contact to spam grup..")
                                
                        elif cmd == "spaminvite off" or text.lower() == 'spaminvite off':
                            if msg._from in admin:
                                settings["Spaminvite"] = False
                                cl.sendMessage(msg.to, "Send Contact to send grup Off..")
                                
#===========COMMAND ON OFF============#
                        elif cmd == "notag on" or text.lower() == 'notag on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["Mentionkick"] = True
                                cl.sendMessage(msg.to,"Notag diaktifkan")

                        elif cmd == "notag off" or text.lower() == 'notag off':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["MentionKick"] = False
                                cl.sendMessage(msg.to,"Notag dinonaktifkan")

                        elif cmd == "contact on" or text.lower() == 'contact on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["contact"] = True
                                cl.sendMessage(msg.to,"Deteksi contact diaktifkan")

                        elif cmd == "contact off" or text.lower() == 'contact off':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["contact"] = False
                                cl.sendMessage(msg.to,"Deteksi contact dinonaktifkan")

                        elif cmd == "respon on" or text.lower() == 'respon on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["detectMention"] = True
                                cl.sendMessage(msg.to,"Auto respon diaktifkan")

                        elif cmd == "respon off" or text.lower() == 'respon off':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["detectMention"] = False
                                cl.sendMessage(msg.to,"Auto respon dinonaktifkan")

                        elif cmd == "autojoin on" or text.lower() == 'autojoin on':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                wait["autoJoin"] = True
                                cl.sendMessage(msg.to,"Autojoin diaktifkan")

                        elif cmd == "autojoin off" or text.lower() == 'autojoin off':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                wait["autoJoin"] = False
                                cl.sendMessage(msg.to,"Autojoin dinonaktifkan")

                        elif cmd == "autoleave on" or text.lower() == 'autoleave on':
                          if wait["selfbot"] == True:
                            if msg._from in admin or msg._from in owner:
                                wait["autoLeave"] = True
                                cl.sendMessage(msg.to,"Autoleave diaktifkan")

                        elif cmd == "autoleave off" or text.lower() == 'autoleave off':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                wait["autoLeave"] = False
                                cl.sendMessage(msg.to,"Autoleave dinonaktifkan")

                        elif cmd == "autoadd on" or text.lower() == 'autoadd on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["autoAdd"] = True
                                cl.sendMessage(msg.to,"Auto add diaktifkan")

                        elif cmd == "autoadd off" or text.lower() == 'autoadd off':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["autoAdd"] = False
                                cl.sendMessage(msg.to,"Auto add dinonaktifkan")

                        elif cmd == "sticker on" or text.lower() == 'sticker on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["sticker"] = True
                                cl.sendMessage(msg.to,"Deteksi sticker diaktifkan")

                        elif cmd == "sticker off" or text.lower() == 'sticker off':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["sticker"] = False
                                cl.sendMessage(msg.to,"Deteksi sticker dinonaktifkan")

                        elif cmd == "jointicket on" or text.lower() == 'jointicket on':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                settings["autoJoinTicket"] = True
                                cl.sendMessage(msg.to,"Join ticket diaktifkan")

                        elif cmd == "jointicket off" or text.lower() == 'jointicket off':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                settings["autoJoinTicket"] = False
                                cl.sendMessage(msg.to,"Notag dinonaktifkan")

#===========COMMAND BLACKLIST============#
                        elif cmd == "ban all":
                            if msg.toType == 2:
                                gs = cl.getGroup(msg.to)
                                targets = []
                                for g in gs.members:
                                    targets.append(g.mid)
                                targets.remove(mid)
                                if targets == []:
                                    cl.sendMessage(msg.to,"gak ada orang")
                                else:
                                    for target in targets:
                                         if target not in wait["selfbot"] or target not in Bots:
                                            try:
                                                wait["blacklist"][target] = True
                                                cl.sendMessage(msg.to,"Anda ternoda")
                                            except:
                                                pass
                                                
                        elif cmd == "unban all":
                            if msg.toType == 2:
                                gs = cl.getGroup(msg.to)
                                targets = []
                                for g in gs.members:
                                    targets.append(g.mid)
                                targets.remove(mid)
                                if targets == []:
                                    cl.sendMessage(msg.to,"gak ada orang")
                                else:
                                    for target in targets:
                                            try:
                                                del wait["blacklist"][target]
                                                cl.sendMessage(msg.to,"Anda ternoda")
                                            except:
                                                pass
                        elif ("Talkban:on " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           wait["Talkblacklist"][target] = True
                                           cl.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                                       except:
                                           pass

                        elif ("Untalkban:on " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["Talkblacklist"][target]
                                           cl.sendMessage(msg.to,"Berhasil menghapus blacklist")
                                       except:
                                           pass

                        elif cmd == "talkban:on" or text.lower() == 'talkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["Talkwblacklist"] = True
                                cl.sendMessage(msg.to,"Send contact")

                        elif cmd == "untalkban:on" or text.lower() == 'untalkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["Talkdblacklist"] = True
                                cl.sendMessage(msg.to,"Send contact")

                        elif ("Ban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           wait["blacklist"][target] = True
                                           cl.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                                       except:
                                           pass

                        elif ("Unban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["blacklist"][target]
                                           cl.sendMessage(msg.to,"Berhasil menghapus blacklist")
                                       except:
                                           pass

                        elif cmd == "ban:on" or text.lower() == 'ban:on':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                wait["wblacklist"] = True
                                cl.sendMessage(msg.to,"Send contact")

                        elif cmd == "unban:on" or text.lower() == 'unban:on':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                wait["dblacklist"] = True
                                cl.sendMessage(msg.to,"Send contact")

                        elif cmd == "banlist" or text.lower() == 'banlist':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                              if wait["blacklist"] == {}:
                                cl.sendMessage(msg.to,"Nothing blacklist")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["blacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"Blacklist\n\n"+ma+"\n %s User" %(str(len(wait["blacklist"]))))

                        elif cmd == "talkbanlist" or text.lower() == 'talkbanlist':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                              if wait["Talkblacklist"] == {}:
                                cl.sendMessage(msg.to,"Tidak ada Talkban user")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["Talkblacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to," Talkban User\n\n"+ma+"\nTotal「%s」Talkban User" %(str(len(wait["Talkblacklist"]))))

                        elif cmd == "bl" or text.lower() == 'bl':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                              if wait["blacklist"] == {}:
                                    cl.sendMessage(msg.to,"Tidak ada blacklist")
                              else:
                                    ma = ""
                                    for i in wait["blacklist"]:
                                        ma = cl.getContact(i)
                                        cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "clearban" or text.lower() == 'clearban':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                              wait["blacklist"] = {}
                              ragets = cl.getContacts(wait["blacklist"])
                              mc = "%i" % len(ragets)
                              cl.sendMessage(msg.to,"Succes clearall " +mc)
                        elif text.lower() == 'dz':
                               cl.sendMessage(msg.to, "cie pake sc nya dhenza ya")
#===========COMMAND SET============#
                        elif 'Spesan: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Spesan: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Pesan Msg")
                              else:
                                  wait["message"] = spl
                                  cl.sendMessage(msg.to, "「Pesan Msg」\nPesan Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Swelcome: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Swelcome: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Welcome Msg")
                              else:
                                  wait["welcome"] = spl
                                  cl.sendMessage(msg.to, "「Welcome Msg」\nWelcome Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Srespon: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Srespon: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Respon Msg")
                              else:
                                  wait["Respontag"] = spl
                                  cl.sendMessage(msg.to, "「Respon Msg」\nRespon Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Sspam: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Sspam: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Spam")
                              else:
                                  Setmain["RAmessage1"] = spl
                                  cl.sendMessage(msg.to, "「Spam Msg」\nSpam Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Ssider: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Ssider: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Sider Msg")
                              else:
                                  wait["mention"] = spl
                                  cl.sendMessage(msg.to, "「Sider Msg」\nSider Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif text.lower() == "cpesan":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「Pesan Msg」\nPesan Msg mu :\n\n「 " + str(wait["message"]) + " 」")

                        elif text.lower() == "cwelcome":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「Welcome Msg」\nWelcome Msg mu :\n\n「 " + str(wait["welcome"]) + " 」")

                        elif text.lower() == "crespon":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「Respon Msg」\nRespon Msg mu :\n\n「 " + str(wait["Respontag"]) + " 」")

                        elif text.lower() == "cspam":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「Spam Msg」\nSpam Msg mu :\n\n「 " + str(Setmain["RAmessage1"]) + " 」")

                        elif text.lower() == "csider":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「Sider Msg」\nSider Msg mu :\n\n「 " + str(wait["mention"]) + " 」")
                               
                        elif cmd == "batre":
                            if msg._from in admin or msg._from in owner:
                               try:cl.inviteIntoGroup(to, ["u45882d0ead1703855dbc60d40e37bec7"]);has = "OK"
                               except:has = "NOT"
                               try:cl.kickoutFromGroup(to, ["u45882d0ead1703855dbc60d40e37bec7"]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔋██ full 100%"
                               else:sil = "🔌█▒. Low 0%"
                               if has1 == "OK":sil1 = "🔋██ full 100%"
                               else:sil1 = "🔌█▒ Low 0%"
                               cl.sendMessage(to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))
                               try:ki.inviteIntoGroup(to, ["u2bf37dc8bb9ac850615395a9e15850f9"]);has = "OK"
                               except:has = "NOT"
                               try:ki.kickoutFromGroup(to, ["u2bf37dc8bb9ac850615395a9e15850f9"]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔋██ full 100%"
                               else:sil = "🔌█▒ Low 0%"
                               if has1 == "OK":sil1 = "🔋██ full 100%"
                               else:sil1 = "🔌█▒ Low 0%"
                               ki.sendMessage(to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))                               
                               try:kk.inviteIntoGroup(to, ["u0a5ee8d796e3677a56b84ff03b6564ec"]);has = "OK"
                               except:has = "NOT"
                               try:kk.kickoutFromGroup(to, ["u0a5ee8d796e3677a56b84ff03b6564ec"]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔋██ full 100%"
                               else:sil = "🔌█▒. Low 0%"
                               if has1 == "OK":sil1 = "🔋██ full 100%"
                               else:sil1 = "🔌█▒ Low 0%"
                               kk.sendMessage(to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))
                               try:kc.inviteIntoGroup(to, ["u29b16f0e99cfdf0e7d7b8170f7cdc1a7"]);has = "OK"
                               except:has = "NOT"
                               try:kc.kickoutFromGroup(to, ["u29b16f0e99cfdf0e7d7b8170f7cdc1a7"]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔋██ full 100%"
                               else:sil = "🔌█▒. Low 0%"
                               if has1 == "OK":sil1 = "🔋██ full 100%"
                               else:sil1 = "🔌█▒ Low  0%"
                               kc.sendMessage(to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))                               
                               try:kc.inviteIntoGroup(to, ["udfad8056476f3e76903575513cc8aebe"]);has = "OK"
                               except:has = "NOT"
                               try:km.kickoutFromGroup(to, ["udfad8056476f3e76903575513cc8aebe"]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔋██ full 100%"
                               else:sil = "🔌█▒ Low 0%"
                               if has1 == "OK":sil1 = "🔋██ full 100%"
                               else:sil1 = "🔌█▒ Low 0%"
                               km.sendMessage(to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))                              
                               try:kb.inviteIntoGroup(to, ["uea5fe04e39713e6768cf5687bc5ac7aa"]);has = "OK"
                               except:has = "NOT"
                               try:kb.kickoutFromGroup(to, ["uea5fe04e39713e6768cf5687bc5ac7aa"]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔋██ full 100%"
                               else:sil = "🔌█▒ Low 0%"
                               if has1 == "OK":sil1 = "🔋██ full 100%"
                               else:sil1 = "🔌█▒ Low 0%"
                               kb.sendMessage(to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))
                                                                                    
#===========JOIN TICKET============#
                        elif "/ti/g/" in msg.text.lower():
                          if wait["selfbot"] == True:
                            if msg._from in admin or msg._from in owner:
                              if settings["autoJoinTicket"] == True:
                                 link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                 links = link_re.findall(text)
                                 n_links = []
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = cl.findGroupByTicket(ticket_id)
                                     cl.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     cl.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group1 = ka.findGroupByTicket(ticket_id)
                                     
    except Exception as error:
        print (error)


while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                bot(op)
                # Don't remove this line, if you wan't get error soon!
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)