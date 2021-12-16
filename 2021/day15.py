import heapq, numpy as np
from collections import defaultdict
from pathlib import Path
path = Path.cwd() / 'input' / 'day15.txt'
with open(path) as f:
    arr = [list(map(int, list(line.strip()))) for line in f.readlines()]

# # test
lines = ['1163751742','1381373672','2136511328','3694931569','7463417111','1319128137','1359912421','3125421639','1293138521','2311944581']
arr_test = [list(map(int, list(line.strip()))) for line in lines]
tN, tM = len(arr_test), len(arr_test[0])

def FullMap(grid, T):
    full_arr = np.zeros((len(grid)*T,len(grid[0])*T), dtype = 'int8')
    ori = np.array(grid)
    for j in range(0, 5*len(grid[0]), len(grid[0])):
        for i in range(0, 5*len(grid), len(grid)):
            fetch = (ori + (i + j)) % 9
            fetch[fetch == 0] = 9
            full_arr[i:i+len(grid), j:j+len(grid[0])] = fetch
    return full_arr

def makeGraph(arr):
    dic = {}
    for x in range(len(arr)):
        for y in range(len(arr[0])):
            dic[(x,y)] = {}
            for nx, ny in [[x+1,y], [x-1,y], [x,y+1], [x,y-1]]:
                if 0 <= nx < len(arr) and 0 <= ny < len(arr[0]) : 
                    dic[(x,y)][(nx,ny)] = arr[nx][ny]
    return dic

def ShortestPath(graph, N, M):
    visited = [[False]*M for _ in range(N)]
    visited[0][0] = True
    
    cost = {}
    for n in graph.keys():
        if n == (0,0):
            cost[n] = 0
        else:
            cost[n] = float('inf')

    h = []
    heapq.heappush(h, (0, (0,0)))

    curr = (0, 0)
    while curr != (N-1, M-1):
        p, curr = heapq.heappop(h)
        for nx, ny in graph[curr].keys():
            if not visited[nx][ny]:
                if cost[(nx, ny)] > p + graph[curr][(nx,ny)]:
                    cost[(nx, ny)] = p + graph[curr][(nx,ny)]
                    heapq.heappush(h, (cost[(nx,ny)], (nx,ny)))

    return cost[(N-1, M-1)]

# Part 1
g_p1 = makeGraph(arr)
N , M = len(arr), len(arr[0])
print(ShortestPath(g_p1, N, M))
print('-'*30)


# Part 2
arr_p2 = FullMap(arr, 5)
g_p2 = makeGraph(arr_p2)
N2, M2 = len(arr_p2), len(arr_p2[0])
print(ShortestPath(g_p2, N2, M2))