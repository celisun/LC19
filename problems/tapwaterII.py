from heapq import heappush, heappop

# update from the border to center
# calcualate/update water trap using min height grid in heap
if not heightMap or len(heightMap) <= 2 or len(heightMap[0]) <= 2:
    return 0

heap, m, n = [], len(heightMap), len(heightMap[0])
for i in xrange(n):
    heappush(heap, (heightMap[0][i], 0, i))
    heappush(heap, (heightMap[m - 1][i], m - 1, i))
    heightMap[0][i] = -1
    heightMap[m - 1][i] = -1
for j in xrange(m):
    heappush(heap, (heightMap[j][0], j, 0))
    heappush(heap, (heightMap[j][n - 1], j, n - 1))
    heightMap[j][0] = -1
    heightMap[j][n - 1] = -1
res = 0
while heap:
    min_height, i, j = heappop(heap)
    for xi, xj in [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]:
        if 0 <= xi < m and 0 <= xj < n and heightMap[xi][xj] >= 0:
            res += max(0, min_height - heightMap[xi][xj])

            # trap water
            heappush(heap, (max(min_height, heightMap[xi][xj]), xi, xj))
            heightMap[xi][xj] = -1

return res