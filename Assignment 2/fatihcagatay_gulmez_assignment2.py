# Fatih Cagatay Gulmez
# 213962062


import heapq
from copy import deepcopy


class PriorityQueue:
    def __init__(self, inlist=None):
        self.priorityqueue = inlist or []
        heapq.heapify(self.priorityqueue)

    def makequeue(self, inlist):
        self.priorityqueue = inlist
        heapq.heapify(self.priorityqueue)

    def insert(self, item):
        heapq.heappush(self.priorityqueue, item)

    def peek(self):
        if len(self.priorityqueue) > 0:
            return self.priorityqueue[0]
        else:
            return None

    def isEmpty(self):
        if len(self.priorityqueue) == 0:
            return True
        else:
            return False

    def deleteMin(self):
        if len(self.priorityqueue) > 0:
            return heapq.heappop(self.priorityqueue)
        else:
            return None

    def decreaseKey(self, item):
        # heapq does not have method to update keys
        # Here, searching the priority queue list to find the item (specifically second value in tuple item. needs to be unique),
        # then updating the item and re-heapifying
        # VERY ineffecient way to implement this function. If this operation is used a lot, consider implementing your own heap
        for i in range(len(self.priorityqueue)):
            if self.priorityqueue[i][1] == item[1]:
                self.priorityqueue[i] = item
                break
        heapq.heapify(self.priorityqueue)


def find_horizon(g, (x, y), cost):
    horizon = []
    parent = x,y
    if x != 0:
        if g[x-1][y] == "X":
            if x-1>0:
                horizon.append((cost+2*g[x-2][y], (x-2,y), parent))
        else:
            horizon.append((cost+g[x - 1][y], (x - 1, y), parent))
    if x != len(g)-1:
        if g[x+1][y] == "X":
            if x+1<len(g)-1:
                horizon.append((cost+2* g[x + 2][y], (x + 2, y), parent))
        else:
            horizon.append((cost+g[x+1][y], (x+1,y), parent))
    if y != 0:
        if g[x][y-1] == "X":
            if y-1>0:
                horizon.append((cost+2*g[x][y - 2], (x, y - 2), parent))
        else:
            horizon.append((cost + g[x][y-1], (x,y-1), parent))
    if y != len(g[0])-1:
        if g[x][y+1] == "X":
            if y+1 <len(g[0])-1:
                horizon.append((cost + 2 * g[x][y + 2], (x, y + 2), parent))
        else:
            horizon.append((cost + g[x][y+1], (x, y+1), parent))
    return horizon


def find_shortest_path(g):
    min_queue = PriorityQueue()
    visited = {(0,0): None}
    current = (0, (0,0), None)
    while current[1] != (len(g)-1, len(g[0])-1):
        points = find_horizon(g, current[1], current[0])
        while len(points)>0:
            a = points.pop()
            if a[1] not in visited:
                min_queue.insert(a)
                visited[a[1]] = current[1]
        current = min_queue.deleteMin()
    x = visited[current[1]]
    path = []
    while x is not None:
        path.append(x)
        x = visited[x]
    path.reverse()
    path.append((len(g)-1, len(g[0])-1))
    # Input: G - 2D array
    # Output: Lowest Cost, Number of steps, Shortest path from 0,0 to m-1, n-1
    # O((V+E)*logV)
    return current[0], path, len(path)-1


def find_horizon_rd(g, (x, y), cost):
    horizon = []
    parent = x,y

    if x != len(g)-1:
        if g[x+1][y] == "X":
            if x+1<len(g)-1:
                horizon.append((cost+2* g[x + 2][y], (x + 2, y), parent))
        else:
            horizon.append((cost+g[x+1][y], (x+1,y), parent))
    if y != len(g[0])-1:
        if g[x][y+1] == "X":
            if y+1 <len(g[0])-1:
                horizon.append((cost + 2 * g[x][y + 2], (x, y + 2), parent))
        else:
            horizon.append((cost + g[x][y+1], (x, y+1), parent))
    return horizon


