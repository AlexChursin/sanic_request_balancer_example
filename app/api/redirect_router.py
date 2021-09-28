import logging
from http import HTTPStatus
from sanic import Blueprint, response, json

from .services.proxy_logic import ProxyIter
from .services.service import get_redirected_route

balancer = Blueprint(__name__)
proxy_iter = ProxyIter()



@balancer.get("/")
def proxy_video_balancer(request):
    if 'video' not in request.args:
        return json({'message': "'video' must be in query"}, status=HTTPStatus.BAD_REQUEST)
    try:
        redirect_path = get_redirected_route(video_url=request.args['video'][0], proxy_iter=proxy_iter)
    except Exception as e:
        logging.critical(str(e))
        return json({'message': str(e)}, status=HTTPStatus.BAD_REQUEST)
    return response.redirect(redirect_path, status=301)
