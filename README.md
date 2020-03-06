# New-York-Subway-Planner
Project to optimize the subway routes using real-time MTA feeds

## Project Description

The purpose of this application is to help New York City Subway users make informed decisions that encourage time-efficiency and reduce hassle. By analyzing real-time data provided by the Metropolitan Transportation Authority (MTA) of New York, the app will be able to generate relevant and up-to-date results. Users will input the origin and destination of their travel route, as well as a preference for reducing travel-time, crowdedness, or transfers.
## Project Design

At the front-end, the Real-time Subway Route Planner application first requires the user to input the desired origin and destination of their trip via drop-down menus, as well as their chosen specification (i.e. time-efficiency, minimize crowdedness, minimize transfers). The application will also display a graph of the NYC subway system with all the stops clearly labeled. The interactive map is visualized using the Folium Python library which acts as an interface between Python and JavaScript. The subway stops are saved in a CSV file with corresponding longitude and latitude coordinates.

Information about train delays, service cancellation, and accidents will be collected real time from MTA website through API and processed as delay edge weights, and average station crowd density (from the entries and exits) will be collected and processed as crowdedness edge weights; the subway map will be stored as a graph (i.e. stations as vertices and train paths as edges) and weights will be added to the edges according to the MTA information. Since the data is collected real-time, the graphs G = (V, E, W ) are generated dynamically. By implementing Dijkstra’s algorithm, the program will then return the best route to the destination according to the user’s preference.

Therefore once the user presses ”submit”, their preferences will then be processed. Once the computation is complete, the front-end receives the shortest path P of the subway graph and P is displayed on the original subway map as a sequence of highlighted stations. The line and stations are also displayed as text above the map, for the user’s convenience.



### Language and programming environment.

The majority of the back-end is developed in Python using the Networkx library. For the front-end, we used Folium and HTML to develop a web interface.
End with an example of getting some data out of the system or using it for a little demo



## Authors

* **Zhenru Zhou** 
* **Mayank** 
* **Francesca Falzon** 


