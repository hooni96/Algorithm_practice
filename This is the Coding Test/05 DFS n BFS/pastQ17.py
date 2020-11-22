'''
★기출 17. 경쟁적 전염★
N * N 크기의 시험관이 있습니다. 특정한 위치에는 바이러스가 존재할 수 있습니다.
바이러스의 종류는 1 ~ K번까지 K가지가 있으며 모든 바이러스는 이 중 하나에 솏합니다.
시험관에 존재하는 모든 바이러스는 1초마다 상, 하, 좌, 우의 방향으로 증식하는데,
매초 번호가 낮은 종류의 바이러스부터 먼저 증식합니다. 또한 증식 과정에서 특정한 칸에 이미 어떠한
바이러스가 있다면, 그곳에는 다른 바이러스가 들어갈 수 없습니다. 시험관의 크기와 바이러스의
위치 정보가 주어졌을 때, S초가 지난 후에 (X, Y)에 졶재하는 바이러스의 종류를 출력하는
프로그램을 작성하세요.

이 문제는 너비 우선 탐색(BFS)을 이용해서 해결할 수 잇다. 다만, 문제에 나와
있는 대로 각 바이러스가 낮은 번호부터 증식한다는 점을 기억하자. 낮은 번호부터 증식하므로, 초기에
큐에 원소를 삽입할 때는 낮은 바이러스의 번호부터 삽입해야한다. 이후에 너비 우선 탐색을 수행하며
방문하지 않은 위치를 차례대로 방문하도록 하면 된다.
'''
# A17
from collections import deque

n, k = map(int, input().split())

graph = [] # 전체 보드 정보를 담는 리스트
data = [] # 바이러스에 대한 정보를 담는 리스트

for i in range(n):
  # 보드 정보를 한 줄 단위로 입력
  graph.append(list(map(int, input().split())))
  for j in range(n):
    # 해당 위치에 바이러스가 존재하는 경우
    if graph[i][j] != 0:
      # (바이러스 종류, 시간, 위치 X, 위치 Y) 삽입
      data.append((graph[i][j], 0, i, j))

# 정렬 이후에 큐로 옮기기(낮은 번호의 바이러스가 먼저 증식하므로)
data.sort()
q = deque(data)

target_s, target_x, target_y = map(int, input().split())

# 바이러스가 퍼져나갈 수 있는 4가지 위치
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 너비 우선 탐색(BFS) 진행
while q:
  virus, s, x, y = q.popleft()
  # 정확히 s초가 지나거나, 큐가 빌 때까지 반복
  if s == target_s:
    break
  # 현재 노드에서 주변 4가지 위치를 각각 확인
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    # 해당 위치로 이동할 수 있는 경우
    if 0 <= nx and nx < n and 0 <= ny and ny < n:
      # 아직 방문하지 않은 위치라면, 그 위치에 바이러스 넣기
      if graph[nx][ny] == 0:
        graph[nx][ny] = virus
        q.append((virus, s + 1, nx, ny))

print(graph[target_x - 1][target_y - 1])