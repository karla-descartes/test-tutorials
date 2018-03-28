The Metadata API serializes and reports all information about available satellite products, scientifically derived data, and individual images. This includes specific information ranging from what spectral bands are captured by satellite sensors, date of capture, and cloud coverage for images, to what pre-computed indicies Descartes Labs scientists have added. The Metadata API is a foundational resource for filtering datasets, so scientists and developers can analyze exactly the data they need. 



```dl.available_products()```
Takes no parameters and returns a list of available products. Each entry is a dictionary including the keys ```product```, which can be used as the ```product``` parameter in other metadata calls, and ```sat_id```. 

```dl.metadata.bands()```
Returns a list of bands available for a given ```product``` or list of products. If no ```product``` is supplied, it returns a list of all bands for all products. Additionally, you can query based on: ```wavelength ```, ```resolution```, and ```tags```.  Each entry returned can contain the following keys, where applicable: 

	wavelength_max'	
	data_unit
	wavelength_center
	color
	dtype	
	name_vendor
	processing_level
	type
	id	
	nbits	
	srcfile	
	wavelength_unit	
	wavelength_min
	res_factor	
	product	
	data_unit_description	
	description	
	tags	
	resolution_unit	
	vendor_order	
	physical_range	
	srcband	
	name_common	
	data_description	
	name	
	default_range	
	data_range	
	jpx_layer	
	wavelength_fwhm	
	owner_type	
	nodata	
	resolution

If you want to get all available bands given a product, use something similar to: 
	
	bands = dl.metadata.bands('landsat:LC08:PRE:TOAR')
	len(bands)
	>>> 16
	[band['name'] for band in bands]
	>>> ['coastal-aerosol', 'blue', 'green', 'red', 'nir', 'swir1', 'swir2', 'cirrus', 'tirs1', 'alpha', 'bright-mask', 'cloud-mask', 'qa_cirrus', 'qa_cloud', 'qa_snow', 'qa_water']



```dl.metadata.derived_bands()```   
Returns a list of scientifically derived bands. The optional parameter ```bands``` limits the return to those products computed using one or all of the listed spectral bands passed in. The parameter ```require_bands``` is a boolean value used to explicity state if the searched bands must contain all the spectral bands passed in ```bands```. Each returned record has the following keys: 

    bands 
    data_range
    description 
    dtype
	function_name
	id
	name 
	name_common
	physical_range

