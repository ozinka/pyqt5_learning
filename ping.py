from urllib.request import urlopen
from requests import get
from time import perf_counter


def timer(func):
    def timeit(*args, **kwargs):
        begin = perf_counter()
        func(*args, **kwargs)
        end = perf_counter()
        print(f"Total time taken in {func.__name__}:  {end - begin} sec")

    return timeit


@timer
def get_ip_urllib():
    ip = urlopen('https://api.ipify.org').read().decode('utf-8')
    print(ip)


@timer
def get_iprequests():
    ip = get("https://api.ipify.org").text
    print(ip)


get_ip_urllib()
get_iprequests()
