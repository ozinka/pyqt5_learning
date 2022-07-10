import getpass4
import string
from time import perf_counter

passwd = getpass4.getpass(prompt='Password: ', char='-')
# passwd = 'Acer5'
dct = string.ascii_lowercase + string.ascii_uppercase + string.digits



def increase(wrd: string) -> str:
    if len(wrd) == 0:
        return dct[0]
    if wrd[-1] == dct[-1]:
        return increase(wrd[:-1]) + dct[0]
    return wrd[:-1] + dct[dct.index(wrd[-1]) + 1]


def calc(wrd):
    while len(wrd) < 12:
        # print(f"Checking: {wrd + '_'}")
        for i in dct:
            if wrd + i == passwd:
                print(f"Password is: {wrd + i}")
                return
        wrd = increase(wrd)
    return None


if __name__ == "__main__":
    cur_time = perf_counter()
    calc('')
    end_time = perf_counter()
    print(f'Elapsed time (s): {end_time - cur_time}')
