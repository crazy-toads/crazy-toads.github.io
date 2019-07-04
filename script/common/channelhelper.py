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

def getTsunamy(channel):
    value = Tsunami.GLOBAL
    if 'description' in channel:
        if channel['description'].find("#projet") != -1:
            value |= Tsunami.PROJECT
        if channel['description'].find("#democratie") != -1:
            value |= Tsunami.DEMOCRACY
        if channel['description'].find("#ecologie") != -1:
            value |= Tsunami.ECOLOGY
        if channel['description'].find("#technologie") != -1:
            value |= Tsunami.TECHNOLOGY
    return value

class Tsunami:
    GLOBAL      = 1 << 0
    PROJECT     = 1 << 1
    DEMOCRACY   = 1 << 2
    ECOLOGY     = 1 << 3
    TECHNOLOGY  = 1 << 4

def getAllChannels(rocket):
  index = 0
  allChannels = []
  while True:
    channels = rocket.channels_list(offset= index).json()
      
    allChannels.extend([ channel for channel in channels['channels'] if 'archived' not in channel])
    if channels['count'] + channels['offset'] >= channels['total']:
      break
    index += channels['count']
  return allChannels

if __name__ == "__main__":
    print("Ce fichier est juste une librarie")