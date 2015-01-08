# source: http://pcjericks.github.io/py-gdalogr-cookbook/vector_layers.html#convert-vector-layer-to-array
import ogr, gdal
import numpy as np
vector_fn = 'sierranevada2.shp'

# Define pixel_size and NoData value of new raster
pixel_size = 1000
NoData_value = -9999

# Open the data source and read in the extent
source_ds = ogr.Open(vector_fn)
source_layer = source_ds.GetLayer()
source_srs = source_layer.GetSpatialRef()
x_min, x_max, y_min, y_max = source_layer.GetExtent()

# Create the destination data source
x_res = int((x_max - x_min) / pixel_size)
y_res = int((y_max - y_min) / pixel_size)
target_ds = gdal.GetDriverByName('MEM').Create('', x_res, y_res, gdal.GDT_Int32)
target_ds.SetGeoTransform((x_min, pixel_size, 0, y_max, 0, -pixel_size))
band = target_ds.GetRasterBand(1)
band.SetNoDataValue(NoData_value)

# Rasterize
gdal.RasterizeLayer(target_ds, [1], source_layer, options = ["ATTRIBUTE=cat"])#burn_values=[1])

# Read as array
array = band.ReadAsArray().astype(np.int32)
print array
np.unique(array)

layerDefinition = source_layer.GetLayerDefn()
for i in range(layerDefinition.GetFieldCount()):
	print layerDefinition.GetFieldDefn(i).GetName()

print "Name  -  Type  Width  Precision"
for i in range(layerDefinition.GetFieldCount()):
    fieldName =  layerDefinition.GetFieldDefn(i).GetName()
    fieldTypeCode = layerDefinition.GetFieldDefn(i).GetType()
    fieldType = layerDefinition.GetFieldDefn(i).GetFieldTypeName(fieldTypeCode)
    fieldWidth = layerDefinition.GetFieldDefn(i).GetWidth()
    GetPrecision = layerDefinition.GetFieldDefn(i).GetPrecision()
    print fieldName + " - " + fieldType+ " " + str(fieldWidth) + " " + str(GetPrecision)

feature = source_layer.GetFeature(0)
cat = feature.GetField('cat')
wdpa_id = feature.GetFieldAsString('wdpa_id')
source_layer.GetFeature(0).GetField('cat')

