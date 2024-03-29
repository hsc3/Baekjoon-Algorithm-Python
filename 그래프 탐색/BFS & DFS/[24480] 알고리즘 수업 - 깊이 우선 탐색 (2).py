# [24480] 알고리즘 수업 - 깊이 우선 탐색 (2) | Silver 2 | 그래프 탐색
'''
오늘도 서준이는 깊이 우선 탐색(DFS) 수업 조교를 하고 있다. 아빠가 수업한 내용을 학생들이 잘 이해했는지 문제를 통해서 확인해보자.
N개의 정점과 M개의 간선으로 구성된 무방향 그래프(undirected graph)가 주어진다. 정점 번호는 1번부터 N번이고 모든 간선의 가중치는 1이다.
정점 R에서 시작하여 깊이 우선 탐색으로 노드를 방문할 경우 노드의 방문 순서를 출력하자.

깊이 우선 탐색 의사 코드는 다음과 같다. 인접 정점은 내림차순으로 방문한다.

dfs(V, E, R) {  # V : 정점 집합, E : 간선 집합, R : 시작 정점
    visited[R] <- YES;  # 시작 정점 R을 방문 했다고 표시한다.
    for each x ∈ E(R)  # E(R) : 정점 R의 인접 정점 집합.(정점 번호를 내림차순으로 방문한다)
        if (visited[x] = NO) then dfs(V, E, x);
}
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def DFS(u):
    global visit_num

    visited[u] = True
    answer[u] = visit_num # 정점 u를 방문한다.

    for adj in sorted(graph[u], reverse=True):
        if not visited[adj]:
            visit_num += 1
            DFS(adj) # 정점 u의 인접한 정점 adj를 방문한다. -> 재귀로 정점 adj의 인접한 정점 방문
            # 정점 adj의 인접한 정점들을 모두 방문한면 다시, 정점 u의 인접한 다음 정점 방문

if __name__ == "__main__":
    N, M, R = map(int, input().split()) # 정점, 간선, 시작 정점
    graph = [[] for _ in range(N+1)] # 정점 별 간선 저장
    visited = [False for _ in range(N+1)]

    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    answer = [0 for _ in range(N+1)]
    visit_num = 1
    DFS(R)
    print(*answer[1:], sep='\n')