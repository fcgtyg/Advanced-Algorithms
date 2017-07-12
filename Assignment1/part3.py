from collections import deque as q


def number_of_paths(G, start, stop):
    edges = q()
    g=[]
    path_num = 0
    for i in G:
        if i[0] == start:
            edges.append(i)
        else:
            g.append(i)
    G = g
    while len(edges) > 0:
        iter = edges.popleft()
        if iter[1] == stop:
            path_num +=1
        path_num += number_of_paths(G, iter[1], stop)
    return path_num


G=[("A","B"),("A","C"),("B","D"),("C","D"),("C","E"),("D","E")]

print number_of_paths(G, "A", "D")