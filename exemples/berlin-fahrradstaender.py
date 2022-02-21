# Source:
# - https://daten.berlin.de/datensaetze/stra%C3%9Fenbefahrung-2014-fahrradst%C3%A4nder-wfs
# - https://fbinter.stadt-berlin.de/fb/berlin/service_intern.jsp?id=s_Fahrradstaender@senstadt&type=WFS

# <gml:featureMember>
#   <fis:s_Fahrradstaender fid="s_Fahrradstaender.10202">
#     <fis:ELEM_NR>44480006_44480007.02</fis:ELEM_NR>
#     <fis:FLAECHE>0.39167427558</fis:FLAECHE>
#     <fis:FRS_ANZAHL>1</fis:FRS_ANZAHL>
#     <fis:FRS_N>1</fis:FRS_N>
#     <fis:GIS_ID>Fl_20141010_444</fis:GIS_ID>
#     <fis:LAENGE>0.0</fis:LAENGE>
#     <fis:Shape>
#       <gml:MultiPolygon>
#         <gml:polygonMember>
#           <gml:Polygon>
#             <gml:outerBoundaryIs>
#               <gml:LinearRing>
#                 <gml:coordinates cs="," decimal="." ts=" ">389025.6796000004,5813653.9889 389025.5537999999,5813652.376499999 389025.2953000003,5813652.3496 389025.4540999997,5813653.99 389025.6796000004,5813653.9889</gml:coordinates>
#               </gml:LinearRing>
#             </gml:outerBoundaryIs>
#           </gml:Polygon>
#         </gml:polygonMember>
#       </gml:MultiPolygon>
#     </fis:Shape>
#   </fis:s_Fahrradstaender>
# </gml:featureMember>

# Where to get the latest feed
# !TODO: Download ist 9,5 MB groß. Für Testing besser lokale Datei nutzen? Wie geht das?
download_url = 'https://fbinter.stadt-berlin.de/fb/wfs/data/senstadt/s_Fahrradstaender?request=GetFeature&service=WFS&version=1.0.0&TYPENAME=s_Fahrradstaender'
# What to write for the changeset's source tag
source = 'Geoportal Berlin / Straßenbefahrung 2014 - Fahrradständer'
# These two lines negate each other:
# dataset_id = 'velobike'
# We actually do not use ref:velobike tag
# no_dataset_id = True
# Overpass API query
query = [('amenity', 'bicycle_parking')]
# Maximum lookup radius is 100 meters
max_distance = 100
# The overpass query chooses all relevant points,
# so points that are not in the dataset should be deleted
delete_unmatched = True
# If delete_unmatched were False, we'd be retagging these parkings:
# !TODO:
tag_unmatched = {
    'fixme': '???',
    'amenity': None,
    'was:amenity': 'bicycle_parking'
}
# Overwriting these tags
# !TODO:
master_tags = ('capacity')

def dataset(fileobj):
    import codecs
    import json
    import logging

    # Specifying utf-8 is important, otherwise you'd get "bytes" instead of "str"
    source = json.load(codecs.getreader('utf-8')(fileobj))
    data = []
    for el in source['Items']:
        try:
            gid = int(el['fis:GIS_ID'])
            # !TODO: Fläche von gml:coordinates umwandeln in lat/lon
            lon = el['Position']['Lon']
            lat = el['Position']['Lat']
            tags = {
                'amenity': 'bicycle_parking',
                'bicycle_parking': 'stands',
                'ref:official': el['fis:GIS_ID'],
                'capacity': el['fis:FRS_ANZAHL'] * 2,
                'access': 'yes',
            }
            try:
                lat = float(lat)
                lon = float(lon)
                data.append(SourcePoint(gid, lat, lon, tags))
            except Exception as e:
                logging.warning('PROFILE: Failed to parse lat/lon for rental stand %s: %s', gid, str(e))
        except Exception as e:
            logging.warning('PROFILE: Failed to get attributes for rental stand: %s', str(e))
    return data
