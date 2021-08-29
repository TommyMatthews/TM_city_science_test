# TM_city_science_test

Hello! Please find my submission for the City Science technical test in this folder.

**Choice of algorithm:**

I have used Dijsktra's algorithm to find the shortest path between verticies. It is worth noting that in the case of a non-unique shortest path it will only find one of them, however due to the complexity of the network this seems unlikely anyway.

Link to algorithm:
https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm


**Building the project:**

To run this app you need Python installed along with the numpy and pandas packages.
For the app to work the .dat file containing the graph of interest should be in the same folder.


**Using the app:**

To run the app use the following command:

python Shortest_route_app.py graph_data.dat source_vertex target_vertex

where graph_data.dat is the data file for the graph of interest and source_vertex and target_vertex are the start and end of your route respectively.


**Functionality tests:**

Test_1 contains a 5 vertex graph where the source and end vertex are connected. There is a trivial shortest route from A to E which the app finds. The graph is:

A B 1
A C 3
A D 3
B C 1
B E 3
C E 1
D E 3

Test_2 contains the same graph but with all links to vertex E are removed. The app successfully reports that is no link if you try to find a route to E. If you try to find a route from E it will tell you that the source is not connected to the graph.


**Speed tests:**

Single_route_speed_test.py is used in the same way as the basic app and additionally returns the time taken to find the specific route. On my (fairly old) computer this finds my random sample tests running at 0.75s or under.

Whole_network_speed_test.py runs the app from inside a shell over all possible vertex pairings (excluding source = target pairings), records the time for each pairing, and then returns the maximum time taken. This can be run using:

pytyon Whole_network_speed_test.py graph_data.dat

This seems to return times about an order of magnitude shorter than running the app on its own, I'm not sure why this is. Usefully, this does tell us that the algorithm successfully works for all possible source target parings. Note that Whole_network_speed_test calls a version of the app with all print commands suppressed. This is App_for_speed_test.py . 
