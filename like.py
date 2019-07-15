#! /usr/bin/env python
# -*- coding: utf-8 -*-

import vk_api, requests, random, json, datetime, re, time, vk

access_token = "e39283131afbdb0b2c2882beeec72616616444db0fb431d3a203e97c6bafb5c4d4acb87848d2c78097f00"
session = vk.Session(access_token=access_token)
vkapi = vk.API(session)

import urllib2
opener = vkapi.urllib2.build_opener()
fp = urllib2.urlopen("https://vk.com/al_feed.php?section=source&source=67957835&al_id=509580022&preload=1&more=0&offset=1")
mybytes = fp.read()

mystr = mybytes.decode("utf8")
open('/home/areafishing/Рабочий стол/fff.txt', 'w').close()
fp.close()
f = open('/home/areafishing/Рабочий стол/fff.txt', 'w')
mystr=mystr.encode('utf-8')
f.write(mystr)
f.close()