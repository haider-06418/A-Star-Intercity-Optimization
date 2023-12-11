# creating graph

import math
import json


# function to load json file into a dictionary
def load_json(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
    return data


# Haversine function to calculate distance
def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # radius of Earth in kilometers
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    # distance = math.sqrt((lat2 - lat1)**2 + (lon2 - lon1)**2) # Euclidean distance
    return distance


def create_graph(city_data_file):
    # city name and coordinates for calculating distance
    city_coordinates = load_json(city_data_file)

    # initializing the graph
    graph = {city: [] for city in city_coordinates}

    # populating the graph with distances
    for city1 in city_coordinates:
        for city2 in city_coordinates:
            if city1 != city2:
                dist = haversine(*city_coordinates[city1], *city_coordinates[city2])
                # if dist <= 250:
                if dist <= 150:
                    graph[city1].append({'city': city2, 'distance': dist})

    # saving the graph to a json file
    with open('graphs/graph.json', 'w') as file:
        json.dump(graph, file, indent=4)
    print("Graph saved to 'graph.json'")


    # for node in graph:    
    #     # # Check if the value is an empty list
    #     # if not graph[node]:
    #     #     print(f"No values for node: {node}")


create_graph('city_data.json')