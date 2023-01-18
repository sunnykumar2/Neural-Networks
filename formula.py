from sympy.core.cache import cacheit

from sympy import binomial


@cacheit
def a(n): return 1 if n == 0 else 2**binomial(n, 2) - \
    sum(a(k)*binomial(n, k) for k in range(n))


n=input()
n=int(n)
print(a(n))
