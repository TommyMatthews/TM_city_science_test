#Basic version of app for running Dijkstra's algorithm 

import sys
import numpy as np
from pandas import read_csv as read_csv
file = sys.argv[1]
source = sys.argv[2]
target = sys.argv[3]

# Check to see that a distinct source and target have been entered
if source == target:
    print('Source and Target are the same vertex')
    quit() 

#reading in data and converting it to a numpy array
raw_data = read_csv(file, sep =" ", header = None )
data_array = raw_data.to_numpy()

#Check to see if source is connected to rest of graph
#find the indicies of all edges leaving the source
array_indicies_of_source_neighbours = np.where(data_array[:,0] == source)
#check to see if source is disconnected from network, if so quit
if array_indicies_of_source_neighbours[0].size == 0:
    print('Source is not connected to rest of network')
    quit()

#creating an array and then a list of all verticies
vertex_array = np.union1d(data_array[:,0],data_array[:,1])
vertex_list = vertex_array.tolist()
#creating a duplicate list to lable unvisited verticies
unvisited_verticies = vertex_array.tolist()

#Initialising a dictionaries of distances to verticies
#Initially all non source verticies have distance infinity, source vertex distance is zero
infinity_array = np.ones(len(vertex_list))*np.inf
infinity_list = infinity_array.tolist()

distance_dict= dict(zip(vertex_list,infinity_list))
unvisited_distance_dict = dict(zip(unvisited_verticies,infinity_list))
distance_dict[source] = 0
unvisited_distance_dict[source] = 0

#Initialising a dictionary of the previous vertex on the shortest path on each vertex
#Initially all are labelled with empty
number_of_verticies = len(vertex_list)
previous_initialisation_list = ['empty']*len(vertex_list)
previous_dict = dict(zip(vertex_list, previous_initialisation_list))

#Loop to run through Djisktra's algorithm
while len(unvisited_verticies) != 0: #Whilst there are still verticies to visit

    #identify the vertex with the shortest distance to the source:
    #in the case of multiple answers, this returns the first found, which works fine within this algorithm
    next_closest_vertex = min(unvisited_distance_dict, key=unvisited_distance_dict.get) 
    #remove this vertex from this list and distance dictionary of unvisited verticies
    unvisited_verticies.remove(next_closest_vertex)
    del unvisited_distance_dict[next_closest_vertex]
    #find the indicies of all edges leaving the next closest vertex
    array_indicies_of_neighbours = np.where(data_array[:,0] == next_closest_vertex)
    #extract the neighbours of the next closest vertex
    neighbours_and_distances_array = data_array[array_indicies_of_neighbours,1:3][0]
    
    
    #loop over each neighbour
    for i in range(len(neighbours_and_distances_array)):
        #calculate the total distance from the source to that neighbour, through the "next closest vertex"
        edge_length_to_neighbour = neighbours_and_distances_array[i,1]
        trial_distance = distance_dict[next_closest_vertex] + edge_length_to_neighbour
        
        #check if this is shorter than any previous distance label assigned to this vertex
        neighbour = neighbours_and_distances_array[i,0]
        if trial_distance < distance_dict[neighbour]:
            #update the dictionaries of distances to include this new, shorter distance
            distance_dict[neighbour] = trial_distance
            unvisited_distance_dict[neighbour] = trial_distance
            #label the "next closest vertex" as the new previous node to this neighbour
            previous_dict[neighbour] = next_closest_vertex
    
    
    #Check to see if target has been reached, can break out of the loop if so
    if next_closest_vertex == target:
        target_reached = True 
        break
    
    #Check to see if no further nodes are reachable
    #For this to be the case, all nodes left unvisited will have a distance value of infinity
    #return a list of the distance to the unvisited verticies
    test_list = [0]*len(unvisited_verticies)
    for i, unvisited_vertex  in enumerate(unvisited_verticies):
        unvisited_vertex_distance = distance_dict[unvisited_vertex]
        test_list[i] = unvisited_vertex_distance
        
    #Check to see if all unvisited nodes have distance infinity
    test_condition = all(distance == np.inf for distance in test_list)
    
    #If test condition true the target and source are not connected
    if test_condition == True:
        print('Target not connected to source')
        break

#check that target has been reached
if test_condition != True:
    #Start constructing the path back to the source at the target vertex
    shortest_path = [target]
    tracer = target
    #Loop until the source is reached:
    while previous_dict[tracer] != 'empty':
        #Add the previous vertex in the path to the shortest path list
        shortest_path.append(previous_dict[tracer])
        #Move the tracer back along the path
        tracer = previous_dict[tracer]
    #Put the path into the correct order
    shortest_path.reverse() 
    #Print out the path
    print('The shortest path from ', source, ' to ' , target, ' is:')
    for path_vertex in shortest_path:
        print(path_vertex)    
