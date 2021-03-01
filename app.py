from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from requests import Session
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
Bootstrap(app)

COIN_GECKO_URL = "https://api.coingecko.com/api/v3/coins/list?include_platform=false"
COIN_MARKET_URL = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
parameters = {
    'start': '1',
    'limit': '20',
    'convert': 'USD'
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '7bd8ecae-9401-41e8-80ca-c6dffbaabe07'
}

session = Session()
session.headers.update(headers)
response = session.get(COIN_MARKET_URL, params=parameters)
data = response.json()['data']

gecko_session = Session()
gecko_response = session.get(COIN_GECKO_URL)
gecko_data = gecko_response.json()

cryptos = {}

for row in gecko_data:
    for line in data:
        if row['symbol'] == line['symbol'].lower() and row['name'] == line['name']:
            cryptos[row['name']] = row['id']


@app.route('/')
def top_currencies():
    return render_template("index.html", cryptos=data)


@app.route('/<string:crypto_name>', methods=['GET'])
def get_more_info(crypto_name):
    crypto_id = cryptos.get(crypto_name)
    return render_template("ticker.html", _id=crypto_id, name=crypto_name)


if __name__ == '__main__':
    app.run(debug=True)
