# -*- coding: utf-8 -*-

'''
this file is handle the request action
make the proxyip, header, cookie, to avoid be banned
get ip should first start the ProxyIP 
from haining.qin, 17-05-03
'''

import json
import urllib2
import sys
import time,socket,random
import re,collections
import decimal
import sys
import codecs
import json
import time
import random
import subprocess
import codecs
import os
#import httplib.cookie
import cookielib

sys.path.append(os.getcwd()+'/../../iproxys/IPPROXYS')
print(os.getcwd()+'/../../iproxys/IPPROXYS')

hds=[{'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},\
    {'User-Agent':'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'},\
    {'User-Agent':'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'},\
    {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0'},\
    {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/44.0.2403.89 Chrome/44.0.2403.89 Safari/537.36'},\
    {'User-Agent':'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},\
    {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},\
    {'User-Agent':'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0'},\
    {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},\
    {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},\
    {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'},\
    {'User-Agent':'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11'},\
    {'User-Agent':'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11'}]

def saveHtml(file_name,file_content):
    with open (file_name,"wb") as f:
        f.write(file_content)

def getip():
        f=open('./ipaddr.txt','r')
        ct=random.randint(1,20)
        for line in f.readlines():
            ct=ct-1
            if(ct<1):
                print(line)
                return line

def makeMyOpener():
#    cj = http.cookiejar.CookieJar()
    cj = cookielib.CookieJar()
    proxy = urllib2.ProxyHandler({'http': getIp()})  # 设置proxy
    print(proxy)
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj),proxy)
    myheader = hds[random.randint(0,len(hds)-1)]
    print(myheader)
    opener.addheader=myheader
    return opener

#open new urls with new opener which change the header and proxy
def openurls(url):
  print(url)
  opener = makeMyOpener()
  response=opener.open(url, timeout=20)
  data=response.read()
  return data

def handle_data_from_response(data):
# print(soup)
  print('== HANDLE THE DATA')
  if False:
      save2file_linux(data)
  if True:
      print('== PIC THE DATA')
      picTheData(data)
      time.sleep(3)

  if False:
      print('== PIC THE DATA XPATH')
      picdata_xpath(data)

def save2file_linux(data):
    f = codecs.open('./%s.html'%(re.sub(r"[^A-Za-z0-9]", "", url)), 'w', chardet.detect(data)['encoding'])
    f.write("")
#    f.close()
    f = codecs.open('./%s.html'%(re.sub(r"[^A-Za-z0-9]", "", url)), 'a+', chardet.detect(data)['encoding'])
    f.write(data)
    f.flush()
    f.close()

def picdata_xpath(html):
          selector = etree.HTML(html)
  #while True:
          print('== GET ALL CONTENT')
          count=1
#      while True:
#          print('== ENTER INTO THE WHILE')
          links = selector.xpath('//*[@id="J_Reviews"]/div')
          count=count+1
          for link in links:
              print((links.xpath('string(.)').strip()))
              time.sleep(10)
#          for link in links:
#              print(link)
#              pass
#     links = selector.xpath('//*[@id="J_Reviews"]/div/div[7]/div/a[5]').click()



def picTheData(data):
    soup = BeautifulSoup(data, 'lxml')
    print('== CONVERT 2 SOUP')
    time.sleep(3)
    print((type(soup)))
    print('== GET THE TAOBAO DATA')
    print(soup)
    alist = soup.findAll('h4',attrs=({'class':'hd'}))
    for a in alist:
        print(a)
        if('累计评价' in str(a)):
            print('== READY to CLICK')
            (a.click())
            print('== CLICK TO SHOW CUSTOMS SAYS')
            data=openurls(opener,baseurl)
            print('== REFRESH THE DATA')
            handle_data_from_response(data)

def getIp():
    # getIP from server web.py json style
    opener = urllib2.build_opener()
    print('getIP')
    response=opener.open("http://127.0.0.1:18000", timeout=20)
    dicts=(json.loads(response.read().decode()))
    i=random.randint(0,len(dicts))
    ip=str(dicts[i][0])+':'+str(dicts[i][1])
    print(ip)
    return ip
    
def request(url):
  opener=makeMyOpener()
  data=openurls(opener,url)
  return data

if __name__=="__main__":
  print('__main__')
