import json
from flask import Flask, request

app = Flask(__name__)

@app.route('/send_sos', methods=['POST'])
def send_sos():
    data = request.json
    with open('sos_alerts.json', 'a') as f:
        json.dump(data, f)
        f.write('\n')
    return {'status': 'SOS sent'}

@app.route('/get_sos', methods=['GET'])
def get_sos():
    with open('sos_alerts.json', 'r') as f:
        alerts = [json.loads(line) for line in f]
    return {'alerts': alerts}

if __name__ == '__main__':
    app.run(debug=True)
