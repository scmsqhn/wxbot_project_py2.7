#!/usr/bin/env python
# -*- coding:utf-8 -*- 

#===================================================
#---------------------------------------------------
import os
import cookielib
import random
import requests
import time
import xml.dom.minidom
# for media upload
import mimetypes
import aip
import urllib2
import urllib
import json
import chardet
import demjson
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class test(object):

    def __init__(self):
      print '__init__'
      pass

    def ananTextHandler(self, content):
      '''''http://www.cnblogs.com/111testing/p/6079565.html发布json POST请求
      '''
      url = 'https://aip.baidubce.com/rpc/2.0/nlp/v2/comment_tag?access_token=24.d648b7a82d965179ff55a84a5ca10ce2.2592000.1499176480.282335-9723636'
      
      if not isinstance(content, unicode):
        print chardet.detect(content)
        print content
        style = chardet.detect(content)
        content = content.decode(style['encoding'])
      body_value_str = {
          "text": content,
          "type": 13
      }
#      print chardet.detect(body_value_str['text'])
      body_value_str = (json.dumps(body_value_str, encoding='gbk', ensure_ascii=False)).encode('gbk')
      print chardet.detect(body_value_str)
      request = urllib2.Request(url, body_value_str)
      request.add_header("Content-Type", "application/json")
      r = urllib2.urlopen(request).read().decode('gbk')
      r = json.loads(r)
      print '\n# r=', r
      count = len(r['items'])
      print count
      rlist = []
      rstr = ""
      for i in range(0,count):
        rdict = {}
        #print i
        rdict['abstract'] = self.pickSpan(r['items'][i]['abstract'])
        rdict['adj'] = self.pickSpan(r['items'][i]['adj'])
        rdict['sentiment'] = r['items'][i]['sentiment']
        rlist.append(rdict)
        rstr = rdict['abstract'], rdict['adj']
      return rstr

    def pickSpan(self, string):
      import re
      string= re.search(r'<span>(.*?)</span>', string, flags=0)
      if string:
        string = string.group(0) 
        r = re.sub(r'<span>', ' ', string)  
        r = re.sub(r'</span>', ' ', r)  
        return r
      return ''

mytest = test()

ins = '@14f632097f0fa31daa6fe721c5a1dce00d2bc57a498ef40ae411382c12e80d27:<br/>长虹手机电池耐用,待机时间长'
ins1 = ins
ins = ins1
print chardet.detect(ins)
mytest.ananTextHandler(ins)