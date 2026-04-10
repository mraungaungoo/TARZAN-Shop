from flask import Flask, render_template, jsonify, request
import os

# Vercel ပေါ်မှာ templates folder ကို မှန်မှန်ကန်ကန် ရှာတွေ့ဖို့အတွက်ပါ
base_dir = os.path.dirname(os.path.abspath(__file__))
template_dir = os.path.join(base_dir, '..', 'templates')
static_dir = os.path.join(base_dir, '..', 'static')

app = Flask(__name__, 
            template_folder=template_dir, 
            static_folder=static_dir)

@app.route('/')
def home():
    # index.html ရှိမရှိ စစ်ပြီးမှ ပြပေးမှာပါ
    return render_template('index.html')

@app.route('/admin')
def admin_page():
    # admin.html ဖိုင်ရှိမှ အလုပ်လုပ်မှာပါ
    return render_template('admin.html')

# API Routes
@app.route('/api/user/profile')
def get_profile():
    return jsonify({
        'balance': 50000,
        'user_name': 'TARZAN User'
    })

@app.route('/api/payment/methods')
def get_payment():
    return jsonify({
        'kpay': '09758509043', # သင့်နံပါတ် ပြောင်းထည့်ပါ
        'wave': '09758509043'
    })

@app.route('/api/orders/create', methods=['POST'])
def create_order():
    import random
    order_id = f"TZ{random.randint(100000, 999999)}"
    return jsonify({'success': True, 'order_id': order_id})

# Vercel Handler
def handler(request):
    return app(request)

if __name__ == '__main__':
    app.run(debug=True)
