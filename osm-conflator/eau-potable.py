# Conflation point d'eau potable de Grenoble

#Usage :
#conflate  eau-potable.py -i data/Grenoble/eau-potable/grenoble_eau_potable.geojson  -o eau-potable.osm -c eau-potable.geojson

# Champ  "source" du changeset
source = 'Grenoble-Alpes Métropole'
# Rapprochement géométrique seulement (
no_dataset_id = True
# Requête Overpass API : ('key','value') (limitée à la bbox du jeu de données)
query = [('amenity', 'drinking_water')]  
# Les valeurs de ces tags remplacent les valeurs des objets OSM.
master_tags = ('operator','amenity')
# Regarder au maximum 100 mètres autour d'un point du jeu de données.
max_distance = 50
# pour permettre les points groupés
#duplicate_distance = 0 

 

# A list of SourcePoint objects. Initialize with (id, lat, lon, {tags}).
# {
#   "type": "FeatureCollection",
#   "features": [
#     {
#       "type": "Feature",
#       "properties": {},
#       "geometry": {
#         "type": "Point",
#         "coordinates": [
#           5.735241,
#           45.195728
#         ]
#       },
#       "id": "I4NzA"
#     },

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
            gid = el['id']
            tags = {
                'amenity': 'drinking_water',
                'man_made': 'water_tap',
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

