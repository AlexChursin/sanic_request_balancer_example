from http import HTTPStatus

from sanic import Blueprint, response, text
from service import get_redirected_route

balancer = Blueprint(__name__)



@balancer.get("/")
def proxy_video_balancer(request):
    if 'video' not in request.args:
        return text('"video" must be in query', status=HTTPStatus.BAD_REQUEST)
    redirect_path = get_redirected_route(request)
    return response.redirect(redirect_path, status=301)