def find_shortest_path_with_negative_cost(g):
    # Input: 2D Array
    # Output: SAME
    # O(V+E)
    min_queue = PriorityQueue()
    parent_point= {(0, 0): None}
    visited = {(0, 0): None}

    min_queue.insert((0, (0, 0), None))
    mini = 999999
    while not min_queue.isEmpty():
        parent_point.clear()
        current = min_queue.deleteMin()
        parent_point[current[1]] = current[2]
        points = find_horizon_rd(g, current[1], current[0])
        while len(points) > 0:
            a = points.pop()
            if a[1] == (len(g)-1, len(g[0])-1):
                if mini > a[0]:
                    mini = a[0]
                    rtrn = a[0], a[1], a[2]
                    visited2 = deepcopy(visited)
            elif a[1] not in parent_point:

                min_queue.insert(a)

                visited[a[1]] = current[1]

    x = rtrn[2]
    path = []
    while x is not None:
        path.append(x)
        x = visited2[x]
    path.reverse()
    path.append((len(g) - 1, len(g[0]) - 1))
    return rtrn[0], path, len(path) - 1


def find_horizon_check(g, (x, y), cost, checkpoints):
    horizon = []
    parent = x,y
    if x != 0:
        if g[x-1][y] == "Check":
            if checkpoints == 0:
                horizon.append((cost, (x-1,y), parent, checkpoints+1))
            else:
                horizon.append((cost+9999, (x - 1, y), parent, checkpoints + 1))
        else:
            horizon.append((cost+g[x - 1][y], (x - 1, y), parent, checkpoints))
    if x != len(g)-1:
        if g[x+1][y] == "Check":
            if checkpoints == 0:
                horizon.append((cost, (x+1,y), parent, checkpoints+1))
            else:
                horizon.append((cost+9999, (x + 1, y), parent, checkpoints + 1))
        else:
            horizon.append((cost+g[x+1][y], (x+1,y), parent, checkpoints))
    if y != 0:
        if g[x][y-1] == "Check":
            if checkpoints == 0:
                horizon.append((cost, (x, y - 1), parent, checkpoints+1))
            else:
                horizon.append((cost+9999, (x, y - 1), parent, checkpoints + 1))
        else:
            horizon.append((cost + g[x][y-1], (x,y-1), parent, checkpoints))
    if y != len(g[0])-1:
        if g[x][y+1] == "Check":
            if checkpoints == 0:
                horizon.append((cost, (x,y+1), parent, checkpoints+1))
            else:
                horizon.append((cost+9999, (x, y + 1), parent, checkpoints + 1))
        else:
            horizon.append((cost + g[x][y+1], (x, y+1), parent, checkpoints))
    return horizon


def find_shortest_path_with_checkpoint(g):
    for i in range(len(g)):
        for j in range(len(g[i])):
            if g[i][j] != "Check":
                g[i][j]+=9999

    min_queue = PriorityQueue()
    visited = {(0, 0): None}
    current = (0, (0, 0), None, 0)
    while current[1] != (len(g) - 1, len(g[0]) - 1):
        points = find_horizon_check(g, current[1], current[0], current[3])
        while len(points) > 0:
            a = points.pop()
            if a[1] not in visited:
                min_queue.insert(a)
                visited[a[1]] = current[1]
        current = min_queue.deleteMin()
    x = current[2]
    path = []
    while x is not None:
        path.append(x)
        x = visited[x]
    path.reverse()
    path.append((len(g) - 1, len(g[0]) - 1))
    return current[0]-(len(path)-2)*9999, path, len(path) - 1


example1 = [
    [0, "X", 1,  4,  9, "X"],
    [1,  7,  1, "X", 1,  8],
    [1, "X", 1,  20, "X", 4],
    [10, 2,  1, "X", 20,  0]]
example2 = [
    [0, "X", 5, -3, 3, "X"],
    [6, -4, 5, "X", 2, -2],
    [4, "X", -30, -7, "X", 5],
    [5, 2, -2, "X", 2, 0]]
example3 = [
    [0,       1,       1,     "Check",       9,     3],
    [5,       7,       1,     6,       1,     3],
    [3, "Check",       1,     5,       8,     4],
    [10,      2,       5,     4,       3,     0]]


find_shortest_path(example1)
find_shortest_path_with_negative_cost(example2)
print find_shortest_path_with_checkpoint(example3)

