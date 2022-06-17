# 14889_스타트와-링크
# 2022-06-17

def comb(arr, n):
    result = []

    if n == 0:
        return [[]]

    for i in range(len(arr)):
        elem = arr[i]        
        for rest in comb(arr[i+1:], n-1):
            result.append([elem] + rest)   
    return result


def perm(arr, n):
    result = []
    if n == 0:
        return [[]]

    for i in range(len(arr)):
        elem = arr[i]
        for rest in perm(arr[:i] + arr[i+1:], n - 1):
            result.append([elem] + rest)
    return result


def ability(team1, team2):
    global min_abil

    team1_pt_num = perm(team1, 2)
    team2_pt_num = perm(team2, 2)
    
    t1_pt, t2_pt = 0, 0
    
    for t1 in team1_pt_num:
        t1_i, t1_j = t1
        t1_pt += S[t1_i][t1_j]

    for t2 in team2_pt_num:
        t2_i, t2_j = t2
        t2_pt += S[t2_i][t2_j]

    if abs((t1_pt - t2_pt)) < min_abil:
        min_abil = abs((t1_pt - t2_pt))


N = int(input())

S = [list(map(int, input().split())) for _ in range(N)]

min_abil = 9999

team_lst = []
for i in range(N):
    team_lst.append(i)

start_teams = comb(team_lst, N//2)
link_teams = []
for start_team in start_teams:
    tmp = [x for x in team_lst if x not in start_team]
    link_teams.append(tmp)

for n in range(len(start_teams)):
    ability(start_teams[n], link_teams[n])

print(min_abil)