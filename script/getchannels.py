# coding: utf8

# toutes les chaines sont en unicode (même les docstrings)
from __future__ import unicode_literals

from pprint import pprint
from rocketchat_API.rocketchat import RocketChat
import json
import dev_config as cfg

def getNodesOrigin(channel):
  nodes = []
  if 'description' not in channel:
    nodes.append("global")
    return nodes

  if channel['description'].find("#projet") != -1:
    nodes.append("project")
  if channel['description'].find("#democratie") != -1:
    nodes.append("democratie")
  if channel['description'].find("#ecologie") != -1:
    nodes.append("ecologie")
  if channel['description'].find("#technologie") != -1:
    nodes.append("technologie")

  if not nodes:
    nodes.append("global")

  return nodes

colorInfo = { 
  'global': 'orange',
  'technologie': 'gray',
  'democratie': 'red',
  'ecologie': 'green',
  'project': 'blue'
}

rocket = RocketChat(cfg.rocket['user'], cfg.rocket['password'], server_url='https://coa.crapaud-fou.org')

edge_index = 0
datas = []
datas.append( { 'data':{'id':'mare', 'label': 'mare', 'size': '300', 'color': 'black', 'href': 'https://coa.crapaud-fou.org/'}})
datas.append( { 'data':{'id':'global', 'label': 'global', 'size': '200', 'color': colorInfo['global'], 'href': 'https://coa.crapaud-fou.org/'}})
datas.append( { 'data':{'id':'ecologie', 'label': 'ecologie', 'size': '200', 'color': colorInfo['ecologie'], 'href': 'https://coa.crapaud-fou.org/'}})
datas.append( { 'data':{'id':'democratie', 'label': 'democratie', 'size': '200', 'color': colorInfo['democratie'], 'href': 'https://coa.crapaud-fou.org/'}})
datas.append( { 'data':{'id':'technologie', 'label': 'technologie', 'size': '200', 'color': colorInfo['technologie'], 'href': 'https://coa.crapaud-fou.org/'}})
datas.append( { 'data':{'id':'project', 'label': 'projet', 'size': '200', 'color': colorInfo['project'], 'href': 'https://coa.crapaud-fou.org/'}})
datas.append( { 'data':{'id': 'edge_' + str(edge_index), 'source': 'mare', 'target': 'global', 'color': colorInfo['global']}})
edge_index += 1
datas.append( { 'data':{'id': 'edge_' + str(edge_index), 'source': 'mare', 'target': 'ecologie', 'color': colorInfo['ecologie']}})
edge_index += 1
datas.append( { 'data':{'id': 'edge_' + str(edge_index), 'source': 'mare', 'target': 'democratie', 'color': colorInfo['democratie']}})
edge_index += 1
datas.append( { 'data':{'id': 'edge_' + str(edge_index), 'source': 'mare', 'target': 'technologie', 'color': colorInfo['technologie']}})
edge_index += 1
datas.append( { 'data':{'id': 'edge_' + str(edge_index), 'source': 'mare', 'target': 'project', 'color': colorInfo['project']}})
edge_index += 1

index = 0
nbChannels = 0
nbCohorte = 0
totalChannels = 0
while True:  
  channels = rocket.channels_list(offset= index).json()
  totalChannels = channels['total']

  for channel in channels['channels']:
    if channel['name'].find('cohorte') != -1:
      nbCohorte += 1
      continue

    node =  {
      'data' : {
        'id': channel['_id'],
        'label': channel['fname'] if 'fname' in channel else channel['name'],
        'size': '100',
        'color': 'grey',
        'href': 'https://coa.crapaud-fou.org/channel/'+channel['name']
      }
    }
    datas.append(node)

    nodesOrigin = getNodesOrigin(channel)
    for nodeOrigin in nodesOrigin:
      if nodeOrigin is not None:
        datas.append( { 'data':{'id': 'edge_' + str(edge_index), 'source': nodeOrigin, 'target': channel['_id'], 'color': colorInfo[nodeOrigin]}})
        edge_index += 1

    nbChannels += 1

  if channels['count'] + channels['offset'] >= channels['total']:
    break
  index += channels['count']

with open('./public/data/result.json', "w") as file_write:
  json.dump(datas, file_write)

pprint("Nb displayed channels : " + str(nbChannels))
pprint("Nb cohorte channels : " + str(nbCohorte))
pprint("Nb total channels : " + str(totalChannels))