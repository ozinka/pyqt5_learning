import getpass
import string
from time import perf_counter

dct = string.ascii_lowercase + string.ascii_uppercase + string.digits
first = dct[0]
last = dct[-1]


def timer(func):
    def wrapper(*arg, **kw):
        t1 = perf_counter()
        res = func(*arg, **kw)
        t2 = perf_counter()
        print(f"{func.__name__}, {t2 - t1}")
        return res

    return wrapper


def increase(wrd: string) -> str:
    if len(wrd) == 0:
        return first
    if wrd[-1] == last:
        return increase(wrd[:-1]) + first
    return wrd[:-1] + dct[dct.index(wrd[-1]) + 1]


@timer
def calc(passwd):
    wrd = ''
    while len(wrd) < 6:
        # print(f"Checkwing: {wrd + '_'}")
        for i in dct:
            if wrd + i == passwd:
                print(f"Password is: {wrd + i}")
                return
        wrd = increase(wrd)


# aaa 3
def calc2(n, passwd):
    if n == 0:
        return ''
    for i in dct:
        if (psw := calc2(n - 1, passwd) + i) == passwd:
            return psw


if __name__ == "__main__":
    # passwd = getpass4.getpass(prompt='Password: ', char='-')
    passwd = 'Acer'
    cur_time = perf_counter()
    # print(calc(passwd))
    print(calc(passwd))
    end_time = perf_counter()
    print(f'Elapsed time (s): {end_time - cur_time}')
