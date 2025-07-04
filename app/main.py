from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from DevSecOps-secured Flask App on port 5100!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5100)

