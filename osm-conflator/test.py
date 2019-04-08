import logging
fileobj = open("data/pav-communes/pav-Claix.tsv","r") 
n=0
data = []
for line in fileobj: 
    #print(line)
    n=n+1
    if n==1:
        continue
    try:
        col = line.split("\t")
        gid = col[1]  # col['id']
        lon = col[24] # col['x_longitude']
        lat = col[25] # col['y_latitude']
        tags = {
            'ref' : gid,
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
            #data.append(SourcePoint(gid, lat, lon, tags))
        except Exception as e:
            logging.warning('PROFILE: line %d Failed to parse lat/lon/ref for  %s: %s',n, gid, str(e))                               
        print(n,lat,lon,tags)
    except Exception as e:
        logging.warning('PROFILE: line %d Failed to get attributes : %s',n, str(e))  
    print(data)   