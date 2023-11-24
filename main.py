# from flask import Flask
# app = Flask(__name__)
#
# @app.route('/')
# def hello_geek():
#     return '<h1>Hello from Flask & Docker</h2>'
#
#
# if __name__ == "__main__":
#     app.run(debug=True)

# SEE https://www.freecodecamp.org/news/how-to-dockerize-a-flask-app/ for an EXAMPLE with FLASK

def hello():
    print('Hello !')


if __name__ == '__main__':
    hello()
