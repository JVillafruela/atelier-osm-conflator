# Import arceaux à vélo de Grenoble
# https://wiki.openstreetmap.org/wiki/Grenoble_groupe_local/import_metropole-grenoble
#Usage :
#conflate arceaux.py -i data/Grenoble/Arceaux_EPSG4326.geojson -o arceaux.osm -c arceaux.geojson

# Champ  "source" du changeset
source = 'Grenoble-Alpes Métropole'
# Identifiants opendata copiés dans le tag "ref:$dataset_id"  
# dataset_id = 'FR:GrenobleAlpesMetropole:Arceaux'
# Rapprochement géométrique seulement (
no_dataset_id = True
# Requête Overpass API : ('key','value') (limitée à la bbox du jeu de données)
query = [('amenity', 'bicycle_parking'), ('bicycle_parking', 'stands')]  
# Les valeurs de ces tags remplacent les valeurs des objets OSM.
master_tags = ('ref','operator','bicycle_parking','capacity')
# Regarder au maximum 20 mètres autour d'un point du jeu de données.
max_distance = 20
# pour permettre les PAV groupés
duplicate_distance = 0 

 

# A list of SourcePoint objects. Initialize with (id, lat, lon, {tags}).
#{
#    "name": "Arceaux_EPSG4326",
#    "type": "FeatureCollection",
#    "features": [{
#            "type": "Feature",
#            "geometry": {
#                "type": "Point",
#                "coordinates": [5.72616761182579, 45.1865894781128]
#            },
#            "properties": {
#                "MOB_ARCE_ID": 46,
#                "MOB_ARCE_NB": 1,
#                "MOB_ARCE_TYP": "nouveau modèle",
#                "MOB_ARCE_DATECRE": "20010101000000"
#            }
#        },

def dataset(fileobj):
    import codecs
    import json
    import logging

    # Specifying utf-8 is important, otherwise you'd get "bytes" instead of "str"
    source = json.load(codecs.getreader('utf-8')(fileobj))
    data = []
    for el in source['features']:
        try:
            lon = el['geometry']['coordinates'][0]
            lat = el['geometry']['coordinates'][1]
            gid = el['properties']['MOB_ARCE_ID']
            capacity = 2 * el['properties']['MOB_ARCE_NB']
            tags = {
                'amenity': 'bicycle_parking',
                'bicycle_parking': 'stands',
                'capacity': capacity
            }
            try:
                lat = float(lat)
                lon = float(lon)
                data.append(SourcePoint(gid, lat, lon, tags))
            except Exception as e:
                logging.warning('PROFILE: Failed to parse lat/lon for gid %s: %s', gid, str(e))
        except Exception as e:
            logging.warning('PROFILE: Failed to get attributes for gid: %s', str(e))
    return data

