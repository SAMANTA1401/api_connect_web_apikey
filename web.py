from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'this web(web.py) run on port 5001 and connect to api(app2.py) port 5000 using api key'})


@app.route('/get_data', methods=['GET'])
def get_data():
    # Replace with the actual API URL
    api_url = 'http://localhost:5000/students'
    # Replace with the actual API key
    api_key = 'rth25th345ny4ertyrtg5r6ynn46yu566'

    headers = {'X-API-KEY': api_key}
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'error': 'Failed to retrieve data'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)