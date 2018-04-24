============
Metadata
============

The Metadata API is a foundational resource for filtering datasets, so scientists and developers can analyze exactly the data they need. The most common interaction you will have with the Metdata API will be searching for available imagery. There are two methods that return subsets of our available imagery: **Search** and **Features**.

It is important to note that these methods return image IDs and their associated metadata. To obtain image data for analysis or plotting, you pass the desired IDs to the Raster API. This is a very popular workflow among our users. 

***************
Search
***************
The most common method for returning small subsets of imagery objects. All parameters are optional, though some filtering mechanism is necessary to make the result useful. Most commonly, users filter metadata given a spatio-temporal query. A GeoJSON FeatureCollection is returned, containing a list of features each comprised of an image ID and its associated metadata.  The following are the most popular query parameters.

**Products** 
A list of one or more product IDs. A complete list of Descartes Labs' products can be obtained using the Metadata method Products. A common workflow would include listing all available products, and in turn passing the only the product IDs you are interested in as a list to this key. 

**A Spatial Query** 

One, but not more, of the following spatial types can be used to search for available imagery:

**Place**  
Our Places API houses popular political boundaries across the globe in GeoJSON format. You can search for available boundaries using the Places Find method. The returned object contains the attribute Slug, which is what you'll want to pass to this key. 

**Geometry**	   
Alternatively, you can define your own geometry as a GeoJSON or WKT region of interest explicitly. This is especially useful when the Places API doesn't have the exact boundary you need. It also allows for unique user defined shapes, such as parcels of land, fields, or construction sites. This key can also take the geometry output of our Places API. 

**DLTile**		 
The Raster API allows you to generate tiles over a given area. This is a common method for scaling up analysis over large geographic areas. The workflow includes generating a set of DLTiles using the Raster API, then iteratively running the same Metadata Search over the tiles, giving back unique image metadata available for each tile.

**Start and End Time**
These parameters allow you to set the desired start and end time for your search. They can be entered using most common date/time formats as a string. If no explicit timezone is given, the timestamp is assumed to be in UTC. For example '2012-06-01' means June 1st 2012 00:00 in UTC, '2012-06-01 00:00+02:00' means June 1st 2012 00:00 in GMT+2.


**Cloud Fraction**
Querying by cloud fraction allows you reduce the number of pixels obscured by clouds. This value should be entered as a float between 0 and 1. 1 allows for 100% cloud cover, and 0% for none what-so-ever. It is good to keep in mind that this metdata belongs to the entire scene, so if you are clipping the image by a geometry, there is a good chance the percentage does not directly apply to your portion of the scene. For example, an image with .5 cloud fraction, when clipped, may be completely free of clouds, or could be entirely covered. 

The following example demonstrates passing all of the above parameters to Search to access a subset of imagery. The fifth line collects the image IDs. You can then pass this list to our Raster API Ndarray method to get back their data. 

.. code-block::

 import descarteslabs as dl
 >>> new_mexico = dl.places.find('north-america_united-states_new-mexico')
 >>> new_mexico_shape = new_mexico[0]['slug']
 >>> features = dl.metadata.search("landsat:LC08:PRE:TOAR",start_time='2016-03-01',end_time='2016-06-30', cloud_fraction=.15, place=new_mexico_shape)
 >>> ids = [f['id'] for f in features['features']]
 >>> print("There are {} images over New Mexico that are 15% or less cloudy from March to June in 2016".format(len(ids)))
 There are 93 images over New Mexico that are 15% or less cloudy from March to June in 2016


***************
Features 
***************
Similar to Search, this is the most efficient method for accessing image IDs and their metadata. All parameters are optional. This method is built to handle requests resulting in 10000 returns or more, though it works well for smaller subsets, too. A generator of GeoJSON feature objects is returned, allowing you to efficiently scroll through and access the search results. The input parameters are exactly the same, except no limit is applicable. Instead, a Batch Size may be set to adjust the number of features to fetch per request.

Here's an example of counting all Landsat 8 TOAR images over the US in our catalog captured in a 6 month period.

.. code-block::

 import descarteslabs as dl
 >>> us = dl.places.find('north-america_united-states')
 >>> us_shape = us[0]['slug']
 >>> features = dl.metadata.features("landsat:LC08:PRE:TOAR",start_time='2016-01-01',end_time='2016-06-30', place=us_shape)
 >>> total = 0
 >>> for f in features: 
 >>> 	total += 1                    
 >>> print(There were {} Landsat 8 TOAR images captured over the US from January to June in 2016.".format(total))
 There were 8314 Landsat 8 TOAR images captured over the US from January to June in 2016.

