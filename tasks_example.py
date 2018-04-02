
from descarteslabs.client.services.tasks import AsyncTasks, as_completed
from descarteslabs.client.services.raster import raster

# Create the task to add a really compute heavy function to 
# Tasks are good at compute heavy processes, not great a memory dependent processing, such as training a model
task = AsyncTasks()


def mask_clouds(x, option=None):
    return "Hello World {} {}".format(x, option)

async_func = task.create_function(mask_clouds)


# async_func = task.create_function(mask_clouds,
# 	name='hello-world',
#     image="us.gcr.io/dl-ci-cd/images/tasks/base/task-base"
#           "@sha256:2518990c087c0122d6150ddb278f331090ab4f9a140e4ec6fe0a8b2d4756e038"
# )

# task1 = async_func(1)
# task2 = async_func(2, option='hi')
# print task1.result
# print task2.result

# tasks = async_func.map(xrange(100))
# for task in as_completed(tasks):
#     print task.result