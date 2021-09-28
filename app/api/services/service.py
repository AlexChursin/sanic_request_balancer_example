import logging

from pydantic import BaseModel, AnyHttpUrl, ValidationError
from .proxy_logic import ProxyIter
from ..config import SERVER_CONFIG



class URL(BaseModel):
    url: AnyHttpUrl


def generate_cnd_host(url: str) -> str:
    try:
        index = 8 if url.startswith('https://') else 7  # для парсинга url
        index_d = url[index:].find('/') + index
        cl_url = url[index_d:]  # /video/1488/xcg2dj
        server_name = url[index:index_d].split('.')[0]  # s1
        return url[:index] + f'{SERVER_CONFIG.HOST_CDN}/{server_name}' + cl_url
    except Exception as e:
        logging.error(e)
    return url


def generate_cnd_host_v2(url: str) -> str:
    try:
        v = URL(url=url).url
        return f'{v.scheme}://{SERVER_CONFIG.HOST_CDN}/{v.host.split(".")[0]}{v.path}'
    except ValidationError as e:
        logging.error(e)
    return url


def get_redirected_route(video_url: str, proxy_iter: ProxyIter) -> str:
    if next(proxy_iter) is ProxyIter.RouteType.SERVER:
        redirect_path = video_url
    else:
        redirect_path = generate_cnd_host(url=video_url)
        # redirect_path = generate_cnd_host_v2(url=video_url)  # bad performance
    return redirect_path
