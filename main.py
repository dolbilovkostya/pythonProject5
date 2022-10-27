
from flask import Flask
import utils

app = Flask(__name__)


@app.route("/")
def main_page():
    return utils.get_all()


@app.route('/candidates/<int:pk>/')
def candidates(pk):
    return utils.get_by_pk(pk)


app.run()
