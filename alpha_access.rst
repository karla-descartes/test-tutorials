============
Version Requirments 
============
**Alpha** access only supports Python 2 at this time, though we are working to support Python 3. Because Alpha access includes the ability to scale your processing on our virtual machines, having equivalent pacakge versions on your local machine is important. For this reason, the latest version of Python 2, NumPy, and other standard python libraries are required to use the Alpha scalable compute service. These include: Python 2.7.14, NumPy 1.14, and SciPy 1.0.  

The latest nightly installation can be found here. Authentication should be a simple one-time process of running descarteslabs auth login, which will prompt you to add a API token to your computer’s configuration.

============
Installing Alpha Client via the nightly build 
============

1. Ensure clean environment
``justin@justin:~$ virtualenv test  
New python executable in /home/justin/test/bin/python
Installing setuptools, pip, wheel...done.
justin@justin:~$ source test/bin/activate``

2. Install the nightly release
``(test) justin@justin:~$ pip install "https://storage.googleapis.com/dl-pypi-prod/descarteslabs-alpha-2018.04.08.tar.gz?Expires=1531977001&GoogleAccessId=documentation%40dl-platform.iam.gserviceaccount.com&Signature=tiqrWy2hziJLghVVx0QIuFDIwc9wPOc5bk%2Bq%2F4%2FKAvzo1j43CDDHR8bpUTxsf8e9t4sjpEPny0XKb5S%2FZKvpNgR4hBr5yXZB0GW9aJqc5c4TMS3DJnWezZai4PjRioehkRzLIDK53xTSqG5SITBRAm9%2BZeJF3lQQZs%2FxGD97AzbNuwL7nM%2FcQ84lZiLljZ5dSpYgUD82QYIJTpOe2i15nQpZh97qRuTUKwgs1BZ5c2XH0AG6%2BVH9bImP8f8Mbbjvauompz9iDcJnssThmpNHF43iEfrOCJxqrg6RR2WEwI6Tt4P4E17iZsluOSMRySAuX6xGLVnoiknOzmqTC0WVaw%3D%3D"
...
Successfully installed asn1crypto-0.24.0 cachetools-2.0.1 certifi-2018.1.18 cffi-1.11.5 chardet-3.0.4 cloudpickle-0.4.0 cryptography-2.1.4 descarteslabs-2018.4.8 enum34-1.1.6 idna-2.6 ipaddress-1.0.19 numpy-1.13.3 pyOpenSSL-17.5.0 pycparser-2.18 requests-2.18.4 six-1.11.0 urllib3-1.22```

3. Test the installation:
``(test) justin@justin:~$ python
Python 2.7.12 (default, Nov 19 2016, 06:48:10) 
[GCC 5.4.0 20160609] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> from descarteslabs.client.services.tasks import AsyncTasks
>>> print(AsyncTasks)
<class 'descarteslabs.client.services.tasks.tasks.AsyncTasks'>``


***************
virtualenv 
***************
``virtualenv`` is a tool to create isolated Python environments. Unlike ``conda``, it is not language agnostic, and only works with Python libraries. It works similarly in that, when you install one module, such as Jupyter, all of the required modules will also be downloaded and installed with compatible versions. Installation of the ``virtualenv`` package is easy when using ``pip`` as demonstrated below. It is always a good idea to begin by updating ``pip``, done on the first line. 

.. code-block::

   $ pip install -U pip
   $ pip install virtualenv

To confirm you have installed the ``virtualenv`` system, run ``virtualenv --version``. This should return a version greater than 15.0. Once installed, you can create and activate a new isolated environment. 

.. code-block::

   $ virtualenv --python=python3.6 dl-env
   $ cd dl-env
   $ source bin/activate

Once the virtual environment is activated, the name of the environment will appear before the folder name, indicating that the commands are being run inside the environment and any changes that are performed (such as installing modules) will not affect the main Python installation, but rather install only into the new environment's site-packages configuration. 

.. code-block:: 

   (dl-env)$ pip install jupyterlab
   (dl-env)$ pip install descarteslabs
   (dl-env)$ pip install matplotlib
   (dl-env)$ python -m ipykernel install --user --name=dl-env
   $ deactivate

The second to last line of code will export the virtual environment into JupyterLab, so that you can access and use it in a Jupyter Notebook, an interactive development environment that works well with the Descartes Labs platform. The last line deactivates the environment.

