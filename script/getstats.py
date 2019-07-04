# coding: utf8

# toutes les chaines sont en unicode (même les docstrings)
from __future__ import unicode_literals

# from pprint import pprint
from rocketchat_API.rocketchat import RocketChat
import json
import dev_config as cfg
import os
import random
from datetime import datetime
from monthdelta import monthdelta
from common.channelhelper import getTsunamy, Tsunami, getAllChannels

def getColor():
    r = random.randrange(255)
    g = random.randrange(255)
    b = random.randrange(255)
    return 'rgb({:0},{:0},{:0})'.format(r,g,b)

def save(info):
  # Récupération du répertoire racine du repo
  rootFolder = os.path.join(os.path.dirname(__file__), '..')
  # Répertoire pour stocker le fichier de sortie
  dataFolder = os.path.join(rootFolder, 'public', 'data')

  statsFilePath = os.path.abspath(
      os.path.join(dataFolder, 'channelsstat.json'))
  with open(statsFilePath, "w") as file_write:
    json.dump(info, file_write)

def createElement(label, color, data) :
  return {
    "label": label,
    "backgroundColor": color,
    "data": data
  }

def setTsunamyInfo(tsunamy, messagesDataTsunamy, id, length):
  if tsunamy & Tsunami.GLOBAL:
    messagesDataTsunamy[Tsunami.GLOBAL][id] += length
  if tsunamy & Tsunami.PROJECT:
    messagesDataTsunamy[Tsunami.PROJECT][id] += length
  if tsunamy & Tsunami.DEMOCRACY:
    messagesDataTsunamy[Tsunami.DEMOCRACY][id] += length
  if tsunamy & Tsunami.ECOLOGY:
    messagesDataTsunamy[Tsunami.ECOLOGY][id] += length
  if tsunamy & Tsunami.TECHNOLOGY:
    messagesDataTsunamy[Tsunami.TECHNOLOGY][id] += length

def main():
  rocket = RocketChat(cfg.rocket['user'], cfg.rocket['password'],
                      server_url=cfg.rocket['server'])
  
  labels = [None] * 12
  messagesByChannel = []
  usersByChannel = []
  messagesDataTsunamy = {
    Tsunami.GLOBAL: [0] * 12,
    Tsunami.PROJECT: [0] * 12,
    Tsunami.DEMOCRACY: [0] * 12,
    Tsunami.ECOLOGY: [0] * 12,
    Tsunami.TECHNOLOGY: [0] * 12,
  }
  usersGlobal = []

  now = datetime.now()
  date = datetime(now.year, now.month, now.day, 0,0,0)

  info = {
    "updated": "updated {:02}/{:02}/{:04}".format(now.day, now.month, now.year),
    "labels": labels,
    "messagesByChannel": messagesByChannel,
    "usersByChannel": usersByChannel,
    "messagesByTsunamy": [
      createElement("global", getColor(), messagesDataTsunamy[Tsunami.GLOBAL]),
      createElement("project", getColor(), messagesDataTsunamy[Tsunami.PROJECT]),
      createElement("democratie", getColor(), messagesDataTsunamy[Tsunami.DEMOCRACY]),
      createElement("ecologie", getColor(), messagesDataTsunamy[Tsunami.ECOLOGY]),
      createElement("technologie", getColor(), messagesDataTsunamy[Tsunami.TECHNOLOGY])
    ],
    "usersGlobal": usersGlobal
  }

  uniqueUserGlobal = [None] * 12

  for channel in getAllChannels(rocket):
    dataMess = []
    dataUsers = []
    print( channel['name'] )
    begin = date - monthdelta(12)
    end = begin + monthdelta(1)

    tsunamy = getTsunamy(channel)    

    for id in range(0, 12):
      if uniqueUserGlobal[id] == None:
        uniqueUserGlobal[id] = []
      labels[id] = begin.strftime("%b %Y")
      print(f"\t{labels[id]}")
      begindate =  begin.isoformat()
      enddate = end.isoformat()

      resultMess = rocket.channels_history(channel['_id'], oldest= begindate, latest=enddate, count= 10000).json()
      resultMess = list(filter(lambda mess: 't' not in mess, resultMess['messages']))
      length = len(resultMess)
      dataMess.append(length)

      if length > 0:
        setTsunamyInfo(tsunamy, messagesDataTsunamy, id, length)

        users = []
        for mess in resultMess:
          users.append(mess['u']['_id'])
          uniqueUserGlobal[id].append(mess['u']['_id'])
        usersDistinct = set(users)
        dataUsers.append(len(usersDistinct))
      else:
        dataUsers.append(0)

      begin = end
      end = begin + monthdelta(1)
  
    color = getColor()
    messageByChannel = createElement(channel['name'], color,dataMess)
    userByChannel = createElement( channel['name'], color,dataUsers)

    messagesByChannel.append(messageByChannel)
    usersByChannel.append(userByChannel)

  for id in range(0, 12):
    uniqueUserGlobal[id] = len(set(uniqueUserGlobal[id]))

  userGlobal = createElement( 'global', 'red', uniqueUserGlobal)
  usersGlobal.append(userGlobal)

  save(info)



if __name__ == "__main__":
    main()