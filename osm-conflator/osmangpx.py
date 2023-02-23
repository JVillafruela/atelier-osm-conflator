import argparse
import geopandas as gpd
import json
import os

'''
  Favorite saved in OSMAnd : 

    <wpt lat="45.1853074" lon="5.715546">
        <time>2023-02-21T19:00:44Z</time>
        <name>Parking à vélos</name>
        <desc>parking rue Clément</desc>
        <type>Osm</type>
        <extensions>
            <osmand:amenity_subtype>bicycle_parking</osmand:amenity_subtype>
            <osmand:amenity_name></osmand:amenity_name>
            <osmand:collapsable_bicycle_parking_type>bicycle_parking_stands</osmand:collapsable_bicycle_parking_type>
            <osmand:osm_tag_covered_no>no</osmand:osm_tag_covered_no>
            <osmand:amenity_type>transportation</osmand:amenity_type>
            <osmand:osm_tag_capacity>20</osmand:osm_tag_capacity>
            <osmand:address>Rue Clément, Berriat Saint-Bruno</osmand:address>
            <osmand:icon>special_star</osmand:icon>
            <osmand:background>circle</osmand:background>
            <osmand:color>#eecc22</osmand:color>
            <osmand:amenity_origin>Amenity:: transportation:bicycle_parking</osmand:amenity_origin>
        </extensions>
    </wpt>

    GeoJON saved "as is" :

    <wpt lat="45.1853054" lon="5.7155496">
    <extensions>
        <osmand:action>modify</osmand:action>
        <osmand:marker-color>#0000ee</osmand:marker-color>
        <osmand:osm_id>1797992437</osmand:osm_id>
        <osmand:osm_type>node</osmand:osm_type>
        <osmand:ref_distance>6.5</osmand:ref_distance>
        <osmand:ref_id>344</osmand:ref_id>
        <osmand:tags.amenity>bicycle_parking</osmand:tags.amenity>
        <osmand:tags.bicycle_parking>stands</osmand:tags.bicycle_parking>
        <osmand:tags.check_date:capacity>2021-12-04</osmand:tags.check_date:capacity>
        <osmand:tags.covered>no</osmand:tags.covered>
        <osmand:tags_changed.capacity>20 -&gt; 10</osmand:tags_changed.capacity>
    </extensions>
    </wpt>  

'''
dirData = 'output'

gpxNs = 'osmand'
gpxNsUrl = 'https://osmand.net'

# borrowed from @Binnette
# https://github.com/Binnette/bookcases-delivrez/blob/main/ParseData.py
def dumpToGpx(data, path):
    data.to_file(path, driver='GPX', GPX_USE_EXTENSIONS=True, GPX_EXTENSIONS_NS=gpxNs, GPX_EXTENSIONS_NS_URL=gpxNsUrl)


def convertGeojsonToGpx(path):
    geojsonData = gpd.read_file(path)
    gpxFile=outfile(path)
    dumpToGpx(geojsonData, gpxFile)

# outfile('/dir/parking.geojson') => '/dir/parking.gpx'            
def outfile(path):
    (base,ext) = os.path.splitext(path)
    fname = base + '.gpx'
    if os.path.isfile(fname):
        os.remove(fname)
    return fname

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert an geojson file to a gpx file usable in OSMAnd. Only the nodes are kept as waypoints')
    parser.add_argument('file', type=argparse.FileType('r'),help='geojson file (.geojson)')
    args = parser.parse_args()
    geojsonfile = args.file.name 
    
    args.file.close()


    convertGeojsonToGpx(geojsonfile)   