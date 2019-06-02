# getchannels
## installation
## pre-requis
Il faut Python 3 & pip car le code est fait en python.
## Installation
Il faut lancer la commande pour avoir les dependences nécessaires :

    pip install -r ./requirement.txt

Il faut créer un fichier dev_config.py avec ses infos de connection au Rocket.chat

    rocket = {
        'user' : 'username',
        'password': 'pwd'
    }
# Lancer
    python getchannels.py

# Commit
Un fichier sera créé dans le répertoire [../public/data/result.json](../public/data/result.json)
