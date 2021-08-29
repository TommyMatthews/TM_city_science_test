#This is a script to run the app over all possible vertex pairings and return the longest time taken to run the app.

import numpy as np
import sys
import timeit
from pandas import read_csv as read_csv

#read in the graph data file
file = sys.argv[1]


#reading in data and converting it to a numpy array
raw_data = read_csv(file, sep =" ", header = None )
data_array = raw_data.to_numpy()
#creating an array and then a list of all verticies (and a duplicate)
vertex_array = np.union1d(data_array[:,0],data_array[:,1])
vertex_list1 = vertex_array.tolist()
vertex_list2 = vertex_array.tolist()

#create a 2d array to fill with the times recorded
times_array = np.zeros((len(vertex_list1),len(vertex_list1)))

#loop over all possible sources
for i, source in enumerate(vertex_list1):
    #remove the source from the list of potential targets - done because I can't stop the source = target
    #exit command from also exiting this script
    vertex_list2.remove(source)
    #loop over all targets
    for j, target in enumerate(vertex_list2):
        #create arguments for app
        sys.argv = ["Shortest_route_app.py", file, source, target]
        #run app and time it
        start = timeit.default_timer()
        script_descriptor = open("App_for_speed_test.py")
        script = script_descriptor.read()
        exec(script)
        end = timeit.default_timer()
        #store time in array
        times_array[i,j] = end-start

#return the maximum time
print('Maximum time is: ', times_array.max())






