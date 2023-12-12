import heapq

def is_valid(x, y, rows, cols):
    return 0 <= x < rows and 0 <= y < cols

def a_star(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    
    # Déplacements possibles (haut, bas, gauche, droite, diagonales)
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]
    
    # Nœud de départ
    start_node = (0, start, 0, abs(goal[0] - start[0]) + abs(goal[1] - start[1]), None)
    
    # File de priorité pour maintenir les nœuds à explorer, triés par coût total (f)
    open_set = [start_node]
    
    # Ensemble pour suivre les nœuds déjà explorés
    closed_set = set()
    
    # Dictionnaire pour stocker les informations du nœud parent pour chaque nœud
    parent = {}
    
    while open_set:
        _, current, g, _, _ = heapq.heappop(open_set)
        
        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parent.get(current)
            return path[::-1]
        
        closed_set.add(current)
        
        for i in range(8):
            new_x, new_y = current[0] + dx[i], current[1] + dy[i]
            
            if is_valid(new_x, new_y, rows, cols) and grid[new_x][new_y] == 0:
                neighbor = (new_x, new_y)
                new_g = g + 1
                new_h = abs(goal[0] - new_x) + abs(goal[1] - new_y)
                new_f = new_g + new_h
                
                if neighbor not in closed_set:
                    heapq.heappush(open_set, (new_f, neighbor, new_g, new_h, current))
                    parent[neighbor] = current
    
    return []

# Exemple d'utilisation
grid = [
    [0, 0, 0, 0, 1, 0],
    [1, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0]
]

start = (0, 0)
goal = (4, 5)

path = a_star(grid, start, goal)

if path:
    print("Chemin trouvé:", path)
else:
    print("Aucun chemin trouvé.")