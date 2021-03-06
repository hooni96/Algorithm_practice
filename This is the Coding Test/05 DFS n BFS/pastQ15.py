'''
★기출 15. 특정 거리의 도시 찾기★
문제에서 모든 도로의 거리는 1이다. 이는 다시 말해 모든 간선의 비용이 1이라는 의미인데,
그래프에서 모든 간선의 비용이 동일할 때는 너비 운선 탐색을 이용하여 최단 거리를 찾을 수 있다.
다시 말해 '모든 도로의 거리는 1'이라는 조건 덕분에 너비 우선 탐색을 이용하여 해결할 수 있다.
먼저 특정한 도시 X를 시작점으로 BFS를 수행하여 모든 도시까지의 최단 거리를 계산한 뒤에,
각 최단 거리를 하나씩 확인하며 그 값이 K인 경우에 해당 도시의 번호를 출력하면 된다.
'''
# A15
from collections import deque

# 도시의 개수, 도로의 개수, 거리 정보, 출발 도시 번호
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

# 모든 도로 정보 입력 받기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

print(graph)

# 모든 도시에 대한 최단 거리 초기화
distance = [-1] * (n + 1)
distance[x] = 0 # 출발 도시까지의 거리는 0으로 설정

# 너비 우선 탐색(BFS) 수행
q = deque([x])
while q:
    now = q.popleft()
    # 현재 도시에서 이동할 수 있는 모든 도시를 확인
    for next_node in graph[now]:
        # 아직 방문하지 않은 도시라면
        if distance[next_node] == -1:
            # 최단 거리 갱신
            distance[next_node] = distance[now] + 1
            q.append(next_node)

# 최단 거리가 K인 모든 도시의 번호를 오름차순으로 출력
check = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True

# 만약 최단 거리가 K인 도시가 없다면, -1 출력
if check == False:
    print(-1)33