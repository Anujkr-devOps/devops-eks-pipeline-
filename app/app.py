from flask import Flask

app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello, World From DevOps AKS Pipeline! from AKS Pods for Video Demo' 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)