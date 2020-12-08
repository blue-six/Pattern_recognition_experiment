import math

from scipy.stats import norm

data = [-3.9847, -3.5549, -1.2401, -0.9780, -0.7932, -2.8531,
        - 2.7605, -3.7287, -3.5414, -2.2692, -3.4549, -3.0752,
        - 3.9934, 2.8792, -0.9780, 0.7932, 1.1882, 3.0682,
        - 1.5799, -1.4885, -0.7431, -0.4221, -1.1186, 4.2532]
l_a_m = [[0, 6], [1, 0]]
p_prior = [0.9, 0.1]
f = lambda x: [norm.pdf(x, -2, 0.5), norm.pdf(x, 2, 2)]
p_posterior = lambda x: [i * j / sum([i * j for i, j in x]) for i, j in x]


# rw = lambda x: [sum([i * j for i, j in zip(l_a_m[0], p_posterior(zip(f(x), p_prior)))]),
#                 sum([i * j for i, j in zip(l_a_m[1], p_posterior(zip(f(x), p_prior)))])]


def rw(x):
    a = []
    for i_, j in zip(p_prior, f(x)):
        a.append(i_ * j)
    b = sum(a)
    c = [ii / b for ii in a]
    e = []
    for i in l_a_m:
        d = 0
        for j in range(len(i)):
            d += i[j] * c[j]
        e.append(d)
    return e
    # print(c)


for i in data:
    end = rw(i)
    print(end)
