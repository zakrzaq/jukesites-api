from os import name
from flask import Flask, request
from flask_cors import CORS


from utils.use import use_envs
from api.enquiries import send_enquiry

use_envs()

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/")
def root():
    return {"message": "JukeSites API"}

@app.route("/enquiries/send", methods=['POST'])
def enquiries_send():
    body = request.get_json()
    res = send_enquiry(body)
    return res


if name == '__main__':
    app.run(debug=True, port=5000)
