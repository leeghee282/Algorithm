# 17140_이차원-배열과-연산
# 2022-06-28


def R(arr):
    for col in arr:
        cnt = [0] * (max(col) + 1)
        visit = [0] * (max(col) + 1)

        for i in range(100):
            if col[i] == 0:
                break
            cnt[col[i]] += 1

        tmp_lst = []

        for i in range(100):
            if col[i] != 0 and visit[col[i]] == 0:
                visit[col[i]] = 1
                tmp_lst.append((col[i], cnt[col[i]]))

                if len(tmp_lst) > 100:
                    break
        
        for i in range(len(tmp_lst)):
            for j in range(i, len(tmp_lst)):
                if tmp_lst[i][1] > tmp_lst[j][1]:
                    tmp_lst[i], tmp_lst[j] = tmp_lst[j], tmp_lst[i]
        
        for i in range(len(tmp_lst)):
            for j in range(i, len(tmp_lst)):
                if tmp_lst[i][1] == tmp_lst[j][1]:
                    if tmp_lst[i][0] > tmp_lst[j][0]:
                        tmp_lst[i], tmp_lst[j] = tmp_lst[j], tmp_lst[i]
                else:
                    break

        for i in range(100):
            if col[i] == 0:
                break
            col[i] = 0

        for i in range(2*len(tmp_lst)):
            col[i] = tmp_lst[i//2][i%2]


def C(arr):
    new_arr = []

    row, col = 0, 0

    for i in range(100):
        row += 1
        col_tmp = 0

        for j in range(100):
            col_tmp += 1
            if arr[i][j] == 0:
                break

        if col_tmp > col:
            col = col_tmp

        if arr[i][0] == 0:
            break

    for j in range(col):
        new_arr_col = []
        for i in range(row):
            new_arr_col.append(arr[i][j])
        new_arr.append(new_arr_col)

    tmp = R(new_arr)

    cnt_row = len(tmp)
    cnt_col = len(tmp[0])
    res = []

    for j in range(cnt_col):
        new_res_col = []
        for i in range(cnt_row):
            new_res_col.append(tmp[i][j])
        res.append(new_res_col)

    return res


r, c, k = map(int, input().split())
r, c = r-1, c-1

A = [list(map(int, input().split())) for _ in range(3)]
array = [[0]*100 for _ in range(100)]

for i in range(3):
    for j in range(3):
        array[i][j] = A[i][j]

R(array)
print(array)
# ans_lst = []
# ans = -1

# for t in range(100):

# print(ans)