
cache = {}
def grid_traveler(rows,cols):

    num_ways = [[0 for _ in range(cols)] for _ in range(rows)]

    num_ways[0][0] = 1


    for col in range(1, cols): 
        num_ways[0][col] = 1

    for row in range(1, rows): 
        num_ways[row][0] = 1


    for row in range(1, rows):
        for col in range(1, cols):
            num_ways[row][col] = num_ways[row-1][col] + num_ways[row][col-1]

    return num_ways[rows-1][cols-1]

def recursive_grid_traveler(rows, cols, cached):
    if (rows, cols) in cached:
        return cached[(rows, cols)]
    if rows == 1 or cols == 1:
        return 1
    if rows <= 0 or cols <= 0 :
        return 0
    cached[(rows, cols)] = recursive_grid_traveler(rows-1, cols, cached) + recursive_grid_traveler(rows, cols-1, cached)
    return cached[(rows, cols)]
a = recursive_grid_traveler(1,400, cache)
print(a)
b = grid_traveler(1,400)
print(b)
