# 17140_이차원-배열과-연산
# 2022-06-27


def R(arr):
    res = []
    max_len = 0
    for col in arr:
        cnt = [0] * (max(col) + 1)
        visit = [0] * (max(col) + 1)

        for i in range(len(col)):
            cnt[col[i]] += 1

        tmp_lst = []

        for i in range(len(col)):
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
        res_c = []
        for t in tmp_lst:
            for c in t:
                res_c.append(c)

        res.append(res_c)

    for r in res:
        if len(r) > max_len:
            max_len = len(r)

    for r in res:
        tmp = max_len - len(r)
        for _ in range(tmp):
            r.append(0)

    return res


def C(arr):
    new_arr = []

    cnt_row = len(arr)
    cnt_col = len(arr[0])

    for j in range(cnt_col):
        new_arr_col = []
        for i in range(cnt_row):
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

A = [list(map(int, input().split())) for _ in range(3)]

ans_lst = []
ans = -1

for t in range(100):
    if t == 0:
        if A[r-1][c-1] == k:
            ans = t
            break
        else:
            ans_lst = R(A)
    else:
        print(ans_lst)
        res_row = len(ans_lst)
        res_col = len(ans_lst[0])

        if res_row >= r and res_col >= c:
            if ans_lst[r-1][c-1] == k:
                ans = t
                break
        else:
            if res_col >= res_row:
                ans_lst = R(ans_lst)
            else:
                ans_lst = C(ans_lst)

print(ans)