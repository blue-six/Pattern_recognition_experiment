import math

import pandas

data = pandas.read_csv("banana.dat", skiprows=[0, 1, 2], header=None)
# print(data_)
w1 = 0
w2 = 0
all_ = data.__len__()
for i in data.iterrows():
    # print(len(i[1]))
    if i[1][2] == 1:
        w1 += 1
    else:
        w2 += 1
# print(w1, w2)
prob1, prob2 = w1 / all_, w2 / all_


def posible(x, h, data_):
    p = [0, 0]
    data_l = data_.values.tolist()
    a = 1 / (all_ * h) * 1 / math.sqrt(2 * math.pi)
    for j in data_l:
        if j[2] == 1:
            p[0] += a * math.exp(-1 / 2 * (abs(j[0] - x)) ** 2 / h)
        else:
            p[1] += a * math.exp(-1 / 2 * (abs(j[0] - x)) ** 2 / h)
    return p


for i in range(-30, 30, 1):
    print(f"{i / 10}:", end='')
    pp = posible(i / 10, 0.01, data)
    pb1 = prob1 * pp[0] / (prob1 * pp[0] + prob2 * pp[1])
    pb2 = prob2 * pp[1] / (prob1 * pp[0] + prob2 * pp[1])
    if pb1 > pb2:
        print("pb1:", pb1)
    else:
        print("pb2:", pb2)
