# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 18:46:44 2019

@author: DiPu
"""

from flask import Flask, request, render_template, url_for
import numpy as np
import pickle
import jsonify
app = Flask(__name__)
model=pickle.load(open("WalmartSales.pkl","rb"))
@app.route("/main")
def home():
    return render_template("index.html")
#def output():
#    form_data = request.form
#    status = credit_card(form_data["card"])
#    return render_template("response.html",status=status)

@app.route('/api',methods=['POST'])
def predict():
    # Get the data from the POST request.
    form_data=request.form
    # Make prediction using model loaded from disk as per the data.
    prediction = model.predict([[np.array(data['Store',"IsHoliday","Temperature","Fuel_Price","MarkDown1","MarkDown2","MarkDown3","MarkDown4","MarkDown5","CPI","Unemployment","Type","Size","DateO"])]])
    # Take the first value of prediction
    output = prediction[0]
    return render_template("response.html",status=output)

if __name__ == "__main__":
    app.run(debug=True)

