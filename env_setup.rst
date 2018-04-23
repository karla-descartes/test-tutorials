============
Version Requirments 
============
Specific Python and Python module versions are required Depending on if you are an Alpha or Beta user. Beta users are largely able to use whichever version of Python they wish, though the latest release of Python 2 or 3 are recommended (Python 2.7.14 and Python 3.6.5 respectively). Alpha access only supports Python 2 at this time, though we are working to support Python 3. Because Alpha access includes the ability to scale your processing on our virtual machines, having equivalent versions on your local machine is important. For this reason, having the latest version of Python 2, NumPy 

============
Virtual Environments
============

To manage the installation of the Descartes Labs platform and supporting Python libraries, we suggest using ``conda `` or ``virtualenv``. Both modules facilitate virtual environments. A virtual environment makes it possible to set up and maintain completely separate Python installations on the same computer. When activated, all modules installed are separate from the main Python installation (in other words, the modules installed inside a virtual environment will not be added to the main site-packages folder). This allows for a lot less package management headaches.

install pip https://pip.pypa.io/en/stable/installing/

minimum versions for python and numpy 

***************
conda
***************
.. one time installation 
The best ways to install conda are through installing either Anaconda or Miniconda. A third option is a separate installation through Python Package Index (PyPI).



Apart from using Anaconda Navigator and Cloud for package management, you can use conda, a binary package manager, as a command-line tool to manage your package installations. Conda quickly installs, runs and updates packages and their dependencies. Conda easily creates, saves, loads and switches between environments on your local computer. 

Installing packages with conda is straightforward, as it resembles the syntax of pip. However, it is good to know that conda cannot install packages directly from a git server. This means that the latest version of many packages under development cannot be downloaded with conda. Also, conda doesn't cover all the packages available on PyPI as pip itself, which is why you always have access to pip when creating a new environment with Anaconda Navigator (more on pip as we proceed further).

You can verify if conda is installed by typing the following command in a terminal: >> conda -version
If installed, conda will displays the number of the version that you have installed. Installing the package of your choice can be done with the following command in a terminal:
>> conda install <package-name>
Updating an already installed package to its latest available version can be done as follows:
>> conda update <package-name>
You can also install a particular version of a package by pointing out the version number:
>> conda install <package-name>=1.2.0
You can update all the available packages simply by using the --all argument:
>> conda update --all Uninstall packages can be done too:
>> conda remove <package-name>
Extensive conda documentation is available through https:/​/​conda.​io/​docs/​index.​html.



***************
virtualenv 
***************
.. one time installation 
pip install virtualenv


.. creating a new environment 
virtualenv --python=python3.6 new-environment
cd new-environment 
.. path to environment bin folder 
source bin/activate
pip install jupyterlab
pip install descarteslabs
pip install matplotlib
python -m ipykernel install --user --name=hello-world


.. can be run anywhere
deactivate



Installing virtualenv
Installation of the virtualenv package is easy when using pip: the package is called from PyPI
(the Python Package Index at pypi.org). pip install virtualenv
This command will add virtualenv and its supporting modules. Make sure that the main Python installation has been added to the "PATH" Windows environment variables so that virtualenv can be called from the command line.
Running virtualenv
To create the virtual environment, open a command line and enter the following command structure, virtualenv {environment name}. In this case, the name of the environment is cartoenv:

 Inside the folder where virtualenv is created, a series of folders are generated with the code files necessary to support Python. There is also a Lib folder, which contains the site- packages folder that will hold all of the modules installed inside this virtual version of Python.
Activating the virtual environment
To start using the new virtual environment from the command line, pass the following argument inside the folder that holds the virtual environment. This will run the activate batch file, and will start the virtual environment:
C:\PythonGeospatial3>cartoenv\Scripts\activate
Once the virtual environment is activated, the name of the environment will appear before the folder name, indicating that the commands are being run inside the environment and any changes that are performed (such as installing modules) will not affect the main Python installation:
(cartoenv) C:\PythonGeospatial3>
In a Linux environment, the command source {environment}/bin/activate is used instead.
When programming in Linux, the commands in the terminal would look like this:
silas@ubuntu16:~$ mkdir carto silas@ubuntu16:~$ cd carto/ silas@ubuntu16:~/carto$ virtualenv cartoenv
  
 New python executable in /home/silas/carto/cartoenv/bin/python Installing setuptools, pip, wheel...done. silas@ubuntu16:~/carto$ source cartoenv/bin/activate (cartoenv) silas@ubuntu16:~/carto$
In either OS, to deactivate the virtual environment, pass the deactivate command. This will end the virtual session:
   C:\PythonGeospatial3>cartoenv\Scripts\activate
(cartoenv) C:\PythonGeospatial3>deactivate C:\PythonGeospatial3>
Installing modules in the virtualenv
Because each virtual environment is separate from the main Python installation, each environment must have the required modules installed. While this can seem like a pain,
pip makes it quite easy. After setting up the first virtual environment, a pip command called freeze allows you to generate a file called requirements.txt. This file can be copied into a new virtual environment, and using pip install, all of the listed modules will be added from PyPI.
To generate a requirements.txt file in the current folder, use this command: (cartoenv) C:\Packt\Chapters>pip freeze > requirements.txt
After the file has been copied into a new virtual environment folder, activate the environment and pass the following command to read from the file:
   (newenv) C:\Packt\Chapters>pip install -r requirements.txt
Modules to use
For this virtual environment, we will install the two modules CARTOframes and jupyter. The second module will allow us to run Jupyter Notebooks, which are specialized browser- based coding environments.
Activate the virtual environment, and install the modules within the virtual environment with the following commands:
   (cartoenv) C:\Packt\Chapters>pip install cartoframes
   (cartoenv) C:\Packt\Chapters>pip install jupyter
All of the required modules will also be downloaded and installed along with the two that we are installing directly. Using pip and virtualenv makes package installation and management simple and quick.


***************
Jupyter Notebook
***************
