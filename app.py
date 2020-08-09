import numpy as np
from flask import Flask,request,jsonify,render_template
import pickle
import pandas as pd
import datetime as dt
from datetime import datetime
from datetime import datetime as dt

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict',methods =['POST'])
def predict():
    option = request.form['options']
    if(option=="LR"):
        date = request.form['date']
        d = dt.strptime(date, '%d-%m-%Y').date()
        date = d.toordinal()
        date = np.array(date)
        date = date.reshape(-1,1)
        prediction = model.predict(date)
        output = int(prediction)
        return render_template('index.html' , pred = "{}".format(output))

if __name__=="__main__":
    app.run(debug=True)
