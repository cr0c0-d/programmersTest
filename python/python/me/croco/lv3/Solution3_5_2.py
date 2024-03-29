'''
240328
2019 KAKAO BLIND RECRUITMENT > 길 찾기 게임
https://school.programmers.co.kr/learn/courses/30/lessons/42892

라이언이 구상한(그리고 아마도 라이언만 즐거울만한) 게임은,
카카오 프렌즈를 두 팀으로 나누고,
각 팀이 같은 곳을 다른 순서로 방문하도록 해서 먼저 순회를 마친 팀이 승리하는 것이다.

그냥 지도를 주고 게임을 시작하면 재미가 덜해지므로,
라이언은 방문할 곳의 2차원 좌표 값을 구하고 각 장소를 이진트리의 노드가 되도록 구성한 후,
순회 방법을 힌트로 주어 각 팀이 스스로 경로를 찾도록 할 계획이다.

라이언은 아래와 같은 특별한 규칙으로 트리 노드들을 구성한다.

트리를 구성하는 모든 노드의 x, y 좌표 값은 정수이다.
모든 노드는 서로 다른 x값을 가진다.
같은 레벨(level)에 있는 노드는 같은 y 좌표를 가진다.
자식 노드의 y 값은 항상 부모 노드보다 작다.
임의의 노드 V의 왼쪽 서브 트리(left subtree)에 있는 모든 노드의 x값은 V의 x값보다 작다.
임의의 노드 V의 오른쪽 서브 트리(right subtree)에 있는 모든 노드의 x값은 V의 x값보다 크다.

위 이진트리에서 전위 순회(preorder), 후위 순회(postorder)를 한 결과는 다음과 같고, 이것은 각 팀이 방문해야 할 순서를 의미한다.

전위 순회 : 7, 4, 6, 9, 1, 8, 5, 2, 3
후위 순회 : 9, 6, 5, 8, 1, 4, 3, 2, 7
다행히 두 팀 모두 머리를 모아 분석한 끝에 라이언의 의도를 간신히 알아차렸다.

그러나 여전히 문제는 남아있다. 노드의 수가 예시처럼 적다면 쉽게 해결할 수 있겠지만, 예상대로 라이언은 그렇게 할 생각이 전혀 없었다.

이제 당신이 나설 때가 되었다.

곤경에 빠진 카카오 프렌즈를 위해 이진트리를 구성하는 노드들의 좌표가 담긴 배열 nodeinfo가 매개변수로 주어질 때,
노드들로 구성된 이진트리를 전위 순회, 후위 순회한 결과를 2차원 배열에 순서대로 담아 return 하도록 solution 함수를 완성하자.

제한사항
nodeinfo는 이진트리를 구성하는 각 노드의 좌표가 1번 노드부터 순서대로 들어있는 2차원 배열이다.
nodeinfo의 길이는 1 이상 10,000 이하이다.
nodeinfo[i] 는 i + 1번 노드의 좌표이며, [x축 좌표, y축 좌표] 순으로 들어있다.
모든 노드의 좌표 값은 0 이상 100,000 이하인 정수이다.
트리의 깊이가 1,000 이하인 경우만 입력으로 주어진다.
모든 노드의 좌표는 문제에 주어진 규칙을 따르며, 잘못된 노드 위치가 주어지는 경우는 없다.

nodeinfo	result
[[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]	[[7,4,6,9,1,8,5,2,3],[9,6,5,8,1,4,3,2,7]]
'''
# 재귀함수 사용하지 않고 구현하기
def solution(nodeinfo) :
    # nodeinfo에는 각 노드의 좌표만 있음
    # y가 같으면 같은 레벨, x의 위치로 좌우 서브트리 판단
    # 부모/자식 관계를 저장하고 전위/후위 순회 메서드 만들기

    node_list = [ ]
    for index, xy in enumerate(nodeinfo) :
        node_list.append(Node(index, xy))

    node_list.sort(key=lambda x : (-x.xy[1], x.xy[0]))  # y값 내림차순, x값 오름차순 정렬

    root = None
    for node in node_list :

            if root : # 루트가 있는 경우 (맨 처음 빼고 전부 이쪽 로직)
                parent = root   # 루트부터 자리 탐색 시작

                while True : # 자리 찾을 때까지 반복
                    if parent.xy[0] > node.xy[0] :   # 부모 노드보다 왼쪽일 경우
                        if parent.left :    # 부모에 이미 왼쪽 서브트리가 있으면
                            parent = parent.left    # 부모의 왼쪽 서브트리를 부모로 두고 다시 탐색
                            continue
                        else :      # 왼쪽 서브트리가 없으면
                            parent.left = node  # 현재 노드를 부모의 왼쪽 서브트리로 지정
                            break   # 자리를 찾았으므로 while문 나가기

                    else :  # 부모 노드보다 오른쪽일 경우 (이하 로직은 왼쪽의 경우와 동일)
                        if parent.right :
                            parent = parent.right
                            continue
                        else :
                            parent.right = node
                            break

            else :  # 루트가 없는 경우 (맨 처음 루트일 때만 이쪽)
                root = node

    return [preorder(root), postorder(root)]


def preorder(node) :
    # 전위 순회 순서 : 현재 -> 왼쪽 -> 오른쪽
    # 리턴할 값은 순회할 노드의 인덱스+1을 배열 형식으로
    answer = []
    stack = [node]
    while stack :
        this_node = stack.pop()

        if this_node :
            answer.append(this_node.index + 1)
            stack.append(this_node.right)
            stack.append(this_node.left)

    return answer


def postorder(node) :
    # 후위 순회 순서 : 왼쪽 -> 오른쪽 -> 현재
    # 리턴할 값은 순회할 노드의 인덱스+1을 배열 형식으로
    answer = []
    stack = [(node, False)]
    while stack :
        this_node, visited = stack.pop()

        if this_node:
            if visited :
                answer.append(this_node.index + 1)
            else :
                stack.append((this_node, True))
                stack.append((this_node.right, False))
                stack.append((this_node.left, False))

    return answer


class Node :
    def __init__(self, index, xy):
        self.index = index
        self.xy = xy
        self.left = None
        self.right = None


nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
print(solution(nodeinfo))