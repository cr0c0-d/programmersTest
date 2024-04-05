'''
240405
탐욕법(Greedy) > 섬 연결하기
https://school.programmers.co.kr/learn/courses/30/lessons/42861

문제 설명
n개의 섬 사이에 다리를 건설하는 비용(costs)이 주어질 때,
최소의 비용으로 모든 섬이 서로 통행 가능하도록 만들 때 필요한 최소 비용을 return 하도록 solution을 완성하세요.

다리를 여러 번 건너더라도, 도달할 수만 있으면 통행 가능하다고 봅니다.
예를 들어 A 섬과 B 섬 사이에 다리가 있고, B 섬과 C 섬 사이에 다리가 있으면 A 섬과 C 섬은 서로 통행 가능합니다.

제한사항
섬의 개수 n은 1 이상 100 이하입니다.
costs의 길이는 ((n-1) * n) / 2이하입니다.
임의의 i에 대해, costs[i][0] 와 costs[i] [1]에는 다리가 연결되는 두 섬의 번호가 들어있고, costs[i] [2]에는 이 두 섬을 연결하는 다리를 건설할 때 드는 비용입니다.
같은 연결은 두 번 주어지지 않습니다. 또한 순서가 바뀌더라도 같은 연결로 봅니다. 즉 0과 1 사이를 연결하는 비용이 주어졌을 때, 1과 0의 비용이 주어지지 않습니다.
모든 섬 사이의 다리 건설 비용이 주어지지 않습니다. 이 경우, 두 섬 사이의 건설이 불가능한 것으로 봅니다.
연결할 수 없는 섬은 주어지지 않습니다.
입출력 예

n	costs	return
4	[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]	4
'''
def solution(n, costs) :
    # 섬 개수 1 <= n <= 100
    # 다리 건설 비용 costs    [ 섬의 번호 1, 섬의 번호 2, 비용 ]   중복 없음
    costs.sort(key=lambda x : x[2]) # 비용으로 오름차순
    islands = list(range(n))

    total_costs = 0
    bridge = 0
    rank = [0] * n

    for cost in costs :
        if bridge == n-1 :
            return total_costs

        is1, is2 = cost[0], cost[1]
        root1, root2 = find_root(is1, islands), find_root(is2, islands)

        if root1 == root2 : # 이미 연결된 경우
            continue

        union(root1, root2, rank, islands)
        bridge += 1
        total_costs += cost[2]

    return total_costs


def union(x, y, rank, islands) :
    if rank[x] < rank[y] :
        x, y = y, x
    if rank[x] == rank[y] :
        rank[x] += 1

    islands[y] = x


def find_root(start, islands) :
    parent = islands[start]
    if parent == start :
        return start
    else :
        return find_root(parent, islands)



n, costs = 4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
print(solution(n, costs))