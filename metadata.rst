============
Metadata
============

The Metadata API serializes and reports all information about available satellite products, scientifically derived data, and individual images. This includes information ranging from what spectral bands are captured by satellite sensors, date of capture, and cloud coverage for images, to what pre-computed indicies Descartes Labs scientists have added to products. The Metadata API is a foundational resource for filtering datasets, so scientists and developers can analyze exactly the data they need. The most common interaction you will have with the Metdata API will be searching for available imagery. There are two methods that return subsets of our imagery catalog entries: Search and Features. 

There are numerous Metadata methods that return lists of available image products and bands that can yeild useful ids to pass to Search and Features. While those are not covered at length here, they are documented in the API Reference. 

It is important to note that these methods return image IDs and their associated metadata. To obtain image data for analysis or plotting, you pass the desired IDs to the Raster API. This is a very popular workflow among our users. 

***************
Search
***************
The most commmon method for returning small subsets of imagery objects. All parameters are optional, though some filtering mechanisim is necessary to make the result useful. Most commonly, users filter metadata given a spatio-temporal query. A GeoJSON FeatureCollection is returned, containing a list of features containing image IDs and their associated metadata.  The following are the most popular query parameters. 

**Products** 
A list of one or more product IDs. A complete list of Descartes Labs' products can be obtained using the Metadata method Products. A common workflow will be to isolate a specific satellite's offerings through filtering the products. An example would be creating a list of all the IDs pertaining to Landsat 8. 

***A Spatial Query***
One, but not more, of the following spatial queries can be used to search for available imagery.

	**Place** 
	A Place requires a call to our Places API which houses popular political boundaries across the globe in GeoJSON format. The returned object contains the attribute Slug, which is what you'll want to pass into this parameter. 
	**Geometry** 
	Alternatively, you can define your own geometry as a GeoJSON or WKT region of interest explicitly. This is especially useful when the Places API doesn't have the exact boundary you need. It also allows for unique user defined shapes, such as parcels of land, fields, or construction sites.
	**DLtile*** 
	The Raster API allows you to generate tiles over a given area. This is common method for scaling up analysis over large geographic areas. A common workflow is to generate a set of DLTiles using the Raster API, then iteratively run the same Metadata Search over the tiles, giving back unique image metadata for each tile.

***Start and End Time*** 
These allow you to set the desired start and end time for your search.  These parameters accept most common date/time formats as a string. If no explicit timezone is given, the timestamp is assumed to be in UTC. For example '2012-06-01' means June 1st 2012 00:00 in UTC, '2012-06-01 00:00+02:00' means June 1st 2012 00:00 in GMT+2.

(str) – Desired ending timestamp, in any common format.

***Cloud Fraction***
(float) – Maximum cloud fraction, calculated by data provider.

***Limit*** 
(int) – Number of items to return up to the maximum of 10000.





***************
Features 
***************
Similar to Search, this is the most efficient method for returning image IDs and their metadata to the user. All parameters are optional. This method is built to handle requests resulting in 10000 returns or more, though it works well for smaller subsets, too. A generator of GeoJSON Feature objects is returned, allowing you to efficiently scroll through and access the search results. The input parameters are similar, save the following differences. 



No limit, No offset  
batch_size (int) – Number of features to fetch per request.

