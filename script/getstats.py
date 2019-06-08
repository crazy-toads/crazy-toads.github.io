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
usersByChannel = []

now = datetime.now()
date = datetime(now.year, now.month, now.day, 0,0,0)

while True:
  channels = rocket.channels_list(offset=index).json()
  totalChannels = channels['total']
  
  for channel in channels['channels']:
    dataMess = []
    dataUsers = []
    pprint( channel['name'] )
    begin = date - monthdelta(12)
    end = begin + monthdelta(1)
    
    for id in range(0, 12):
      labels[id] = begin.strftime("%b %Y")
      begindate =  begin.isoformat()
      enddate = end.isoformat()
      resultMess = rocket.channels_history(channel['_id'], oldest= begindate, latest=enddate, count= 10000).json()
      lenght = len(resultMess['messages'])
      dataMess.append(lenght)

      if lenght > 0:
        users = []
        for mess in resultMess['messages']:
          users.append(mess['u']['_id'])      
        usersDistinct = set(users)
        dataUsers.append(len(usersDistinct))
      else:
        dataUsers.append(0)

      begin = end
      end = begin + monthdelta(1)
   
    messageByChannel = {
        "label": channel['name'],
        "backgroundColor": getColor(),
        "data": dataMess
    }

    userByChannel = {
        "label": channel['name'],
        "backgroundColor": getColor(),
        "data": dataUsers
    }

    messagesByChannel.append(messageByChannel)
    usersByChannel.append(userByChannel)

  if channels['count'] + channels['offset'] >= channels['total']:
    break
  index += channels['count']

# Récupération du répertoire racine du repo
rootFolder = os.path.join(os.path.dirname(__file__), '..')
# Répertoire pour stocker le fichier de sortie
dataFolder = os.path.join(rootFolder, 'public', 'data')

info = {
  "updated": "updated {:02}/{:02}/{:04}".format(now.day, now.month, now.year),
  "labels": labels,
  "messagesByChannel": messagesByChannel,
  "usersByChannel": usersByChannel
}

statsFilePath = os.path.abspath(
    os.path.join(dataFolder, 'messagesByChannel.json'))
with open(statsFilePath, "w") as file_write:
  json.dump(info, file_write)

