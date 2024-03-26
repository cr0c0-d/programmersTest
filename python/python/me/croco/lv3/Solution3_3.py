'''
240326
2021 Dev-Matching: 웹 백엔드 개발자(상반기) > 다단계 칫솔 판매
https://school.programmers.co.kr/learn/courses/30/lessons/77486

문제설명은 링크 참고

각 판매원의 이름을 담은 배열 enroll,
각 판매원을 다단계 조직에 참여시킨 다른 판매원의 이름을 담은 배열 referral,
판매량 집계 데이터의 판매원 이름을 나열한 배열 seller,
판매량 집계 데이터의 판매 수량을 나열한 배열 amount가 매개변수로 주어질 때,
각 판매원이 득한 이익금을 나열한 배열을 return 하도록 solution 함수를 완성해주세요.
판매원에게 배분된 이익금의 총합을 계산하여(정수형으로), 입력으로 주어진 enroll에 이름이 포함된 순서에 따라 나열하면 됩니다.

제한사항
enroll의 길이는 1 이상 10,000 이하입니다.
enroll에 민호의 이름은 없습니다. 따라서 enroll의 길이는 민호를 제외한 조직 구성원의 총 수입니다.
referral의 길이는 enroll의 길이와 같습니다.
referral 내에서 i 번째에 있는 이름은 배열 enroll 내에서 i 번째에 있는 판매원을 조직에 참여시킨 사람의 이름입니다.
어느 누구의 추천도 없이 조직에 참여한 사람에 대해서는 referral 배열 내에 추천인의 이름이 기입되지 않고 “-“ 가 기입됩니다. 위 예제에서는 john 과 mary 가 이러한 예에 해당합니다.
enroll 에 등장하는 이름은 조직에 참여한 순서에 따릅니다.
즉, 어느 판매원의 이름이 enroll 의 i 번째에 등장한다면, 이 판매원을 조직에 참여시킨 사람의 이름, 즉 referral 의 i 번째 원소는 이미 배열 enroll 의 j 번째 (j < i) 에 등장했음이 보장됩니다.
seller의 길이는 1 이상 100,000 이하입니다.
seller 내의 i 번째에 있는 이름은 i 번째 판매 집계 데이터가 어느 판매원에 의한 것인지를 나타냅니다.
seller 에는 같은 이름이 중복해서 들어있을 수 있습니다.
amount의 길이는 seller의 길이와 같습니다.
amount 내의 i 번째에 있는 수는 i 번째 판매 집계 데이터의 판매량을 나타냅니다.
판매량의 범위, 즉 amount 의 원소들의 범위는 1 이상 100 이하인 자연수입니다.
칫솔 한 개를 판매하여 얻어지는 이익은 100 원으로 정해져 있습니다.
모든 조직 구성원들의 이름은 10 글자 이내의 영문 알파벳 소문자들로만 이루어져 있습니다.
입출력 예
enroll	referral	seller	amount	result
["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]	["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]	["young", "john", "tod", "emily", "mary"]	[12, 4, 2, 5, 10]	[360, 958, 108, 0, 450, 18, 180, 1080]
["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]	["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]	["sam", "emily", "jaimie", "edward"]	[2, 3, 5, 4]	[0, 110, 378, 180, 270, 450, 0, 0]
'''
def solution(enroll, referral, seller, amount) :
    # enroll은 노드, referral은 부모
    # seller와 amount를 순회하며 이익 계산
    # 현재 직원의 이익 계산 -> 부모의 이익 계산 : 루트까지 while문으로 돌리기

    node_dict = dict(zip(enroll, referral))     # 직원별 추천인 연결 딕셔너리 - { 직원 명 : 추천 직원 명}

    total = {name : 0 for name in enroll}       # 직원별 수익 딕셔너리 - { 직원 명 : 수익 } - 초기값은 0

    for man, amt in zip(seller, amount):    # 판매직원과 판매량을 순회
        p = amt * 100   # 판매수익

        curr = man  # 실 판매직원부터 시작

        while curr != "-" and p > 0 :   # 루트 노드가 아니고, 계산할 수익이 0보다 큼
            total[curr] += p - p // 10  # 수익의 10퍼센트를 제외하고 현재 직원의 수익에 더함
            curr = node_dict[curr]      # 다음 계산할 직원은 현재 직원의 추천인
            p //= 10    # 추천인의 수익은 현재 직원의 10퍼센트

    return [total[i] for i in enroll]


enroll, referral, seller, amount = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10]
print(solution(enroll, referral, seller, amount))