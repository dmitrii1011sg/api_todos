import os

from flask import Flask, jsonify
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('TOKEN')


@app.route('/api/task', methods=['GET'])
def index():
    return jsonify({'tasks': 123})


if __name__ == '__main__':
    app.run(debug=True)
