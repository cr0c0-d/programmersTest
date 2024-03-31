'''
240331
월간 코드 챌린지 시즌1 > 트리 트리오 중간값
https://school.programmers.co.kr/learn/courses/30/lessons/68937

문제 설명
n개의 점으로 이루어진 트리가 있습니다. 이때, 트리 상에서 다음과 같은 것들을 정의합니다.

어떤 두 점 사이의 거리는, 두 점을 잇는 경로 상 간선의 개수로 정의합니다.
임의의 3개의 점 a, b, c에 대한 함수 f(a, b, c)의 값을 a와 b 사이의 거리, b와 c 사이의 거리, c와 a 사이의 거리, 3개 값의 중간값으로 정의합니다.
트리의 정점의 개수 n과 트리의 간선을 나타내는 2차원 정수 배열 edges가 매개변수로 주어집니다.
주어진 트리에서 임의의 3개의 점을 뽑아 만들 수 있는 모든 f값 중에서, 제일 큰 값을 구해 return 하도록 solution 함수를 완성해주세요.

제한 사항
n은 3 이상 250,000 이하입니다.
edges의 행의 개수는 n-1 입니다.
edges의 각 행은 [v1, v2] 2개의 정수로 이루어져 있으며, 이는 v1번 정점과 v2번 정점 사이에 간선이 있음을 의미합니다.
v1, v2는 각각 1 이상 n 이하입니다.
v1, v2는 다른 수입니다.
입력으로 주어지는 그래프는 항상 트리입니다.

입출력 예
n	edges	result
4	[[1,2],[2,3],[3,4]]	2
5	[[1,5],[2,5],[3,5],[4,5]]	2
'''
from collections import deque
import copy
def solution(n, edges) :
    # 트리의 지름이 모든 f값 중 가장 큰 값

    edge_list = { i : [ ] for i in range(1, n+1) }

    for i, k in edges :
        edge_list[i].append(k)
        edge_list[k].append(i)


    dist_1, node_1 = bfs(1, edge_list)
    dist_2, node_2 = bfs(node_1[0], edge_list)
    dist_3, node_3 = bfs(node_2[0], edge_list)

    return (len(node_2) == 1 and len(node_3) == 1) and dist_3 - 1 or dist_3


def bfs(start, edge_list) :
    visited = [-1] * (len(edge_list) + 2)
    queue = deque()
    queue.append((start, 0))
    visited[start] = 0
    max_distance = 0

    while queue :
        node, distance = queue.popleft()
        max_distance = max(max_distance, distance)

        for i in edge_list[node] :
            if visited[i] < 0 : # 방문하지 않은 곳이면
                queue.append((i, distance + 1))
                visited[i] = distance + 1

    return max_distance, [i for i, v in enumerate(visited) if v == max_distance]


n, edges = 5, [[1,5],[2,5],[3,5],[4,5]]
print(solution(n, edges))