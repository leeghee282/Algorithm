# 1206_View 풀이
# 2022-05-19

# input.txt를 연 뒤, data에 list로 저장(줄바꿈 제거)
F = open('input.txt', 'r')
data = F.readlines()
data = list(map(lambda s: s.strip('\n'), data))

T = 10

for n in range(T):
    # tc는 data의 개수, buildings는 각 빌딩의 높이를 list로 저장
    tc = int(data[2*n])
    buildings = list(map(int, data[2*n+1].split()))

    # 결과 값을 초기화
    view = 0

    for i in range(2, tc-1):
        # 조망권을 계산할 수 있는 건물을 선택
        if (buildings[i] > buildings[i-2]) and (buildings[i] > buildings[i-1]) and (buildings[i] > buildings[i+1]) and (buildings[i] > buildings[i+2]):
            # 조망권을 계산하기 위해 선택된 건물의 좌우로 2칸 내에 가장 높은 건물의 높이를 계산
            max_building = 0
            if buildings[i-2] > buildings[i-1]:
                max_building = buildings[i-2]
            else:
                max_building = buildings[i-1]
            if buildings[i+1] > max_building:
                max_building = buildings[i+1]
            if buildings[i+2] > max_building:
                max_building = buildings[i+2]

            # 조망권이 확보된 세대의 수를 계산
            view += buildings[i] - max_building

    # 결과 출력
    print('#{} {}' .format(n+1, view))