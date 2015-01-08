# dissolve the shapefile by the wdpaid field!
import fiona
from rasterstats import zonal_stats

# an iterable of objects with geo_interface

lyr = fiona.open('sierranevada2.shp')

features = (x for x in lyr if x['properties']['wdpa_id'])# == '209561139')

a = zonal_stats(features, 'test.tif',copy_properties=True,stats="std count")

features = (x for x in lyr if x['properties']['wdpa_id'])# == '209561139')

acat = zonal_stats(features, 'test.tif', categorical=True, copy_properties=True)

# test

features = (x for x in lyr if x['properties']['wdpa_id'] == '209561139')

a = zonal_stats(features, 'test.tif',copy_properties=True,stats="min max median mean std count sum")

