"""
깊이 우선 탐색
- 그래프의 모든 정점을 발견하는 알고리즘
- 알고리즘
    1. 현재 정점과 인접한 간선들을 하나씩 검사
    2. 아직 방문하지 않은 정점으로 향하는 간선이 있다면 그 간선을 따라 이동
    3. 더 이상 이동할 수 없는 경우, 현재 정점의 부모 정점으로 돌아가서 다시 1번부터 반복
- 시간복잡도: O(V + E) (V: 정점의 수, E: 간선의 수)
- 공간복잡도: O(V) (재귀 호출 스택 사용 시)
- 구현 방법: 재귀 호출 또는 스택을 이용한 반복문
- 적용할 수 있는 상황
    - 경로 탐색: 미로 찾기, 게임 맵 탐색 등.
    - 그래프의 연결 요소 찾기: u 에서 dfs 하면, visited 에 있는 정점들이 u와 연결된 정점들이다.
    - 연결된 부분집합의 갯수 찾기: dfs_all() 에서 dfs() 를 호출하는 횟수
    - 위상 정렬: DAG(Directed Acyclic Graph)에서의 작업 순서 결정
        - dfs_all() 을 수행하며 dfs() 가 종료될 때마다 현재 정점의 번호를 기록
        - dfs_all() 이 종료된 후, 기록된 번호를 역순으로 정렬하면 위상 정렬 결과가 된다.
    - 사이클 탐지: 방향 그래프에서의 사이클 여부 확인 (역순 간선 존재 확인)
    - 오일러 서킷: 모든 간선을 정확히 한 번씩 방문하는 경로 중 시작점과 끝점이 같은 경로
        - 모든 정점의 차수가 짝수여야 한다. (유향 그래프의 경우, 들어오는 간선의 수와 나가는 간선의 수가 같아야 함)
        - 알고리즘
            1. 시작 정점에서 dfs() 를 수행하며 모든 간선을 방문
            2. 방문한 간선들을 기록
            3. 기록된 간선들을 순서대로 출력하면 오일러 서킷이 된다.
            4. 아직 방문하지 않은 간선이 있다면, 그 간선을 따라 dfs() 를 다시 수행
            5. 두 서킷을 합쳐서 하나의 오일러 서킷을 만든다.
    - 오일러 트레일: 모든 간선을 정확히 한 번씩 방문하는 경로 중 시작점과 끝점이 다른 경로
        - 시작 정점과 끝 정점의 차수가 홀수인 정점이 정확히 두 개여야 한다. 각각 시작점과 끝점이 된다.
        - 알고리즘
            1. 차수가 홀수인 두 정점 a, b 를 찾는다.
            2. 간선 (b, a) 를 추가한 후, a 에서 오일러 서킷을 찾는다.
            3. 오일러 서킷을 찾은 후 (b, a) 를 제거한다.
"""


def dfs(graph, start, visited=set()):
    visited.add(start)  # 현재 정점을 방문 처리
    print("Visit:", start)  # 현재 정점 출력

    for neighbor in graph[start]:  # 현재 정점과 인접한 모든 정점에 대해
        if neighbor not in visited:  # 아직 방문하지 않은 정점이라면
            dfs(graph, neighbor, visited)  # 재귀적으로 DFS 호출

    return visited  # 방문한 정점의 집합 반환


# 예시 그래프
example_graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}


# DFS 실행
visited_nodes = dfs(example_graph, 'A')
print("Visited nodes:", visited_nodes)  # 방문한 정점 출력
# 출력: Visit: A, Visit: B, Visit: D, Visit: E, Visit: F, Visit: C
# 방문한 정점: {'A', 'B', 'C', 'D', 'E', 'F'}
# 순서가 다를 수 있음 (DFS는 방문 순서에 따라 다름)
# 예시 그래프는 인접 리스트 형태로 표현됨
# 그래프는 딕셔너리 형태로 표현됨


def dfs_all(graph):
    visited = set()
    for node in graph:
        if node not in visited:
            dfs(graph, node, visited)
    return visited


# dfs 를 이용한 경로 탐색
def find_path_dfs(graph, start, goal, path=[]):
    path = path + [start]
    if start == goal:
        return path
    for neighbor in graph.get(start, []):
        if neighbor not in path:
            new_path = find_path_dfs(graph, neighbor, goal, path)
            if new_path:
                return new_path
    return None

# 경로 탐색 예시
path = find_path_dfs(example_graph, 'A', 'F')
print("Found path:", path)


# 오일러 서킷 예시
# 홀수 점에서 시작하면 오일러 트레일도 구해진다. 
def euler_circuit(graph, here, circuit=list()):
    for there in range(len(graph)):
        if graph[here][there] > 0:
            graph[here][there] -= 1
            graph[there][here] -= 1
            euler_circuit(graph, there, circuit)

    circuit.append(here)

    return circuit[::-1]  # 역순으로 반환