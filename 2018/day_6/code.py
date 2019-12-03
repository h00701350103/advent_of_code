


from collections import namedtuple
import math

#x range 43 - 359



Result = namedtuple('Result', ['owner', 'distance'])

def star_1():
    board = {}
    areas = {}
    results = []


    with open('input.txt') as f:
        for line in f:
            x, y = [int(i) for i in line.split(',')]
            board[(x, y)] = Result((x, y), 0)
            areas[(x, y)] = 1
    new_sources = list(areas.keys())

    distance = 1
    distance_since_popped = 0
    while True:
        active_sources = new_sources[:]
        for source in active_sources:
            added_area=0

            for x_diff in range(-distance, distance+1):
                y_list = [abs(x_diff) - distance]
                if y_list[0] != 0:
                    y_list.append(-y_list[0])
                for y_diff in y_list:
                    coord = (source[0] + x_diff, source[1] + y_diff)
                    if coord not in board:
                        board[coord] = Result(source, distance)
                        areas[source] += 1
                        added_area += 1
                    elif board[coord].distance == distance:
                        if board[coord].owner != '.':
                            areas[board[coord].owner] -= 1
                        board[coord] = Result('.', distance)
            #remove source from active_sources
            if added_area == 0:
                results.append((source, areas[source]))
                new_sources.remove(source)
                distance_since_popped = 0


        if distance_since_popped == 10 and results:
            print(results)
            print(max(results, key= lambda x: x[1]))
            distance_since_popped = 0
            input()
        distance_since_popped += 1
        distance += 1


def star_2(filename, max_dist):
    sources = []
    total = [0, 0]
    total_points = 0

    with open(filename) as f:
        for line in f:
            x, y = [int(i) for i in line.split(',')]
            sources.append((x, y))
            total[0] += x
            total[1] += y
    midpoint = (math.floor(total[0] / len(sources)),
                math.floor(total[1] / len(sources)))
    
    for y_dir in -1, +1:
        y_delta = 0 if y_dir == -1 else 1
        while True:
            row_added_points = 0
            
            for x_dir in -1, +1:
                x_delta = 0 if x_dir == -1 else 1
                while included(sources,
                               (midpoint[0] + x_delta, midpoint[1] + y_delta),
                               max_dist):
                    row_added_points += 1
                    x_delta += x_dir
                print(x_delta, y_delta)
                input()
            
            if row_added_points == 0:
                print(y_delta)
                break
            total_points += row_added_points
            y_delta += y_dir
    print(total_points)



def included(sources, point, max_dist):
    total_dist = 0
    for source in sources:
        total_dist += abs(source[0] - point[0]) + abs(source[1] - point[1])
        if total_dist >= max_dist:
            return False
    return True




if __name__ == "__main__":
    star_2('input.txt', 10000)
    #star_2('example.txt', 32)
