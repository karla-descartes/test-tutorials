============
Version Requirments 
============
**Beta** users are largely able to use whichever version of Python they wish, though the latest release of Python 2 or 3 are recommended (Python 2.7.14 and Python 3.6.5 respectively). 

**Alpha** access only supports Python 2 at this time, though we are working to support Python 3. Because Alpha access includes the ability to scale your processing on our virtual machines, having equivalent versions on your local machine is important. For this reason, having the latest version of Python 2, NumPy, and other standard python libraries is required to use the Alpha scalable compute service. These include: Python 2.7.14, NumPy 1.14, and SciPy 1.0.  

============
Virtual Environments
============

To manage the installation of the Descartes Labs platform and supporting Python libraries, we suggest using ``conda`` or ``virtualenv`` to create separate environments. A virtual environment makes it possible to set up and maintain an isolated set of Python and module installations on the same computer. When activated, all modules installed are separate from the main Python installation, and added to an environment specific configuration. The problem being addressed is one of dependencies and version compatibility, as well as permissions. This allows for a lot less package management headaches. Whether you intend to use ``conda``, ``virtualenv``, or no environment manager, installing the Descartes Labs platform requires `PyPi <https://pip.pypa.io/en/stable/installing/>`_.


***************
conda
***************
Conda is an open source environment management system that runs on most common operating systems. It can be installed as a stand alone package manager, but is also part of the open source Anaconda project, which offers Anaconda Navigator and Cloud, a graphical interface for module installations and a hosted cloud account for storing environments and code. The recommended ways to install conda are either through Anaconda or Miniconda, where Miniconda is a much smaller piece of software with the bare essentials. A third option is a separate installation through Python Package Index (PyPI).


`miniconda <https://conda.io/miniconda.html>`_  

`Anaconda <https://www.anaconda.com/download/#windows>`_  

`PyPi <https://pypi.org/project/conda/>`_  

If you've correctly installed ``conda``, you should be able to run ``which conda`` and have it return you default location. If this command is successful, you can create a virtual environment to isolate installations for a new project. Installing packages is straightforward, as it resembles the syntax of ``pip``, and is compatible with ``pip``. If ``conda`` does not host a module, or you want to install a package currently under development, you can compile it using ``pip`` or from source. Here is an example of the steps commonly used to set up a Descartes Labs Beta development environment followed by an explanation.

.. code-block::

 $ conda create -n dl-env -c conda-forge python=3 
 $ source activate dl-env
 (dl-env)$ which python
 (dl-env)$ conda install scipy scikit-image ipython jupyterlab jupyter gdal scikit-learn pandas matplotlib
 (dl-env)$ pip install -U pip
 (dl-env)$ pip install descarteslabs
 $ source deactivate

To create a new ``conda`` environment, ``-n``  sets the name of the environment. The ``-c`` denotes a channel, or repository from which to pull compatible package denpendencies. ``conda-forge`` is a widely used and reliable channel for installations. Lastly, you are able to set the Python version of the environment. 

To add additional packages to your clean environment, you activate it from anywhere as seen on the second line above. You can confirm you are referencing the isolated environment by running ``which python``. It should not be pointing at your main Python installation, but rather the conda environment of interest.  Once activated, you can begin installing packages via ``conda`` and ``pip``. It is good idea to update ``pip`` before using it to install modules in the clean environment, as done on line 5. After you've finished installing packages, you can deactivate the environment. You are ready to use this environment for your first Descartes Labs project.     
 

***************
virtualenv 
***************
``virtualenv`` is an alternative tool to create isolated Python environments. Unlike ``conda``, it is not language agnostic, and only works with Python libraries. It works similarly in that, when you install one module, such as Jupyter, all of the required modules will also be downloaded and installed with compatible versions. Installation of the ``virtualenv`` package is easy when using ``pip`` as demonstrated below. It is always a good idea to begin by updating ``pip``, done on the first line. 

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

