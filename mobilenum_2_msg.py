# coding=UTF-8

# get all the kind of phone num which is divided as 3-4-4
# check with 3-4 to get the phone's msg from net
# with this we can serve the customer better
# 17-05-02 haining.qin changhong

# ENVIRONMENT: python2

# get provider information by phoneNumber

from urllib import urlopen
import socket
import re
from db.MongoHelper import MongoHelper
from db.RedisHelper import RedisHelper
from db.ISqlHelper import ISqlHelper
import db.config
import random
import time
import request
import urllib2

#from wxbot_project_py2\.7 import MongoHelper
#130
HEAD_BASE_PHONE = [132,155,156,186,185,186,185,145,134,135,136,137,138,139,150,151,152,157,158,159,182,183,188,187,133,153,180,181,189]

def get4random():
    i=random.randint(0,9999)
    return i

def obtainPhoneNum(head,middle):
    strPhone=str(head)+"%04d"%middle+"%04d"%get4random()
    return strPhone

# get html source code for url
def getPageCode(url):
    print(url)
    text = request.openurls(url)
#    text = text.decode("utf-8")     # depending on coding of source code responded
    print(text)
    return text

# parse html source code to get provider information
def parseString(src):
    print(src)
    pat = []
    pat.append('(?<=归属地：</span>).+(?=<br />)')
    pat.append('(?<=卡类型：</span>).+(?=<br />)')
    pat.append('(?<=运营商：</span>).+(?=<br />)')
    pat.append('(?<=区号：</span>)\d+(?=<br />)')
    pat.append('(?<=邮编：</span>)\d+(?=<br />)')
    item = []
    for i in range(len(pat)):
        m = re.search(pat[i], src)
        if m:
            v = m.group(0)
            item.append(v)
    print(item)
    return item

# get provider by phoneNum
def getProvider(phoneNum):
    url = "http://www.sjgsd.com/n/?q=%s" %phoneNum
    print(url)
    text = getPageCode(url)
    item = parseString(text)
#    result.append((phoneNum, item))
    print(item)
    return item

# write result to file
def writeResult(result):
    print(result)
    f = open("result.log", "w")
    for num, item in result:
        f.write("%s:\t" %num)
        for i in item:
            f.write("%s,\t" %i)
        f.write("\n")
    f.close()

def washData(phonenum,result):
    for i in result:
        i=i.strip(' ')
    final_result=[6]
    final_result[0]=phonenum
    final_result[1:]=result
    return_dict = [{'Num':final_result[0]},{'ProvAndCity':final_result[1]},\
                   {'net':final_result[2]},{'CityNum':final_result[4]},\
                   {'MailNum':final_result[5]},]
    print(return_dict)
    return return_dict

def saveTotalPhoneNum2RedisDB():
    import redis
    myredis=redis.Redis(db=0,host='127.0.0.1', port=6379)
    pipe = myredis.pipeline()
    for i in range(0,len(HEAD_BASE_PHONE)):
      for j in range(0000,9999):
        phoneNum=obtainPhoneNum(HEAD_BASE_PHONE[i],j)
        myredis.lpush("phoneNum",phoneNum)
    pipe.execute()

    pipe = myredis.pipeline()
    myredis.lpush("phoneNum",phoneNum)
    pipe.execute()

if __name__ == "__main__":
    import redis
    myredis=redis.Redis(db=0,host='127.0.0.1', port=6379)
    mongo=MongoHelper()
    mongo.init_db()
    while(True):
        phoneNum=myredis.rpop('phoneNum')
        print(phoneNum)
        try:
          result=getProvider(phoneNum)
          print(result)
        except IndexError,e:
          print(IndexError,e)
          pipe = myredis.pipeline()
          myredis.lpush("phoneNum",phoneNum)
          pipe.execute()
          continue
        except urllib2.URLError,e:
          print(urllib2.URLError,e)
          continue
        except socket.timeout,e:
          print(IndexError,e)
          continue
        except :
          print("connection close by peer")
          continue
        print("%s is finished" %phoneNum)
        try:
            mongo.insert(washData(phoneNum,result))
            time.sleep(3)
        except IndexError,e:
            print(IndexError)
            print(e)
    #writeResult(result)

