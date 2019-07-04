# coding: utf8

# toutes les chaines sont en unicode (même les docstrings)
from __future__ import unicode_literals

from pprint import pprint
from rocketchat_API.rocketchat import RocketChat
import json
import dev_config as cfg
import os
import re
from common.channelhelper import getNodesOrigin, getAllChannels, Tsunami

def main():
  
  colorInfo = { 
    'global': 'orange',
    'technologie': 'gray',
    'democratie': 'red',
    'ecologie': 'green',
    'project': 'blue'
  }

  rocket = RocketChat(cfg.rocket['user'], cfg.rocket['password'], server_url=cfg.rocket['server'])

  sizebase = 100
  datas = []
  datas.append( { 'data':{'id':'global', 'label': 'global', 'size': sizebase, 'color': colorInfo['global'], 'href': 'https://coa.crapaud-fou.org/'}})
  datas.append( { 'data':{'id':'ecologie', 'label': 'ecologie', 'size': sizebase, 'color': colorInfo['ecologie'], 'href': 'https://coa.crapaud-fou.org/'}})
  datas.append( { 'data':{'id':'democratie', 'label': 'democratie', 'size': sizebase, 'color': colorInfo['democratie'], 'href': 'https://coa.crapaud-fou.org/'}})
  datas.append( { 'data':{'id':'technologie', 'label': 'technologie', 'size': sizebase, 'color': colorInfo['technologie'], 'href': 'https://coa.crapaud-fou.org/'}})
  datas.append( { 'data':{'id':'project', 'label': 'projet', 'size': sizebase, 'color': colorInfo['project'], 'href': 'https://coa.crapaud-fou.org/'}})

  cohortes = { 'fr': { 'updateMap': 'france_fr'}}
  cohortescolor = { 'fr': 'green' }
  nbChannels = 0
  nbCohorte = 0
  totalChannels = 0
  for channel in getAllChannels(rocket):
    print("{}".format(channel['name']))
      
    if channel['name'].find('cohorte') != -1:
      if 'description' in channel:
        m = re.findall(r'#([\w-]+)', channel['description'])
        for region in m:
          cohortescolor.update( { region: 'green' } )
          cohortes.update( { region: { 'link': channel['name']}})
      nbCohorte += 1
      continue

    size = channel['usersCount']

    if (channel['_id'] == 'GENERAL') or (channel['_id'] == 'rp5gdRrZubMKic3Nk') :
      size = sizebase

    node =  {
      'data' : {
        'id': channel['_id'],
        'label': channel['fname'] if 'fname' in channel else channel['name'],
        'size': size,
        'color': 'grey',
        'href':  f"{cfg.rocket['server']}/channel/{channel['name']}"
      }
    }
    datas.append(node)

    nodesOrigin = getNodesOrigin(channel)
    for nodeOrigin in nodesOrigin:
      if nodeOrigin is not None:
        datas.append( { 'data':{'source': nodeOrigin, 'target': channel['_id'], 'color': colorInfo[nodeOrigin]}})

    nbChannels += 1

  # Récupération du répertoire racine du repo
  rootFolder = os.path.join(os.path.dirname(__file__), '..')
  # Répertoire pour stocker le fichier de sortie
  dataFolder = os.path.join(rootFolder, 'public','data')
  # Faut il essayer de le créer au cas ou?
  # os.makedirs(dataFolderPath, exist_ok=True)
  channelsFilePath = os.path.abspath(os.path.join(dataFolder,'channelslist.json'))

  #print("Ecriture dans : "+channelsFilePath)

  with open(channelsFilePath, "w") as file_write:
    json.dump(datas, file_write)

  cohortecolorFilePath = os.path.abspath(os.path.join(dataFolder,'cohortescolor.json'))
  with open(cohortecolorFilePath, "w") as file_write:
    json.dump(cohortescolor, file_write)

  cohorteFilePath = os.path.abspath(os.path.join(dataFolder,'cohorteslist.json'))
  with open(cohorteFilePath, "w") as file_write:
    json.dump(cohortes, file_write)

  pprint("Nb displayed channels : " + str(nbChannels))
  pprint("Nb cohorte channels : " + str(nbCohorte))

if __name__ == "__main__":
    main()