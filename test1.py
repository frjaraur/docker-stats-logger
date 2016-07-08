#!/usr/bin/env python3
import io
from docker import Client
cli = Client(base_url='unix://var/run/docker.sock')
containers=cli.containers()

for container in containers:
    #print (container)
    container_name=str(container['Names'])[3:-2]
    #container_name=container_name[3:-2]
    print ("------------------------")
    print (container_name)
    print ("------------------------")
    for keys in container.keys():
        print (keys + " ---> " + str(container[keys]))

    container_stats = cli.stats(container,False,False)
    print (container_stats)


    #f = io.StringIO(container_stats)
    #contents = f.getvalue()
    #f.close
    #for stats in container_stats:
    #    print (stats)
#images = cli.images()
#print(images[0])
