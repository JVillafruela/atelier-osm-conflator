#!/usr/bin/bash

conflate  eau-potable.py -i data/Grenoble/eau-potable/grenoble_eau_potable.geojson  -o output/eau-potable.osm -c output/eau-potable.geojson
jq '.features |= map(select(.properties.action == "create"))' eau-potable.geojson >eau-potable-create.geojson
jq '.features |= map(select(.properties.action == "modify"))' eau-potable.geojson >eau-potable-modify.geojson
