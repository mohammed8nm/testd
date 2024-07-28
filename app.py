# app.py

from flask import Flask, jsonify, request
import requests

COVALENT_API_KEY = 'cqt_wFb4xHHk7pPXKcVgjpC6BW3hrwqB'
CHAIN_ID = 1
app = Flask(__name__)

@app.route('/')
def home():
    return "Covalent Crypto Wallet API"


@app.route('/assets', methods=['GET'])
def get_assets():
    wallet_address = request.args.get('wallet_address')
    url = f'https://api.covalenthq.com/v1/{CHAIN_ID}/address/{wallet_address}/balances_v2/?key={COVALENT_API_KEY}'
    response = requests.get(url)
    data = response.json()
    return jsonify(data)


@app.route('/total_value', methods=['GET'])
def get_total_value():
    wallet_address = request.args.get('wallet_address')
    url = f'https://api.covalenthq.com/v1/{CHAIN_ID}/address/{wallet_address}/balances_v2/?key={COVALENT_API_KEY}'
    response = requests.get(url)
    data = response.json()
    total_value = sum(item['quote'] for item in data['data']['items'] if item['quote'] is not None)
    return jsonify({'total_usd_value': total_value})
    

@app.route('/transactions', methods=['GET'])
def get_transactions():
    wallet_address = request.args.get('wallet_address')
    page_number = request.args.get('page_number', '0')
    url = f'https://api.covalenthq.com/v1/{CHAIN_ID}/address/{wallet_address}/transactions_v2/?page-number={page_number}&key={COVALENT_API_KEY}'
    response = requests.get(url)
    data = response.json()
    return jsonify(data)



if __name__ == '__main__':
    app.run(debug=True)