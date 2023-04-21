def manhattan_distance(pointA, pointB):
    total = 0
    for index in range(len(pointA)):
        total += abs(pointA[index] - pointB[index])
    return total