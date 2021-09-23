from enum import Enum
import typing

from config import SERVER_CONFIG


class ProxyRoute(Enum):
    CND = 0
    SERVER = 1


def get_proxy_iter() -> typing.Iterator[ProxyRoute]:
    i = 0
    while True:
        i += 1
        if i == 10:  # каждый 10й запрос отправляем на сервер
            i = 0
            yield ProxyRoute.SERVER
        else:
            yield ProxyRoute.CND


proxy_iter = get_proxy_iter()


def generate_cnd_host(url: str) -> str:
    index = 8 if url.startswith('https://') else 7  # для парсинга url
    index_d = url[index:].find('/') + index
    cl_url = url[index_d:]  # /video/1488/xcg2dj
    server_name = url[index:index_d].split('.')[0]  # s1
    return url[:index] + f'{SERVER_CONFIG.HOST_CDN}/{server_name}' + cl_url


def get_redirected_route(request) -> str:
    video_url = str(request.args['video'][0])
    if next(proxy_iter) is ProxyRoute.SERVER:
        redirect_path = video_url
    else:
        redirect_path = generate_cnd_host(url=video_url)
    return redirect_path
