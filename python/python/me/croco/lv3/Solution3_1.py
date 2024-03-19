'''
2021 카카오 채용연계형 인턴십
표 편집
https://school.programmers.co.kr/learn/courses/30/lessons/81303
'''
def solution(n, k, cmd):
    up = [i-1 for i in range(n+1)]    # 각 행의 직전 행을 가리키는 배열 (인덱스 5 행의 직전 행은 up[5])
    down = [i+1 for i in range(n+1)]   # 각 행의 직후 행을 가리키는 배열 (인덱스 5 행의 직후 행은 down[5])

    deleted = []    # 삭제한 행 인덱스를 담는 배열

    for dir in cmd :

        if dir.startswith("C") : # 행 삭제
            # 현재 행 k 기준, down[k의 직전 행] = k의 직후 행 / up[k의 직후 행] = k의 직전 행
            # down[up[k]] = down[k] / up[down[k]] = up[k]

            down[up[k]] = down[k]
            up[down[k]] = up[k]

            deleted.append(k)

            k = down[k] == n and up[k] or down[k]

        elif dir.startswith("Z") : # 삭제행 복구
            res = deleted.pop()
            down[up[res]] = res
            up[down[res]] = res

        else :
            action, num = dir.split(" ")
            if action == "U" :  # 위로
                for _ in range(int(num)) :
                    k = up[k]

            else :     # 아래로
                for _ in range(int(num)) :
                    k = down[k]

    # answer = ''.join([deleted.__contains__(i) and "X" or "O" for i in range(n)])

    answer = ['O']*n

    for i in deleted :
        answer[i] = 'X'

    answer = ''.join(answer)

    return answer





n = 8
k = 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
print(solution(n, k, cmd))



'''
    answer = ''
    table = [[i, i-1, i+1] for i in range(n)]
    deleted = []

    for dir in cmd :
        if dir[0] == "U" :
            # k -= int(dir[2])
            for _ in range(int(dir[2])) :
                k = table[k][1]

        elif dir[0] == "D" :
            # k += int(dir[2])
            for _ in range(int(dir[2])) :
                k = table[k][2]

        elif dir == "C" :
            prev = table[k-1][0]
            next = table[k+1][0]
            table[k-1][2] = next
            table[k+1][1] = prev
            deleted.append(table[k][0])
            if k == len(table) - len(deleted) :
                k -= 1

        elif dir == "Z" :
            lst = deleted.pop()
            table[lst-1][2] = lst
            table[lst+1][1] = lst



    answer = ''.join([deleted.__contains__(i) and 'X' or 'O' for i in range(n)])

    return answer
    '''