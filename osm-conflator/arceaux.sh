#!/usr/bin/bash

conflate  arceaux.py -i  data/Grenoble/arceaux/arceaux_epsg4326-2023-07.geojson -o output/arceaux.osm -c output/arceaux.geojson

jq '.features |= map(select(.properties.action == "create"))' output/arceaux.geojson >output/arceaux-create.geojson
jq '.features |= map(select(.properties.action == "modify"))' output/arceaux.geojson >output/arceaux-modify.geojson
