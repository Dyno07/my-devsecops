from flask import Flask
from flask_wtf import CSRFProtect

app = Flask(__name__)

app.config['SECRET_KEY'] = '7eccd0cffdf1a3b326f2d50c6f4a86782ef1346a88e75ce0fe355a06a1496d74'
csrf = CSRFProtect(app)

@app.route('/')
def home():
    return "Hello from DevSecOps-secured Flask App on port 5100!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5100)

