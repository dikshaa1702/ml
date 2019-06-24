# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 19:36:32 2019

@author: DiPu
"""

from flask import Flask, request, render_template, url_for
from validator import credit_card

app = Flask(__name__)

@app.route("/main")
def home():
    return render_template("index.html")

@app.route("/result",methods=["POST"])
def output():
    form_data = request.form
    status = credit_card(form_data["card"])
    return render_template("response.html",status=status)

if __name__ == "__main__":
    app.run(debug=True)