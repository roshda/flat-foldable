# define the vertices of the crease pattern (must do manually)
vertices = [(0, 0), (0, 1), (1, 1), (1, 0), (0.5, 0.5)]

# define the creases of the crease pattern as pairs of vertex indices
creases = [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2), (1, 3), (0, 4), (1, 4), (2, 4), (3, 4)]

# define a function to calculate the angle between two vectors
def angle_between_vectors(a, b):
    dot_product = a[0] * b[0] + a[1] * b[1]
    norm_a = (a[0] ** 2 + a[1] ** 2) ** 0.5
    norm_b = (b[0] ** 2 + b[1] ** 2) ** 0.5
    cos_theta = dot_product / (norm_a * norm_b)
    return math.acos(cos_theta)

# define a function to check if the crease pattern is flat-foldable
def is_flat_foldable(vertices, creases):
    # iterate over each crease in the crease pattern
    for i, (vi, vj) in enumerate(creases):
        # iterate over each adjacent crease to the current crease
        for vk, vl in creases[i+1:] + creases[:i]:
            # if the adjacent crease shares a vertex with the current crease, calculate the angle between the two creases
            if vi == vk or vi == vl or vj == vk or vj == vl:
                vector1 = (vertices[vj][0] - vertices[vi][0], vertices[vj][1] - vertices[vi][1])
                vector2 = (vertices[vl][0] - vertices[vk][0], vertices[vl][1] - vertices[vk][1])
                angle = angle_between_vectors(vector1, vector2)
                # if the angle between the two creases is less than 180 degrees, the crease pattern is not flat-foldable
                if angle < math.pi
