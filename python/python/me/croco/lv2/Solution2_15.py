'''
240326
연습문제 > 미로 탈출
https://school.programmers.co.kr/learn/courses/30/lessons/159993

문제 설명
1 x 1 크기의 칸들로 이루어진 직사각형 격자 형태의 미로에서 탈출하려고 합니다.
각 칸은 통로 또는 벽으로 구성되어 있으며, 벽으로 된 칸은 지나갈 수 없고 통로로 된 칸으로만 이동할 수 있습니다.
통로들 중 한 칸에는 미로를 빠져나가는 문이 있는데, 이 문은 레버를 당겨서만 열 수 있습니다.
레버 또한 통로들 중 한 칸에 있습니다.
따라서, 출발 지점에서 먼저 레버가 있는 칸으로 이동하여 레버를 당긴 후 미로를 빠져나가는 문이 있는 칸으로 이동하면 됩니다.
이때 아직 레버를 당기지 않았더라도 출구가 있는 칸을 지나갈 수 있습니다.
미로에서 한 칸을 이동하는데 1초가 걸린다고 할 때, 최대한 빠르게 미로를 빠져나가는데 걸리는 시간을 구하려 합니다.

미로를 나타낸 문자열 배열 maps가 매개변수로 주어질 때,
미로를 탈출하는데 필요한 최소 시간을 return 하는 solution 함수를 완성해주세요.
만약, 탈출할 수 없다면 -1을 return 해주세요.

제한사항
5 ≤ maps의 길이 ≤ 100
5 ≤ maps[i]의 길이 ≤ 100
maps[i]는 다음 5개의 문자들로만 이루어져 있습니다.
S : 시작 지점
E : 출구
L : 레버
O : 통로
X : 벽
시작 지점과 출구, 레버는 항상 다른 곳에 존재하며 한 개씩만 존재합니다.
출구는 레버가 당겨지지 않아도 지나갈 수 있으며, 모든 통로, 출구, 레버, 시작점은 여러 번 지나갈 수 있습니다.

입출력 예
maps	result
["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]	16
["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"]	-1
'''
from collections import deque
def solution(maps) :
    # 현재 위치 : S
    # X는 못가고 O만 갈 수 있음
    # S에서 레버 L까지의 최단거리 + 레버 L에서 출구 E까지의 최단거리

    start = []
    lever = []
    goal = []

    for index, c in enumerate(maps) :
        if "S" in c :
            start = [c.index("S"), index]
        if "L" in c :
            lever = [c.index("L"), index]
        if "E" in c :
            goal = [c.index("E"), index]

    start_to_lever = bfs(start, lever, maps)    # 시작 ~ 레버 최단시간
    lever_to_goal = bfs(lever, goal, maps)  # 레버 ~ 출구 최단시간

    if start_to_lever != -1 and lever_to_goal != -1 :   # 둘 다 -1이 아니면
        return start_to_lever + lever_to_goal   # 시간을 합산해서 리턴
    else :  # 둘 중 하나라도 -1이면
        return -1   # -1 리턴


# 이동 가능한 지점인지 확인하는 메서드
def is_valid(x, y, maps, visited) :
    # 갈 수 있으려면
    # maps 영역의 밖이면 안 됨
    # 방문하지 않았던 지점이어야 함
    # (x, y)가 "X" 이면 안 됨
    return 0 <= x < len(maps[0]) and 0 <= y < len(maps) and not visited[y][x] and maps[y][x] != "X"


# 시작지점, 도착지점, maps를 받아 최단시간을 구하는 메서드
def bfs(start, end, maps) :
    q = deque()
    visited = [[False for _ in maps[0]] for _ in maps]  # 각 지점의 방문 여부를 저장
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] # 상하좌우 좌표를 계산하기 위함

    q.append((start[0], start[1], 0))   # 시작지점을 큐에 넣고 계산 시작

    while q :   # 큐에 원소가 남아있는 한 계속 계산
        x, y, time = q.popleft()

        if x == end[0] and y == end[1] :    # 도착 지점에 도달했으면 시간 리턴
            return time

        for d in directions :   # 상하좌우 좌표마다 반복
            nx = x + d[0]
            ny = y + d[1]

            if is_valid(nx, ny, maps, visited) :    # 이동 가능한 지점인지 확인하고
                visited[ny][nx] = True  # 방문 처리 후
                q.append((nx, ny, time + 1))    # 큐에 새로운 지점 삽입

    return -1   # 큐에 원소가 없다면 더이상 이동 가능한 지점이 없다는 뜻





maps = [
    "SOOO",
    "XXOL",
    "OOOE"
]
print(solution(maps))