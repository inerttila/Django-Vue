from flask import Flask, request, Response
import requests

app = Flask(__name__)

ORIGINAL_URL = 'http://localhost:8000/'

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def proxy(path):
    target_url = f'{ORIGINAL_URL}/{path}'
    response = requests.get(target_url, params=request.args)
    return Response(response.content, content_type=response.headers['Content-Type'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
