'''
예제 5-11 음료수 얼려 먹기
이 문제는 BFS를 이용했을 때 매우 효과적으로 해결할 수 있다. BFS는 시작 지점에서 가까운 노드부터
차례대로 그래프의 모든 노드를 탐색하기 때문이다. 그러므로 (1, 1) 지점에서부터 BFS를 수행하여
모든 노드의 값을 거리 정보로 넣으면 된다. 특정한 노드를 방문하면 그 이전 노드의 거리에 1을 더한
값을 리스트에 넣는다.
'''
# 5-11
from collections import deque

# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())
# 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
  graph.append(list(map(int, input())))

# 이동할 네 방향 정의(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 소스코드 구현
def bfs(x, y):
  # 큐(Queue) 구현을 위해 deque 라이브러리 사용
  queue = deque()
  queue.append((x, y))
  # 큐가 빌 때까지 반복
  while queue:
    x, y = queue.popleft()
    # 현재 위치에서 네 방향으로의 위치 확인
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      # 미로 찾기 공간을 벗어난 경우 무시
      if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue
      # 벽인 경우 무시
      if graph[nx][ny] == 0:
        continue
      # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx, ny))
  # 가장 오른쪽 아래까지의 최단 거리 변환
  return graph[n - 1][m - 1]

# BFS를 수행한 결과 출력
print(bfs(0, 0))