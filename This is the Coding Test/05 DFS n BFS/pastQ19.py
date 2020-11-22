'''
★기출 19. 연산자 끼워 넣기★
N개의 수로 이루어진 수열이 주어집니다. 또 수와 수 사이에 끼워 넣을 수 있는 N-1개의 연산자가
주어집니다. 연사자는 덧셈, 뺄셈, 곱셈, 나눗셈으로만 이루어져 있습니다. 주어진 수의 순서를
바꾸면 안됩니다. 식의 계산은 연산자 우선순위를 무시하고 앞에서부터 진행해야 합니다. 또 나눗셈은
정수 나눗셈으로 몫만 취합니다. N개의 수와 N-1개의 연산자가 주어졌을 때, 만들 수 있는 식의 결과가
최대인 것과 최소인 것을 구하는 프로그램을 작성하세요
이 문제는 최대 11개의 수가 주어졌을 때, 각 수와 수 사이에 사칙연산 중 하나를 삽입하는
모든 경우에 대해 만들어질 수 있는 결과의 최댓값 및 최솟값을 구하면 된다. 따라서 모든 경우의 수를
계산하기 위하여 완전탐색을 이용하여 문제를 해결할 수 있다. 이 문제에서는 각 사칙연산을 중복하여
사용할 수 있기 때문에, 이 문제를 풀기 위해서는 중복 순열을 계산해야 한다. 본 문제에 대한 정답
소스코드는 itertools의 중복 순열(product) 클래스를 사용하지 않고 DFS를 이용하여 풀겠다.
'''
# A19
n = int(input())
# 연산을 수행하고자 하는 수 리스트
data = list(map(int, input().split()))
# 더하기, 빼기, 곱하기, 나누기 연산자 개수
add, sub, mul, div = map(int, input().split())

# 최솟값과 최댓값 초기화
min_value = 1e9
max_value = -1e9

# 깊이 우선 탐색(DFS) 메서드
def dfs(i, now):
  global min_value, max_value, add, sub, mul, div
  # 모든 연산자를 다 사용한 경우, 최솟값과 최댓값 업데이트
  if i == n:
    min_value = min(min_value, now)
    max_value = max(max_value, now)
  else:
    # 각 연산자에 대하여 재귀적으로 수행
    if add > 0:
      add -= 1
      dfs(i + 1, now + data[i])
      add += 1
    if sub > 0:
      sub -= 1
      dfs(i + 1, now - data[i])
      sub += 1
    if mul > 0:
      mul -= 1
      dfs(i + 1, now * data[i])
      mul += 1
    if div > 0:
      div -= 1
      dfs(i + 1, int(now / data[i]))
      div += 1

# DFS 메서드 호출
dfs(1, data[0])

# 최댓값과 최솟값 차례대로 출력
print(max_value)
print(min_value)
    
