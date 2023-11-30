import click
from flask import Flask
app = Flask(__name__)


HOST = "0.0.0.0"


@click.command()
@click.option('--port', '-p', required=False, type=click.INT, default=None,
              help='Port to communicate with the server')
@click.option('--host', '-h', required=False, type=click.STRING, default='0.0.0.0',
              help='Host address to define server')
def run_app(port=None, host='0.0.0.0'):
    print('port / host from click command : {} / {}'.format(port, host))
    if host is None:
        host = HOST
    if port is None:
        print('Running on PORT :', 'default')
        app.run(debug=True, host=host)
    else:
        print('Running on PORT :', port)
        app.run(debug=True, host=host, port=port)


@app.route('/', methods=['GET'])
def base():
    return '<h1>Hello from Flask & Docker !!</h2>'


@app.route('/action/<port>', methods=['POST', 'GET'])
def hello(port=9999):
    if (port is None) or (port == ""):
        return '<h1>Hello from Flask & Docker from default !!</h2>'
    else:
        return '<h1>Hello from Flask & Docker from port {:} !!</h2>'.format(port)


if __name__ == "__main__":
    run_app()

# SEE https://www.freecodecamp.org/news/how-to-dockerize-a-flask-app/ for an EXAMPLE with FLASK
