import heapq

def dijkstra(graph, start):
    # Initialiser la distance de départ à 0 et la file de priorité
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Vérifier si la distance actuelle est plus grande que la distance enregistrée
        if current_distance > distances[current_node]:
            continue

        # Parcourir les voisins du nœud actuel
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Mettre à jour la distance si un chemin plus court est trouvé
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Exemple d'utilisation
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
shortest_distances = dijkstra(graph, start_node)

print(f"Distances les plus courtes depuis le nœud {start_node}: {shortest_distances}")