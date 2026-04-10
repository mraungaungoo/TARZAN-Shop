from flask import Flask, render_template, jsonify, request, session
from flask_cors import CORS
import os
import json
import hashlib
import hmac
from datetime import datetime
import random

# Templates နဲ့ Static folder ကို မှန်အောင်ညွှန်ပါ
app = Flask(__name__, 
            template_folder='../templates',
            static_folder='../static')

app.secret_key = os.environ.get('SECRET_KEY', 'tarzan-secret-2024')
CORS(app)

BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN', '')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/admin')
def admin():
    # templates ထဲမှာ admin.html ရှိဖို့ လိုပါတယ်ဗျ
    try:
        return render_template('admin.html')
    except:
        return "Admin panel UI (admin.html) not found."

@app.route('/api/validate', methods=['POST'])
def validate():
    data = request.json
    return jsonify({'success': True, 'user': {'id': '123', 'first_name': 'User'}})

@app.route('/api/products', methods=['GET'])
def get_products():
    products = {
        'mlbb': {'86': 2500, '172': 5000, '257': 7500},
        'paypal': {'us': 50000, 'uk': 45000},
        'vpn': {'1m': 8000, '1y': 60000}
    }
    return jsonify(products)

@app.route('/api/orders/create', methods=['POST'])
def create_order():
    data = request.json
    order_id = f"MG{datetime.now().strftime('%Y%m%d')}{random.randint(1000, 9999)}"
    return jsonify({'success': True, 'order_id': order_id})

@app.route('/api/payment/methods', methods=['GET'])
def get_payment():
    return jsonify({
        'kpay': os.environ.get('KPAY_NUMBER', '09xxxxxxxxx'),
        'wave': os.environ.get('WAVE_NUMBER', '09xxxxxxxxx')
    })

# --- Vercel အတွက် အရေးကြီးသော အပိုင်း ---
def handler(request):
    return app(request)

if __name__ == '__main__':
    app.run()
