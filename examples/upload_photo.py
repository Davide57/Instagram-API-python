#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password

from InstagramAPI import InstagramAPI
import time
import os
import datetime

time.sleep(5)

InstagramAPI = InstagramAPI("login", "password")
InstagramAPI.login()  # login

base_path = 'images/'
i=3
t=1800 #set the waiting time
print("Starting ...")
while True:
    
    print("Publishing image " + str(i) + "...")
    final_path = base_path + str(i) + ".jpg"
    caption = "#travel #traveling #travelblogger #world #worldwatching #follow4follow #hotel #hotels #voyage #relax #relaxtime #pool #poolparty #room #luxury"
    InstagramAPI.uploadPhoto(final_path, caption=caption)
    i=i+1
    print("Image published at "+str(datetime.datetime.now().time())+", waiting for " + str(t) + " seconds...")
    time.sleep(t) #waiting for 30 minutes
    print("Restarting ...")
    
