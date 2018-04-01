============
Places 
============
The Places API provides a convenient method for delivering political boundaries to your Descartes Labs development environment. We use the `Who's on Frist API <https://whosonfirst.org/>`_ as our places provider. There are two ways to work with Places geometries outlined below. 




***************
Accessing the Geometry  
***************
**Find**
Returns a list of all matching places. Each element in the list represents a distinct political boundary, and has the attribute ``slug``. A ``slug`` identifier is a valid value to pass to other Descartes Labs APIs, including Metadata Search as the key ``shape``. This ireturn does not include the geometry, but can be passed to the Shape method to access coordinate information. 

This example searches for New Mexico, grabs the first element in the return, and prints its identifier. 

.. code-block:: python

 import descarteslabs as dl
 >>> new_mexico = dl.places.find('north-america_united-states_new-mexico')
 >>> new_mexico_shape = new_mexico[0]['slug']
 north-america_united-states_new-mexico

**Shape**
Returns a single matching GeoJSON with defined coordinates given a ``slug`` identifier. The output can be passed to Metadata Search as the key ``geom``. 

Here is an example accessing the GeoJSON for New Mexico's boundary. 

.. code-block:: python

 import descarteslabs as dl
 from pprint import pprint
 >>> new_mexico_geojson = dl.places.shape('north-america_united-states_new-mexico')
 >>> pprint(new_mexico_geojson)
 {
  u'bbox': [-109.050039, 31.332244, -103.002199, 37.000141],
  u'geometry': {
    u'coordinates': [
      [
        [-109.046156, 34.579291],
        [-109.045223, 36.999084],
        [-106.877293, 37.000141],
        [-106.869798, 36.992424],
        ...
      ]
    ],
    u'type': u'Polygon'
  },
  u'id': 85688493,
  u'properties': {
    u'name': u'New Mexico',
    u'parent_id': 85633793,
    u'path': u'continent:north-america_country:united-states_region:new-mexico',
    u'placetype': u'region',
    u'slug': u'north-america_united-states_new-mexico'
  },
  u'type': u'Feature'
}

***************
Syntax
***************
 The Find and Shape methods have only one required string parameter. The string needs to be in lower case with a "-" separating administrative levels, and "_" in place of spaces. For example, a valid search for Santa Fe, New Mexico is ``'new-mexico_santa-fe``, where the ``slug`` identifier is ``'north-america_united-states_new-mexico_northwest_santa-fe``. 