from osgeo import gdal, ogr
#import numpy as np

# Define pixel_size and NoData value of new raster
pixel_size = 25
NoData_value = -9999

# Filename of input OGR file
vector_fn = 'roads.shp'

# Filename of the raster Tiff that will be created
raster_fn = 'roads25m.tif'

# Open the data source and read in the extent
source_ds = ogr.Open(vector_fn)
source_layer = source_ds.GetLayer()
x_min, x_max, y_min, y_max = source_layer.GetExtent()

# Create the destination data source
x_res = int((x_max - x_min) / pixel_size)
y_res = int((y_max - y_min) / pixel_size)
#target_ds = gdal.GetDriverByName('MEM').Create('', x_res, y_res, 1, gdal.GDT_Int32)
target_ds = gdal.GetDriverByName('GTiff').Create(raster_fn, x_res, y_res, 1, gdal.GDT_Byte)
target_ds.SetGeoTransform((x_min, pixel_size, 0, y_max, 0, -pixel_size))
band = target_ds.GetRasterBand(1)
band.SetNoDataValue(NoData_value)

# Rasterize
gdal.RasterizeLayer(target_ds, [1], source_layer, burn_values=[1])

#array = band.ReadAsArray().astype(np.int32)
#print array
#np.unique(array)

