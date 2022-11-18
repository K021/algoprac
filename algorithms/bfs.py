from collections import deque
from typing import List


# 0, 2, 5, 7 노드만 보면 그래프 다 그릴 수 있음
adj_list = [
    [1, 2, 3, 4],   # 0
    [0, 2, 5],      # 1
    [0, 1, 3, 6],   # 2
    [0, 2, 7],      # 3
    [0],            # 4
    [1, 6],         # 5
    [2, 5, 7],      # 6
    [3, 6, 8],      # 7
    [7],            # 8
]

#   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
adj_matrix = [
    [0, 1, 1, 1, 1, 0, 0, 0, 0, 0],  # 0
    [1, 0, 1, 0, 0, 1, 0, 0, 0, 0],  # 1
    [1, 1, 0, 1, 0, 0, 1, 0, 0, 0],  # 2
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 0],  # 3
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 4
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0],  # 5
    [0, 0, 1, 0, 0, 1, 0, 1, 0, 0],  # 6
    [0, 0, 0, 1, 0, 0, 1, 0, 1, 0],  # 7
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],  # 8
]


def bfs_base(start: int, adj: List[List[int]]):
    discovered = [False] * len(adj)
    order = list()

    q = deque([start])
    discovered[start] = True
    while q:
        here = q.popleft()
        order.append(here)
        for there in adj[here]:
            if not discovered[there]:
                q.append(there)
                discovered[there] = True

    return order


def bfs_depth_and_parent(start: int, adj: List[List[int]]):
    discovered = [False] * len(adj)
    depth = [-1] * len(adj)
    parent = [-1] * len(adj)

    q = deque([start])
    discovered[start] = True
    depth[start] = 0
    parent[start] = start
    while q:
        here = q.popleft()
        for there in adj[here]:
            if not discovered[there]:
                q.append(there)
                discovered[there] = True
                depth[there] = depth[here] + 1
                parent[there] = here

    return depth, parent


def shortest_path_using_parent(end: int, parent: List[int]):
    v = end
    path = [v]
    while parent[v] != v:
        v = parent[v]
        path.append(v)
    path.reverse()
    return path


order = bfs_base(0, adj_list)
depth, parent = bfs_depth_and_parent(0, adj_list)
path = shortest_path_using_parent(8, parent)
print("order:", order)
print("depth:", depth)
print("parent:", parent)
print("path:", path)

