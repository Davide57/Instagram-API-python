#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password

from InstagramAPI.InstagramAPI import InstagramAPI
import time
import os
import random
import datetime
import json

with open('quotes.json') as f:
    json_data = json.load(f)


time.sleep(5)
usernames = ["1","2"]
InstagramAPI = InstagramAPI("1", "2")
InstagramAPI.login()  # login

base_path = 'images/'
with open("counter.txt", "r+") as f:
     i = int(f.read())
current_hour = time.strftime("%H")
if int(current_hour) > 21 or int(current_hour) < 9:
    base_time=60*10  
else:
    base_time=60*30 

print("Starting ...")
while True:
    
    print("Publishing image " + str(i) + "...")
    if(i%40==0): # Spam post
        final_path = base_path + "spam1.jpg"
        caption = "3"
    else:
        final_path = base_path + str(i) + ".jpg"
        index = random.randint(0,len(json_data["quotes"]))
        caption = "\""+json_data["quotes"][index]["quote"]+"\" ("+json_data["quotes"][index]["author"]+")\n\n4"
   
    try:
        InstagramAPI.uploadPhoto(final_path, caption=caption)
    except Exception as e:
        print('Except on calling sendRequest ' + str(e))
        time.sleep(10)
    i=i+1
    if(i>676):
       print('All the images have been published, restart from 0')
       i=1
    

    with open("counter.txt", "r+") as f:
     f.seek(0) 
     f.write(str(i)) 
    
    final_time = base_time + random.randint(1,15)
    print("Image published at "+str(datetime.datetime.now().time())+", waiting for " + str(final_time) + " seconds...")
    
    time.sleep(final_time) #waiting for 30 minutes
    print("Restarting ...")
    



