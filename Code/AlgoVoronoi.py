# Algo diagramme de Voronoï

import matplotlib.pyplot as plt
import numpy as np

def voronoi(points, xlim, ylim):
    x_min, x_max = xlim
    y_min, y_max = ylim
    
    # Générer une grille de points pour la visualisation
    x, y = np.meshgrid(np.linspace(x_min, x_max, 500), np.linspace(y_min, y_max, 500))
    positions = np.vstack([x.ravel(), y.ravel()])
    
    voronoi_diagram = np.zeros_like(x, dtype=int)
    
    for i, point in enumerate(points):
        distances = np.linalg.norm(positions - np.array(point)[:, None, None], axis=0)
        voronoi_diagram[np.unravel_index(np.argmin(distances, axis=0), x.shape)] = i + 1
    
    return voronoi_diagram

def plot_voronoi(points, voronoi_diagram, xlim, ylim):
    plt.figure(figsize=(8, 8))
    
    plt.imshow(voronoi_diagram, extent=(xlim[0], xlim[1], ylim[0], ylim[1]), origin='lower', cmap='viridis', alpha=0.5)
    plt.scatter(*zip(*points), c='red', marker='o')
    
    plt.xlim(xlim)
    plt.ylim(ylim)
    
    plt.title('Diagramme de Voronoi')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    
    plt.show()

# Exemple d'utilisation
points = [(2, 3), (5, 8), (9, 5), (12, 10)]
xlim = (0, 15)
ylim = (0, 15)

voronoi_diagram = voronoi(points, xlim, ylim)
plot_voronoi(points, voronoi_diagram, xlim, ylim)