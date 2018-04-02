***************
DLRun
***************

DL Run provides scalable compute capabilities to users of the Descartes Labs Platform while handling the complexities of scaling these computations for the user. It works by serializing python code and executing that code on nodes hosted by Descartes Labs in their cloud infrastructure. These nodes are able to access Descartes Labs imagery at extremely high rates of throughput which paired with horizontal scaling allow execution of computations over nearly any temporospatial scale.

**NOTE: DLRun presently only runs with python 2.7**


There is a one-time initialization to your user-specific resources that you need to run before you can submit jobs. The following code will initialize these resources for you and allow you to run DLRun code. 
::

  from descarteslabs.ext.tasks import AsyncTasks
  at = AsyncTasks()
  at.create_namespace()


**Basic Example**
.. code-block:: python

  from descarteslabs.ext.tasks import AsyncTasks, as_completed

  def hello(i):
      import geopandas 
      print(geopandas) 
      return "hello {}".format(i) 

  at = AsyncTasks()
  async_func = at.create_function(
  hello,
  name='hello',
  image="us.gcr.io/dl-ci-cd/images/tasks/public/geospatial/geospatial-public:latest",
  )

  task = async_func(5)

  print task.result
  print task.log


This example creates a function called ``hello`` which prints information about the geopandas package and prints ``hello <passed in variable>``. This function is turned into a scalable task using the ``create_function`` method which specifies the function to be scaled, gives it a name, and specifies the image to be used and stores a reference to the task in the ‘task’ variable. (This image contains a number of dependencies common in geospatial analysis. There are not presently methods exposed to generate your own image or to install additional dependencies - if you run into a problem with dependencies not being aval please email support@descarteslabs.com to have it addressed.) The task is then called and 5 is passed in. The code execution then blocks at this step and waits for the result to be returned from the scalable task. This will take a few moments as when task execution starts, instances need to be created before the task is able to be executed. Instance management is handled in the background with instances being created and destroyed as needed to match the compute resources to the need of the job.

This simple example illustrated the basics of DLRun but not the power as it only runs one task. 

**Multiple Task Example**
.. code-block:: python

  task = async_func(5)

  print task.result
  print task.log

  with the following lines

  tasks = async_func.map(range(20))

  for task in as_completed(tasks):
      try:
          print(task.result)
     except:
          print(task.exception)
          print(task.log)

We will have an example that better illustrates the power of DLRun. This example uses the map method. This works similar to a traditional map concept where a function is applied over all of the passed values, in this case a list of 20 integers. Twenty tasks are queued up to be executed. Then for loop uses the as_completed method to collect returned values from completed tasks as they become available. We are also using a try except to catch exceptions and display the log of the task when an exception occurs. 

If you are returning multiple values they can be accessed by using ``task.result[0]`` ``task.result[1]``.