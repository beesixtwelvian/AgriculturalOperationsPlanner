# Winding number

def is_point_inside_polygon(point, polygon):
    x, y = point
    wn = 0  # Winding number

    for i in range(len(polygon) - 1):
        xi, yi = polygon[i]
        xi1, yi1 = polygon[i + 1]

        if yi <= y:
            if yi1 > y and is_left((xi, yi), (xi1, yi1), point) > 0:
                wn += 1
        else:
            if yi1 <= y and is_left((xi, yi), (xi1, yi1), point) < 0:
                wn -= 1

    return wn != 0


def is_left(p0, p1, p2):
    """
    Calcul de l'orientation (gauche/droite) de p0->p1 par rapport à p2.
    Retourne une valeur positive si à gauche, négative si à droite, et zéro si aligné.
    """
    return (p1[0] - p0[0]) * (p2[1] - p0[1]) - (p2[0] - p0[0]) * (p1[1] - p0[1])


# Exemple d'utilisation
polygon = [(0, 0), (0, 5), (5, 5), (5, 0)]  # Polygone convexe
point_inside = (2, 2)
point_outside = (6, 3)

print(f"Le point {point_inside} est à l'intérieur du polygone : {is_point_inside_polygon(point_inside, polygon)}")
print(f"Le point {point_outside} est à l'intérieur du polygone : {is_point_inside_polygon(point_outside, polygon)}")