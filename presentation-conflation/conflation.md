% Conflation
% Groupe local OSM Grenoble - Jérôme Villafruela
% 28/05/2018



# Conflation

Dans les SIG, la conflation est définie comme le processus qui consiste à combiner l'information géographique provenant de sources qui se chevauchent afin de conserver des données exactes, de minimiser la redondance et de réconcilier les conflits de données. [Longley et al. 2001]

# Outils

## Génériques

- Plugin Josm Conflation
- OSM Conflator
- Osmose

## Spécialisés

- Cygnus : pour les routes (Telenav)
- [Hootenanny](https://github.com/ngageoint/hootenanny)
- [OSM POI Analyser](http://openstreetmap.me/) 
- [BatiFusion](https://github.com/jecor/bati-fusion) : Cadastre (Jérôme Cornet)
- [Osmaxil](https://github.com/vince-from-nice/osmaxil) Vincent Frison : arbres, hauteur bâti.

# OSM Conflator

* écrit en Python 3 par maps.me 
* Site : https://github.com/mapsme/osm_conflate
* Doc : https://wiki.openstreetmap.org/wiki/OSM_Conflator
![workflow](images/conflate_audit_chart.jpg)

# OSM Conflator - utilisation

## paramétrage

Fichier python  wifi.py

````
# Ce profil lit un JSON préparé, donc pas de fonction "dataset".

# Champ  "source" du changeset
source = 'Grenoble-Alpes Métropole'
# Identifiants dans tag "ref:Grenoble:wifi" 
dataset_id = 'Grenoble:wifi'
# Requête Overpass API : [wifi="*"]
query = [('wifi', '*')]
# Ces valeurs de balises remplacent les valeurs des objets OSM.
master_tags = ('wifi')
# Regarder au maximum 20 mètres autour d'un jeu de données.
max_distance = 20
````

Exécution

````
conflate wifi.py -i data/wifi.json -o wifi.osm --changes preview.json
````

Visualiser le fichier preview.json dans http://geojson.io 

# Atelier

Utiliser OSM conflator sur les fichiers opendata de la Métro.

Convertir les fichiers geojson en json.

- [Bornes Wifi](http://data.metropolegrenoble.fr/ckan/dataset/bornes-wifi-gratuites-de-grenoble)
- [Horodateurs](http://data.metropolegrenoble.fr/ckan/dataset/emplacement-des-horodateurs-sur-grenoble)
- [Antennes GSM](http://data.metropolegrenoble.fr/ckan/dataset/l-ensemble-des-antennes-gsm)
- [Panneaux d'affichage libre](http://data.beta.metropole-grenoble.fr/dataset/panneaux-d-affichage-libre)