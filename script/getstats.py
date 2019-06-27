# coding: utf8

# toutes les chaines sont en unicode (même les docstrings)
from __future__ import unicode_literals

from pprint import pprint
from rocketchat_API.rocketchat import RocketChat
import json
import dev_config as cfg
import os
import random
from datetime import datetime
from monthdelta import monthdelta
from common.channelhelper import getTsunamy
from common.channelhelper import Tsunami

def getColor():
    r = random.randrange(255)
    g = random.randrange(255)
    b = random.randrange(255)
    return 'rgb({:0},{:0},{:0})'.format(r,g,b)

rocket = RocketChat(cfg.rocket['user'], cfg.rocket['password'],
                    server_url='https://coa.crapaud-fou.org')
index = 0
labels = [None] * 12
messagesByChannel = []
messagesByTsunamy = []
usersByChannel = []
messagesDataTsunamy = {
  "global": [0] * 12,
  "project": [0] * 12,
  "democraty": [0] * 12,
  "ecology": [0] * 12,
  "technology": [0] * 12,
}
usersGlobal = []

now = datetime.now()
date = datetime(now.year, now.month, now.day, 0,0,0)

info = {
  "updated": "updated {:02}/{:02}/{:04}".format(now.day, now.month, now.year),
  "labels": labels,
  "messagesByChannel": messagesByChannel,
  "usersByChannel": usersByChannel,
  "messagesByTsunamy": [{        
        "label": "global",
        "backgroundColor": getColor(),
        "data": messagesDataTsunamy['global']
    },
    {        
        "label": "projet",
        "backgroundColor": getColor(),
        "data": messagesDataTsunamy['project']
    },
    {        
        "label": "democratie",
        "backgroundColor": getColor(),
        "data": messagesDataTsunamy['democraty']
    },
    {        
        "label": "ecologie",
        "backgroundColor": getColor(),
        "data": messagesDataTsunamy['ecology']
    },
    {        
        "label": "technologie",
        "backgroundColor": getColor(),
        "data": messagesDataTsunamy['technology']
    }],
    "usersGlobal": usersGlobal
}

usersTest = [None] * 12

while True:
  channels = rocket.channels_list(offset=index).json()
  totalChannels = channels['total']
    
  for channel in channels['channels']:
    dataMess = []
    dataUsers = []
    pprint( channel['name'] )
    begin = date - monthdelta(12)
    end = begin + monthdelta(1)

    tsunamy = getTsunamy(channel)    

    for id in range(0, 12):
      if usersTest[id] == None:
        usersTest[id] = []
      labels[id] = begin.strftime("%b %Y")
      begindate =  begin.isoformat()
      enddate = end.isoformat()
      resultMess = rocket.channels_history(channel['_id'], oldest= begindate, latest=enddate, count= 10000).json()
      resultMess = list(filter(lambda mess: 't' not in mess, resultMess['messages']))
      lenght = len(resultMess)
      dataMess.append(lenght)

      if lenght > 0:
        if tsunamy & Tsunami.GLOBAL:
          messagesDataTsunamy['global'][id] += lenght
        if tsunamy & Tsunami.PROJECT:
          messagesDataTsunamy['project'][id] += lenght
        if tsunamy & Tsunami.DEMOCRACY:
          messagesDataTsunamy['democraty'][id] += lenght
        if tsunamy & Tsunami.ECOLOGY:
          messagesDataTsunamy['ecology'][id] += lenght
        if tsunamy & Tsunami.TECHNOLOGY:
          messagesDataTsunamy['technology'][id] += lenght

        users = []
        for mess in resultMess:
          users.append(mess['u']['_id'])
          usersTest[id].append(mess['u']['_id'])
        usersDistinct = set(users)
        dataUsers.append(len(usersDistinct))
      else:
        dataUsers.append(0)

      begin = end
      end = begin + monthdelta(1)
   
    color = getColor()
    messageByChannel = {
        "label": channel['name'],
        "backgroundColor": color,
        "data": dataMess
    }

    userByChannel = {
        "label": channel['name'],
        "backgroundColor": color,
        "data": dataUsers
    }

    messagesByChannel.append(messageByChannel)
    usersByChannel.append(userByChannel)

  if channels['count'] + channels['offset'] >= channels['total']:
    break
  index += channels['count']

for id in range(0, 12):
  usersTest[id] = len(set(usersTest[id]))

userGlobal = {
    "label": 'global',
    "backgroundColor": 'red',
    "data": usersTest
}
usersGlobal.append(userGlobal)

# Récupération du répertoire racine du repo
rootFolder = os.path.join(os.path.dirname(__file__), '..')
# Répertoire pour stocker le fichier de sortie
dataFolder = os.path.join(rootFolder, 'public', 'data')

statsFilePath = os.path.abspath(
    os.path.join(dataFolder, 'channelsstat.json'))
with open(statsFilePath, "w") as file_write:
  json.dump(info, file_write)

