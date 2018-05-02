============
Development Environment
============
Managing Python development environments can be tricky, especially if you are new to the language or less familiar with computer science concepts. If you are stuck and in need of some guidance, this guide walks through using ``conda``, a virtual environment manager, to get you access to the Descartes Labs programmatic APIs while accessing other compatible opensource Python modules. This is far from the only development environment that works, and in fact, is not preferred by all our users. Other package management systems allow for more control over module versions, which can be necessary to run our most advance features. This guide merely details one popular option for working within your environment to avoid headaches and suggests best-practice project setup.

***************
Installation and Authentication of the Descartes Labs platform
***************
The basic Descartes Labs Platform installation instructions can be found `here <https://docs.descarteslabs.com/docs/installation.html>`_.  `Authentication <https://docs.descarteslabs.com/docs/authentication.html>`_  should be a simple one-time process of running ``descarteslabs auth login``, which will prompt you to add a API token to your computer’s configuration. Installing the Descartes Labs platform requires `pip <https://pip.pypa.io/en/stable/installing/>`_.


***************
conda
***************
``conda`` is an environment management system, a package manager, and a repository of pre-compiled packages. When you install one module using ``conda``, such as JupyterLab, all of the required modules will also be downloaded and installed with compatible versions.  While there are multiple ways to install ``conda``, we recommend `miniconda <https://conda.io/miniconda.html>`_,  the most lightweight and bare-minimum approach to using ``conda``. 

Installing packages is straightforward, as it resembles the syntax of ``pip``, and is compatible with ``pip``. If ``conda`` does not host a module, or you want to install a package currently under development (such as ours), you can install it using ``pip`` or from source. Here is an example of using ``conda`` to install the Descartes Labs Beta  library along with the popular plotting package, ``matplotlib``.

.. code-block::

 $ conda create -n dl-env -c conda-forge python=3 
 $ source activate dl-env
 (dl-env)$ pip install descarteslabs
 (dl-env)$ conda install matplotlib
 $ source deactivate


To create a new ``conda`` environment, ``-n``  sets the name of the environment. The ``-c`` denotes a channel, or repository from which to pull compatible package denpendencies. ``conda-forge`` is a widely used and reliable channel for installations. To add additional packages to your environment, you activate it from anywhere as seen on the second line above. Once activated, you can begin installing packages via ``conda`` and ``pip``. For more information on using conda, check out their `documentaion <https://conda.io/docs/>`_.

***************
Best Practices 
***************

The versions you need installed for the same modules and even Python itself may vary as you move from project to project. For example, the supporting pacakages and their associated releases that run TensorFlow may not be the same as those that run GDAL. Each project, with its distinct set of modules, are unique snowflakes. For this reason, we recommend following the guidelines when setting up new projects: 

- make a directory for every project

- make a new virtual environment in that directory

- make a git repo in that directory

- keep all data and code in that directory, under version control (as well as a requirements.txt, or Pipfile) 

Using ``conda``, your new project workflow could be: 

.. code-block::

 $ mkdir new_project
 $ cd new_project
 $ conda create --prefix env python=3  # creates a new environment directory `env` in the current directory
 $ conda activate ./env
 (/Users/<you>/../new_project/env) $ conda install --channel conda-forge jupyterlab matplotlib
 (/Users/<you>/../new_project/env) $ pip install descarteslabs
 (/Users/<you>/../new_project/env) $ conda deactivate
 $ git init
 $ echo "env/*" > .gitignore
 $ git add .
 $ git commit -m "Initial commit"

The popular webcomic `xkcd <https://xkcd.com/>`_ captures the difficulty of maintaining Python development environments below.

 .. image:: https://imgs.xkcd.com/comics/python_environment.png

