from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello() -> str:
    return 'Hello'

app.run(host='192.168.219.149', port=5000)
