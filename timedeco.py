import time
from functools import wraps

def timeit(f=None, *, n_iter=100):
    if f is None:
        return lambda f: timeit(f, n_iter=n_iter) #pour avoir n=1000000 et non n=100, ici on appele une deuxieme fois func, et elle n'est plus None
    
    @wraps(f)
    def timed(*args, **kw):
        acc = 0 #float("inf") creation de nombre infiniment grand
        for i in range(n_iter):
            tick = time.perf_counter()
            result = f(*args, **kw)
            acc = max(acc, time.perf_counter() - tick) #min(acc, time.perf_counter() - tick) comparaison du nombre inf grand et du temps de travail de f la premiere fois

        print(f'{f.__name__} ({args}, {kw}) {acc:2.5f} sec')
        return result

    return timed

result = timeit(sum)(range(10 ** 6))

@timeit(n_iter=10)
def f1():
    time.sleep(1)
    return('f1')


@timeit(n_iter=5)
def f2(a):
    time.sleep(2)
    return(f'f2 {a}')


@timeit(n_iter=8)
def f3(a, *args):
    time.sleep(0.3)
    return (f'f3 {args}')


@timeit(n_iter=6)
def f4(a, *args, **kw):
    time.sleep(0.3)
    return (f'f3 {args} {kw}')


f1()
f2(42)
f3(42, 43)
f4(42, 43, foo=2)
