from os import name
from flask import Flask, request


from utils.use import use_envs
from api.enquiries import send_enquiry
from models.enquiries import Enquiry

use_envs()

app = Flask(__name__)


@app.route("/")
def root():
    return {"message": "JukeSites API"}

@app.route("/enquiries/send", methods=['POST'])
def enquiries_send():
    body = request.get_json()
    print(body)
    res = send_enquiry(Enquiry(**body))
    return res


if name == '__main__':
    app.run(debug=True, port=5000)
