from descarteslabs.client.services import Storage

s = Storage()
s.copy_from_bucket(src_bucket_name="karla-skylark", src="honduras.geojson", dest="karla-descartes")

