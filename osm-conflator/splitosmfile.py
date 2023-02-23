import argparse
import osmium
import os.path

class NodeWriter(osmium.SimpleHandler):
    def __init__(self, writer_c, writer_m ):
        osmium.SimpleHandler.__init__(self)
        self.writer_c = writer_c
        self.writer_m = writer_m

    def node(self, n):
        if  n.id < 0 : # new node
            self.writer_c.add_node(n)
        else:
            self.writer_m.add_node(n)
            
# outfile('/dir/parking.osm',create') => '/dir/parking-create.osm'            
def outfile(path,suffix):
    (base,ext) = os.path.splitext(path)
    fname = base + '-' + suffix + ext
    if os.path.isfile(fname):
        os.remove(fname)
    return fname
        
if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Split an OSM file in two, new nodes on one side, modified ones on the other.')
    parser.add_argument('file', type=argparse.FileType('r'),help='OpenStreetMap josm file (.osm)')
    args = parser.parse_args()
    osmfile = args.file.name 
    outfile_c = outfile(osmfile, 'create')
    outfile_m = outfile(osmfile, 'modify')
    args.file.close()
    
    writer_c = osmium.SimpleWriter(outfile_c)
    writer_m = osmium.SimpleWriter(outfile_m)
    h = NodeWriter(writer_c,writer_m)
    h.apply_file(osmfile)

          