This example will output all derived bands' names that use the near infrared spectral band:

		derived_nir_bands = dl.metadata.derived_bands(bands=['nir'], require_bands=True)
		derived_nir_names = [band['name'] for band in derived_nir_bands]```
		derived_nir_names
		>>>['bai', 'evi', 'nbr, 'ndvi', 'ndwi', 'ndwi1', 'ndwi2']


```dl.metadata.features()```
Similar to ```dl.metadata.search()```, but instead, returns a generator that allows you to efficiently scroll through search results. This is advantageous when assessing large amounts of data. Passing in no parameters will return all available features as a generator in the Descartes Labs platform. The following example counts all Landsat 8 TOAR scenes available from January 1, 2016 to March 1, 2016. 
	
	features = dl.metadata.features(
		"landsat:LC08:PRE:TOAR",                             
		start_time='2016-01-01',                             
		end_time="2016-03-01"
	)
	total = 0
	for f in features:                     
		total += 1

	print(total)

```dl.metadata.get()```
Returns the metadata for a single image given an image identifier. The following example demonstrates the keys returned in the metadata dictionary. 

	meta = dl.metadata.get("sentinel-3:OLCI_RGB:meta_2017-01-02-1115_29N_07_S3A_v0")
	meta.keys()
	>>> dict_keys(['acquired', 'bits_per_pixel', 'bucket', 'cs_code', 'descartes_version', 'duration', 'file_sizes', 'files', 'fill_fraction', 'geometry', 'geotrans', 'id', 'identifier', 'key', 'processed', 'product', 'proj4', 'projcs', 'published', 'raster_size', 'sat_id', 'tile_id'])


```dl.metadata.get_by_ids()```
Similar to ```get()```, but instead takes a list of ```image_id```s, and returns a list of metadata entries respective to the input ids. If an image is not found, that id is skipped. 

```dl.metadata.get_band()``` 
Retrieves metadata given a ```band_id```. A ```band_id``` can be obtained using ```dl.metadata.bands()```. 


```dl.metadata.get_bands_by_key()```
Similar to ```bands()```, but rather than a ```product_id```, takes an ```image_id```.  An ```image_id``` can be obtained using ```search()```. 


```dl.metadata.get_derived_band()```
Given a ```derived_band_id```, this method will return information about a single product. The following example demonstrates using ```derived_bands``` to obtain available products and their associated ids, then passing one of the ids to ```get_derived_band()```, and accessing only the ```description``` of that output.  

	derived_bands = dl.metadata.derived_bands()
	[band['id'] for band in derived_bands]
	>>> ['derived:bai', 'derived:evi', 'derived:nbr', 'derived:ndvi', 'derived:ndwi', 'derived:ndwi1', 

	'derived:ndwi2', 'derived:rsqrt', 'derived:visual_cloud_mask']
	dl.metadata.get_derived_band('derived:nbr')['description']
	>>> 'Normalized Burned Ratio (nir - swir2)/(nir + swir2)'


```dl.metdata.products()```
	Returns all available image products, given an optional set of query parameters. The following bit of code shows how to create a dictionary of ```product_id``` keys with the value being the associated ```product_title```.

	products = dl.metadata.products()
	product_ids_titles = {}
		
	for prod in products:
		product_ids_titles[prod['id']] = prod['title']

	>>>{ 'landsat:LC08:01:RT:TOAR': 'Landsat 8 Real Time Collection',
	 'landsat:LC08:01:T1:TOAR': 'Landsat 8 Tier 1 Collection',
	 'landsat:LC08:01:T2:TOAR': 'Landsat 8 Tier 2 Collection',
	 'landsat:LC08:PRE:LaSRC': 'Landsat 8 Pre-collection LaSRC Surface Reflectance',
	 'landsat:LC08:PRE:LaSRC:composite:2013-06-01:2000:v0': 'LC08 LaSRC composite',
	 'landsat:LC08:PRE:TOAR': 'Landsat 8',
	 'landsat:LE07:01:RT:TOAR': 'Landsat 7 Real Time Collection',
	 'landsat:LE07:01:T1:TOAR': 'Landsat 7 Tier 1 Collection',
	 'landsat:LE07:01:T2:TOAR': 'Landsat 7 Tier 2 Collection',
	 'landsat:LE07:PRE:TOAR': 'Landsat 7',
	 'landsat:LT04:PRE:TOAR': 'Landsat 4',
	 'landsat:LT05:PRE:TOAR': 'Landsat 5',
	 'modis:09:CREFL': 'MODIS Aqua/Terra',
	 'modis:09:max-ndvi:16-day:v8b': 'Max NDVI calculation based on MODIS',
	 'sentinel-1:GRD': 'Sentinel-1 A/B',
	 'sentinel-1:SLC:v0': 'Interferogram of Sentinel 1 VV band',
	 'sentinel-2:L1C': 'Sentinel-2 A/B',
	 'sentinel-3:OLCI_RGB': 'Sentinel-3',
	 'srtm:GL1003': 'SRTM Shuttle Radar Topology Mission',
	 'texas-orthoimagery:v0': 'Texas Orthoimagery Program 50cm',
	 'usda:cdl': 'Cropland Data Layer',
	 'usda:cdl:v1': 'Cropland Data Layer v1',
	 'usda:naip:rgbn': 'National Agricultural Imagery Program',
	 'usda:naip:rgbn:v1': 'National Agricultural Imagery Program'}

```dl.metadata.get_product()```




ids 
keys 
products
search 
sources 
summary
properties





















