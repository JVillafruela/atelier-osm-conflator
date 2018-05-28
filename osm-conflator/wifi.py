# Ce profil lit un JSON préparé, donc pas de fonction "dataset".

# Champ  "source" du changeset
source = 'Grenoble-Alpes Métropole'
# Identifiants dans tag "ref:Grenoble:wifi" 
dataset_id = 'Grenoble:wifi'
# Requête Overpass API : [wifi="*"]
query = [('wifi', '*')]
# Ces valeurs de balises remplacent les valeurs des objets OSM.
master_tags = ('wifi')
# Regarder au maximum 20 mètres autour d'un jeu de données.
max_distance = 20
