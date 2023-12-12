import os
import re

import matplotlib.pyplot as plt

# Liste des fichiers avec l'extension .kml dans le dossier actif
CurrentPath = os.getcwd()
kml_files = [
    filename for filename in os.listdir(CurrentPath)
    if filename.endswith(".kml")
]
# Lire le contenu du fichier .kml et stocker dans une variable
FilePath = os.path.join(CurrentPath, kml_files[0])
FileName = os.path.splitext(os.path.basename(FilePath))[0]
with open(FilePath, 'r') as file:
  kml_content = file.read()

data = []

# Récupérer les lots
pattern = r'<Placemark>(.*?)</Placemark>'
placemarks = re.findall(pattern, kml_content, re.DOTALL)
placemarks = [placemark.replace('\t', '') for placemark in placemarks]
# Pour chaque lot afficher son nom
for placemark in placemarks:
  pattern = r'<name>(.*?)</name>'
  name = re.findall(pattern, placemark, re.DOTALL)
  data.append([name, []])
  # Récupérer les polygones
  pattern = r'<Polygon>(.*?)</Polygon>'
  polygons = re.findall(pattern, placemark, re.DOTALL)
  # Pour chaque polygone
  for polygon in polygons:
    # Récupérer les outer
    pattern = r'<outerBoundaryIs>(.*?)</outerBoundaryIs>'
    outers = re.findall(pattern, polygon, re.DOTALL)
    # Pour chaque outer
    for outer in outers:
      data[-1][-1].append(['o', []])
      pattern = r'<coordinates>(.*?)</coordinates>'
      coordinates = re.findall(pattern, outer, re.DOTALL)
      coordinates = coordinates[0].split('\n')
      coordinates = coordinates[1:-1]
      x = []
      y = []
      for coordinate in coordinates:
        co = coordinate.split(',')
        data[-1][-1][-1][-1].append(co)
    # Récupérer les inner
    pattern = r'<innerBoundaryIs>(.*?)</innerBoundaryIs>'
    inners = re.findall(pattern, polygon, re.DOTALL)
    # Pour chaque inner
    for inner in inners:
      data[-1][-1].append(['i', []])
      pattern = r'<coordinates>(.*?)</coordinates>'
      coordinates = re.findall(pattern, inner, re.DOTALL)
      coordinates = coordinates[0].split('\n')
      coordinates = coordinates[1:-1]
      x = []
      y = []
      for coordinate in coordinates:
        co = coordinate.split(',')
        data[-1][-1][-1][-1].append(co)

ax = plt.axes()
ax.set_facecolor("lightblue")

for lot in data:
  label = str(lot[0][0])
  for polygon in lot[1]:
    type = str(polygon[0])
    if type == 'o':
      fillcolor = 'yellow'
    if type == 'i':
      fillcolor = 'darkgreen'
    x = []
    y = []
    for coord in polygon[1]:
      xi = float(coord[0])
      yi = float(coord[1])
      x.append(xi)
      y.append(yi)
      plt.plot(xi, yi, 'ro', markersize=1)
    #plt.plot(x, y, color='red', alpha=0, label=type)
    plt.fill(x, y, color=fillcolor, alpha=1, label=type)

plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.legend()
plt.title(str(FileName))
plt.grid(True)
plt.show()