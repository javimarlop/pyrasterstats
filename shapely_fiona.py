from shapely.geometry import mapping, shape
from shapely.ops import cascaded_union
from fiona import collection

with collection("some_buffer.shp", "r") as input:
    schema = input.schema.copy()
    with collection(
            "some_union.shp", "w", "ESRI Shapefile", schema) as output:
        shapes = []
        for f in input:
            shapes.append(shape(f['geometry']))
        merged = cascaded_union(shapes)
        output.write({
            'properties': {
                'name': 'Buffer Area'
                },
            'geometry': mapping(merged)
            })
##
import fiona
from shapely.geometry import shape
with fiona.open('sites.shp', 'r') as input:
    with open('hw1a.txt', 'w') as output:
       for pt in input:
           id = pt['properties']['id']
           cover = pt['properties']['cover']
           x = str(shape(pt['geometry']).x)
           y = str(shape(pt['geometry']).y)
           output.write(id + ' ' + x + ' ' + y+ ' ' + cover + '\n')
##
from shapely.geometry import mapping, shape
import fiona
# Read the original Shapefile
with fiona.collection('yourfile.shp', 'r') as input:
# The output has the same schema
schema = input.schema.copy()
# write a new shapefile
with fiona.collection('yourcopyfile.shp', 'w', 'ESRI Shapefile', schema) as output:
    for elem in input:
         elem['properties']['field'] = 'whatyouwant' # or a function, or...
         output.write({'properties': elem['properties'],'geometry': mapping(shape(elem['geometry']))})