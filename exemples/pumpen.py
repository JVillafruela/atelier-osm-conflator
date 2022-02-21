# Run with …
#   conflate profiles/pumpen.py -o result_pumpen/pumpen_conflated.osm -c result_pumpen/pumpen_conflated_preview.json

# Where to get the latest feed
download_url = 'https://www.giessdenkiez.de/data/pumps.geojson'
# What to write for the changeset's source tag
source = 'Geoportal Berlin / ATKIS'
# These two lines negate each other:
dataset_id = 'giessdenkiez_pumpen'
# We actually do not use ref:velobike tag
no_dataset_id = True
# Overpass API query:
# http://overpass-turbo.eu/s/PPR
query = [('man_made','water_well'), ('description','Berliner Straßenbrunnen')]
# Maximum lookup radius is 100 meters
max_distance = 100
# The overpass query chooses all relevant points,
# so points that are not in the dataset should be deleted
delete_unmatched = False
# If delete_unmatched were False, we'd be retagging these parkings:
tag_unmatched = {
    'fixme': 'Nicht Teil des Datensatzes von https://www.giessdenkiez.de/data/pumps.geojson',
}
# Overwriting these tags
master_tags = ()


def dataset(fileobj):
    import codecs
    import json
    import logging
    import random

    # Specifying utf-8 is important, otherwise you'd get "bytes" instead of "str"
    source = json.load(codecs.getreader('utf-8')(fileobj))
    data = []
    for el in source['features']:
        try:
            lon = el['geometry']['coordinates'][0]
            lat = el['geometry']['coordinates'][1]
            gid = 'https://www.openstreetmap.org/query?lat=' + str(lat) + '&lon=' + str(lon) + '#map=18/' + str(lat) + '/' + str(lon) + '&random_id=' + str(random.randint(1,10000))
            tags = {
                'tag_von_osm_conflate': 'todo: was wollen wir hier haben? oder löschen?',
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
