from sanic import Sanic
from redirect_router import balancer
from config import SERVER_CONFIG

app = Sanic(__name__)
app.blueprint(balancer)

if __name__ == '__main__':
    app.run(host=SERVER_CONFIG.HOST, port=SERVER_CONFIG.PORT, debug=SERVER_CONFIG.DEBUG)
