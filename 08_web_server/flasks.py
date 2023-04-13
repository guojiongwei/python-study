# 返回首页

from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route('/flask_add', methods=['POST'])
def flask_add():
    print(request)
    return json.dumps(request.json)


@app.route('/')
def handle_home():
  return render_template('home.html')

print(__name__)
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)
