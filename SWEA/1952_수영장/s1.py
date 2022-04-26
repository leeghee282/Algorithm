# 1952_수영장
# 2022-04-26

import sys
sys.stdin = open('input.txt')


def swim_price(idx, price):
    global min_price
    if idx >= 12:
        if price < min_price:
            min_price = price
        return
    if plan[idx]:
        for i in range(3):
            if i == 0:
                swim_price(idx+1, price + plan[idx] * price_list[i])
            elif i == 1:
                swim_price(idx+1, price + price_list[i])
            else:
                swim_price(idx+3, price + price_list[i])
    else:
        swim_price(idx+1, price)


T = int(input())

for tc in range(1, T + 1):
    price_list = list(map(int, input().split()))
    plan = list(map(int, input().split()))

    min_price = price_list[3]
    swim_price(0, 0)

    print('#{} {}'.format(tc, min_price))