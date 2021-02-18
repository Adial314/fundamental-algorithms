# -------------------- REQUIREMENTS -------------------- #

%reset -f
import json
import numpy as np
from time import sleep

from pathlib import Path

from dijkstras.custom.logger import logger


def sort_graph(graph):
    nodes = list()
    distances = list()
    for node, details in graph.items():
        nodes.append(node)
        distances.append(details["distance"])

    _, nodes = zip(*sorted(zip(distances, nodes)))

    prioritized_graph = dict()
    for node in nodes:
        prioritized_graph[node] = graph[node]

    return prioritized_graph



# ------------------------- #

graph_name = "dijkstras/graphs/cphile.json"

with open(graph_name) as f:
    graph = json.load(f)

for node in graph:
    if "distance" in list(graph[node].keys()):
        continue
    else:
        graph[node]["distance"] = np.inf
        graph[node]["via"] = None
        graph[node]["visited"] = False

source = "S"
sink = "E"

shortest_path = list()
queue = dict()
unvisited = list(graph.keys())

node = source
iteration = 0
while node != sink:
    temp_distance = graph[node]["distance"]
    temp_via = graph[node]["via"]
    logger.info(f"iteration {iteration} node {node} with distance {temp_distance} via {temp_via}")
    
    for connection, cost in graph[node]["connections"].items():

        if graph[connection]["visited"]:
            continue
        else:
            logger.info(f"\tevaluating connection {connection} with cost {cost}")
            
            # Evaluate the distance
            current_distance = graph[connection]["distance"]
            connection_distance = graph[node]["distance"] + cost
            logger.info(f"\t\tcurrent distance is {current_distance}")
            logger.info(f"\t\tconnection distance is {connection_distance}")

            # Set new distance
            if connection_distance <= current_distance:
                logger.info(f"\t\tsetting {connection} to {connection_distance} via {node}")
                graph[connection]["distance"] = connection_distance
                graph[connection]["via"] = node
            
        # Sort graph by shortest path
        graph = sort_graph(graph)
        
    # Current node has been visited
    logger.info(f"\tsetting {node} to visited")
    graph[node]["visited"] = True

    # Next priority becomes the new node
    for node in graph:
        if graph[node]["visited"]:
            continue
        else:
            break
            
#     sleep(0.5)
    print(f" ITER {iteration} NODE {node}")
    print("--------------------")
    for element in graph:
        if element == node:
            print(">" + element + str(graph[element]))
        else:
            print(element + str(graph[element]))
    print("--------------------\n")
    
    logger.info(f"next node is {node}")
    iteration += 1
    
