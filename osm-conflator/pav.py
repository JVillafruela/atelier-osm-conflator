# Import points d'apport volontaires de la métropole de Grenoble
# https://wiki.openstreetmap.org/wiki/Grenoble_groupe_local/import_metropole-grenoble
#Usage :
#conflate pav.py -i data/pav-communes/pav-Claix.tsv -o pav.osm -c pav.json

# Champ  "source" du changeset
source = 'Grenoble-Alpes Métropole'
# Identifiants opendata copiés dans le tag "ref:FR:METRO:PAV"  
dataset_id = 'FR:METRO:PAV'
# Requête Overpass API : [amenity="recycling"] (limitée à la bbox du jeu de données)
query = [('amenity', 'recycling')]
# Les valeurs de ces tags remplacent les valeurs des objets OSM.
master_tags = ('ref','operator','recycling_type','recycling:glass','recycling:waste','start_date','location')
# Regarder au maximum 20 mètres autour d'un point du jeu de données.
max_distance = 20

# A list of SourcePoint objects. Initialize with (id, lat, lon, {tags}).
def dataset(fileobj):
    import logging
    #réouverture du fichier en mode texte
    fname = fileobj.name
    fileobj.close()
    fileobj = open(fname, 'r')
    n=0
    data = []
    for line in fileobj: 
        #print(line)

        n=n+1
        if n==1: #en-tête
            continue
        try:
            col = line.split("\t")
            gid = col[1]  # col['id']
            lon = col[24] # col['x_longitude']
            lat = col[25] # col['y_latitude']
            tags = {
                #'ref' : gid,
                'amenity': 'recycling',
                'recycling_type': 'container',
                'operator': 'La Métro'                
            } 
            if col[7]=='': #'type_dechet_code'
                tags['recycling:glass']='yes' 
            if col[7]=='OMR': #ordures ménagères
                tags['recycling:waste']='yes'  
            if col[7]=='CS': #collecte sélective
                continue # ???               
            if col[10]=='enterré': #'type_conteneur']
                tags['location']='underground'  
            try:
                lat = float(lat)
                lon = float(lon)
                data.append(SourcePoint(gid, lat, lon, tags))
            except Exception as e:
                logging.warning('PROFILE: line %d Failed to parse lat/lon/ref for  %s: %s',n, gid, str(e))                               

        except Exception as e:
            logging.warning('PROFILE: line %d Failed to get attributes : %s',n, str(e))  

    return data        
