# Adaptation from https://github.com/JVillafruela/atelier-osm-conflator/blob/master/osm-conflator/arceaux.py

# Extract name and elevation
source = "Grenoble-Alpes Métropole"
no_dataset_id = True
# Overpass API query
query = [("information", "guidepost")]
# Tags to replace
master_tags = ("name", "ele")
# Maximum lookup radius
max_distance = 50  # m


def dataset(fileobj):
    import codecs
    import json
    import logging

    source = json.load(codecs.getreader("utf-8")(fileobj))
    data = []
    for el in source["features"]:
        try:
            lon = el["geometry"]["coordinates"][0]
            lat = el["geometry"]["coordinates"][1]
            gid = el["properties"]["ogc_fid"]
            name = el["properties"]["nommobilier"]
            ele = el["properties"]["blaltitude"]
            if ele is not None:
                # Manage value like "845 m"
                ele = ele.split(" ")[0]
            tags = {
                "information": "guidepost",
                "tourism": "information",
                "name": name,
                "ele": ele,
            }
            try:
                lat = float(lat)
                lon = float(lon)
                data.append(SourcePoint(gid, lat, lon, tags))
            except Exception as e:
                logging.warning(
                    "PROFILE: Failed to parse lat/lon for gid %s: %s", gid, str(e)
                )
        except Exception as e:
            logging.warning("PROFILE: Failed to get attributes for gid: %s", str(e))
    return data
