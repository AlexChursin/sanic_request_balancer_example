from os import environ
from time import time

import pytest

from .config import SERVER_CONFIG
from .services.proxy_logic import ProxyIter
from .services.service import generate_cnd_host_v2, generate_cnd_host, get_redirected_route

video_url = 'http://s3.origin-cluster/video/1488/xcg2djHckad.m3u8'
actual_cdn_url = f'http://{SERVER_CONFIG.HOST_CDN}/s3/video/1488/xcg2djHckad.m3u8'


def test_queries():
    COUNT_QUERY = 20
    proxy_iter = ProxyIter()
    list_res = [get_redirected_route(video_url, proxy_iter) for _ in range(COUNT_QUERY)]
    assert list_res[0] == actual_cdn_url
    assert list_res[9] == video_url
    assert list_res[15] == actual_cdn_url
    assert list_res[19] == video_url


def test_env_file_config():
    from dotenv import load_dotenv
    load_dotenv()
    env_check_list = [k for k, _ in SERVER_CONFIG.__dict__.items() if not k.startswith('__')]
    list_not_found = [param for param in env_check_list if environ.get(param) is None]
    assert len(list_not_found) == 0


@pytest.mark.parametrize('generate_cnd_func', [generate_cnd_host, generate_cnd_host_v2])
def test_generate_cnd_host(generate_cnd_func):
    res = generate_cnd_func(video_url)
    assert res == actual_cdn_url


@pytest.mark.parametrize('func', [generate_cnd_host, generate_cnd_host_v2])
def test_performance_generate_cnd(func):
    COUNT_QUERY = 10000
    stat_time = time()
    [func(video_url) for _ in range(COUNT_QUERY)]
    speed_sec = time() - stat_time
    print(f'speed func {func.__name__}', speed_sec)
    assert speed_sec < 1
