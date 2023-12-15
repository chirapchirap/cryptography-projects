from math import gcd as coprime
mod = 33
t1 = 13
t2 = 22
e1 = 21
e2 = 9
for alpha in range(mod):                                                                            # обрабатывается
        if coprime(alpha, mod) != 1:
            continue
        for beta in range(mod):
            if ((t1 * alpha + beta) % mod == e1) and (
                    (t2 * alpha + beta) % mod == e2):
                print(f'{t1} * {alpha} + {beta} == {e1}')
                print(f'{t2} * {alpha} + {beta} == {e2}')
                print(alpha, beta)
                print('-'*10)
                continue
        