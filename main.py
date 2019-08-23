from flask import Flask
from config import DevConfig

app = Flask(__name__)
app.config.from_object(DevConfig)

@app.route('/')
def home():
    return '<h1>Hola Mundo!</h1>'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)

