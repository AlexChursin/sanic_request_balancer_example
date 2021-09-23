from sanic import Sanic, response

app = Sanic(__name__)


@app.route('/')
def handle_request(request):
    return response.redirect('/redirect')



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
