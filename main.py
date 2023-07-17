from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/api/v1/message', methods=['POST'])
def message():
    response = request.get_json()

    text = response['message']

    print(text)

    return text

if __name__=='__main__':
    app.run()