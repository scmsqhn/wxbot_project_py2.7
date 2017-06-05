#!/usr/bin/env python
# coding: utf-8

#===================================================
from wechat.utils import *
from wxconfig import Constant
#---------------------------------------------------
import random, time, json
#===================================================
from aip.nlp import AipNlp

class Bot(object):

    def __init__(self):
        self.emoticons = Constant.EMOTICON
        self.gifs = []
        self.last_time = time.time()
        self.myAipNlp= AipNlp(Constant.AIP_APPID, Constant.AIP_API_KEY, Constant.AIP_APP_SECRET)
    
    def time_schedule(self):
        print '[*] 判断时间是否触发'
        r = ''
        now = time.time()
        if int(now - self.last_time) > 60*60*8:
            self.last_time = now
            url_latest = Constant.BOT_ZHIHU_URL_LATEST
            url_daily = Constant.BOT_ZHIHU_URL_DAILY
            data = get(url_latest)
            j = json.loads(data)
            story = j['stories'][random.randint(0, len(j['stories'])-1)]
            r = story['title'] + '\n' + url_daily + str(story['id'])
        print '[*] 返回推送链�? ', r.encode('utf-8')
        return r.encode('utf-8')
        
        if time.localtime(time.time())[3]==7 and time.localtime(time.time())[4]==30:
            r=r'早上好,新的一天顺利'
            return r
            
        if time.localtime(time.time())[3]==23 and time.localtime(time.time())[4]==30:
            r='今天辛苦了,晚安'
            return r

    def reply(self, text):
        APIKEY = Constant.BOT_TULING_API_KEY
        api_url = Constant.BOT_TULING_API_URL % (APIKEY, text, '12345678')
        r = json.loads(get(api_url))
        if r.get('code') == 100000 and r.get('text') != Constant.BOT_TULING_BOT_REPLY:
            p = random.randint(1, 10)
            if p > 3:
                return r['text']
            elif p > 1:
                # send emoji
                if random.randint(1, 10) > 5:
                    n = random.randint(0, len(self.emoticons)-1)
                    m = random.randint(1, 3)
                    reply = self.emoticons[n].encode('utf-8') * m
                    return reply
        return ''
        
    def ananTextHandler(self, word):
      r= self.AipNlp.commentTag(word)
      print r
      return r
        
