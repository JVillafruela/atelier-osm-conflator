# Run with …
#   conflate profiles/glasiglus.py -o result_glasiglus/glasiglus_conflated.osm -c result_glasiglus/glasiglus_conflated_preview.json

# Where to get the latest feed
download_url = 'https://www.berlin-recycling.de/?option=com_storelocator&view=map&format=raw&searchall=1&Itemid=537&catid=undefined&tagid=-1&featstate=0'
# What to write for the changeset's source tag
source = 'https://www.berlin-recycling.de/service/standorte-glasiglus'
# These two lines negate each other:
dataset_id = 'berlin-recycling.de/service/standorte-glasiglus'
# We actually do not use ref:velobike tag
no_dataset_id = True
# Overpass API query:
# https://wiki.openstreetmap.org/wiki/DE_talk:Tag:amenity%3Drecycling#Beispiel_f.C3.BCr_Berliner_Glascontainer.2FGlasiglus
query = [('amenity','recycling'),('recycling_type','container'),('recycling:glass_bottles','yes')]
# Maximum lookup radius is 100 meters
max_distance = 100
# The overpass query chooses all relevant points,
# so points that are not in the dataset should be deleted
delete_unmatched = False
# If delete_unmatched were False, we'd be retagging these parkings:
tag_unmatched = {
    'fixme': 'Nicht Teil des Datensatzes von https://www.berlin-recycling.de/service/standorte-glasiglus',
}
# Overwriting these tags
master_tags = ()


def dataset(fileobj):
    import logging
    import random
    import xml.etree.ElementTree as etree

    root = etree.parse(fileobj).getroot()
    data = []
    for el in root.iter('marker'):
        try:
            lon = float(el.find('lng').text)
            lat = float(el.find('lat').text)
            gid = el.find('address').text + ' (RANDOM_ID:' + str(random.randint(1,10000))
            tags = {
                'tag_von_osm_conflate': 'todo: was wollen wir hier haben? oder löschen?',
                'amenity': 'recycling',
                'recycling_type': 'container',
                'recycling:glass_bottles': 'yes',
                'temp_lookup': 'https://www.openstreetmap.org/query?lat=' + str(lat) + '&lon=' + str(lon) + '#map=18/' + str(lat) + '/' + str(lon),
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
