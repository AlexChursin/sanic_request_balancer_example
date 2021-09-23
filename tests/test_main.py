from os import environ
from app.routes.redirect_proxy import generate_cnd_host


def test_env_file():
    env_check_list = ['HOST', 'PORT', 'CDN_HOST']
    list_not_found = [param for param in env_check_list if environ.get(param) is not None]
    assert len(list_not_found) == 0
    # raise EnvironmentError(f'{list_n_found} must be added to .env file')


def test_generate_cnd_host():
    res = generate_cnd_host('http://s1.origin-cluster/video/1488/xcg2djHckad.m3u8')
    assert res == f'http://{SDN_HOST}/s1/video/1488/xcg2djHckad.m3u8'
    res = generate_cnd_host('https://s3.origin-cluster/video/1488/xcg2djHckad.m3u8')
    assert res == f'https://{SDN_HOST}/s3/video/1488/xcg2djHckad.m3u8'
