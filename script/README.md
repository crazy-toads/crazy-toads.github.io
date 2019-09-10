# installation
## pre-requis
Il faut Python 3 & pip car le code est fait en python.
## Installation
Il faut lancer la commande pour avoir les dependences nécessaires :

    pip install -r ./requirements.txt

Il faut créer un fichier dev_config.py avec ses infos de connection au Rocket.chat

    rocket = {
        'user' : 'username',
        'password': 'pwd'
    }
# Get Channels
Permet de générer les infos pour la page  
https://crapaud-fou.org/channelslist/
## Lancer
    python getchannels.py

## Commit
Des fichiers seront créé
* [../public/data/channelslist.json](../public/data/channelslist.json)
* [../public/data/cohortescolor.json](../public/data/cohortescolor.json)
* [../public/data/cohorteslist.json](../public/data/cohorteslist.json)