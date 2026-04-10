from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "TARZAN-Shop Server is Running!"

@app.route('/api/test')
def test():
    return jsonify({"status": "success", "message": "API is working!"})

def handler(request):
    return app(request)
