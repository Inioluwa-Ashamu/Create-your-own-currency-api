from bs4 import BeautifulSoup
from flask import Flask, jsonify
import requests

def get_currency(in_currency, out_currency):
  url= f'https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1'
  r = requests.get(url).text
  soup = BeautifulSoup(r, 'html.parser')
  rate = soup.find('span', class_='ccOutputRslt').get_text()
  rate = float(rate[:-4])
  return rate

app = Flask(__name__)
@app.route('/')
def home():
  return '<h1>This is a custom currency calculator</h1> <p>Example URL: /api/v1/usd-eur</p>'

@app.route('/api/v1/<in_cur>-<out_cur>')
def api(in_cur, out_cur):
  rate = get_currency(in_cur, out_cur)
  result = {'Input currency':in_cur, 'Output currency':out_cur, 'Rate':rate}
  return jsonify(result)

app.run(host='0.0.0.0')