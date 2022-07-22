# import getpass
import string
from time import perf_counter

# passwd = getpass.getpass(prompt='Password: ', char='-')
scope_st = string.ascii_lowercase + string.ascii_uppercase + string.digits
last_symbol = scope_st[-1]
first_symbol = scope_st[0]
passwd = 'Acer'


def timer(func):
    def timeit(*args, **kwargs):
        begin = perf_counter()
        func(*args, **kwargs)
        end = perf_counter()
        print(f"Total time taken in {func.__name__}:  {end - begin} sec")

    return timeit


def increase(wrd: string) -> str:
    if len(wrd) == 0:
        return first_symbol
    if wrd[-1] == last_symbol:
        return increase(wrd[:-1]) + first_symbol
    return wrd[:-1] + scope_st[scope_st.index(wrd[-1]) + 1]


@timer
def calc():
    wrd = ''
    while len(wrd) < 6:
        # print(f"Checking: {wrd + '_'}")
        for i in scope_st:
            if wrd + i == passwd:
                print(f"Password is: {wrd + i}")
                return
        wrd = increase(wrd)
    return None


if __name__ == "__main__":
    calc()
