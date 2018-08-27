#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password

from InstagramAPI.InstagramAPI import InstagramAPI
import time
import os
import random
import datetime

time.sleep(5)
usernames = ["1","2"]
InstagramAPI = InstagramAPI("p1", "p2")
InstagramAPI.login()  # login

base_path = 'images/'
with open("counter.txt", "r+") as f:
     i = int(f.read())

base_time=60*10  #set the waiting time
print("Starting ...")
while True:
    
    print("Publishing image " + str(i) + "...")
    final_path = base_path + str(i) + ".jpg"
    caption = "Follow #worldtelescope, #world, #worldtravel, #travel, #love, #food, #animals, #instagood, #photooftheday, #beautiful, #happy, #cute, #like4like, #followme, #picoftheday, #follow, #me, #summer, #instadaily, #nature, #fun, #follow4follow, #tagsforlikes, #nofilter, #amazing, #photography, #photo, #bestoftheday, #f4f, #cool"
    try:
        InstagramAPI.uploadPhoto(final_path, caption=caption)
    except Exception as e:
        print('Except on calling sendRequest ' + str(e))
        time.sleep(10)
    i=i+1

    with open("counter.txt", "r+") as f:
     f.seek(0) 
     f.write(str(i)) 
    
    final_time = base_time + random.randint(1,15)
    print("Image published at "+str(datetime.datetime.now().time())+", waiting for " + str(final_time) + " seconds...")
    
    time.sleep(final_time) #waiting for 30 minutes
    print("Restarting ...")
    
