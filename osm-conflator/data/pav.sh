curl -L 'https://sigmetropole.lametro.fr/geoserver/open_data/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=open_data:v_opendata_ctd_pav_tous&srsName=EPSG:4326&outputFormat=json' -o pav.json
curl -L 'https://sigmetropole.lametro.fr/geoserver/open_data/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=open_data:v_opendata_ctd_pav_tous&srsName=EPSG:4326&outputFormat=csv' -o pav.csv
dos2unix pav.csv
#apt install csvtool #https://colin.maudry.com/csvtool-manual-page/
csvtool -t COMMA -u TAB cat pav.csv >pav.tsv