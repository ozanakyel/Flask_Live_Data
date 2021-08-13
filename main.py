from flask import Flask, render_template, flash, redirect, url_for, session, logging, request, jsonify
from random import random


app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])  # Main sayfa
def index():
    dest1 = {"assyNo":123,
    "bodyNo":12345,
    "spec":"Corolla Blackkkk"}
    return render_template("index.html", dest1=dest1)

@app.route("/load_new_assyNo", methods=['GET', 'POST'])
def load_new_assyNo():
    number = random()
    print("number:", number)
    return jsonify("", render_template('load_new_assyNo_model.html', number=round(number,2)))


if __name__ == "__main__":
    app.run(debug=True)
