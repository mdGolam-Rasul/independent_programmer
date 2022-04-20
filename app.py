import numpy as np
from flask import Flask, request, render_template
import pickle
from sklearn import preprocessing
import flask
from flask import request, Flask, render_template
import pickle
from pickle import load
import numpy as np
from sklearn.preprocessing import StandardScaler


app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html')


filename = 'model.pkl'
clf = load(open(filename, 'rb'))



@app.route('/predict', methods=['POST'])
def predict():
	if request.method == "POST":
		Age=int(request.form['Age'])
		Blood_Glucose=int(request.form['Blood_Glucose'])
		Systolic_Blood_Pressure=int(request.form['Systolic_Blood_Pressure'])
		Diastolic_Blood_Pressure=int(request.form['Diastolic_Blood_Pressure'])
		Insulin=int(request.form['Insulin'])
		BMI = float(request.form['BMI'])
		Diabetes_Pedigree_Function=float(request.form['Diabetes_Pedigree_Function'])	


		data = np.array([[Age,Blood_Glucose,Systolic_Blood_Pressure,Diastolic_Blood_Pressure,Insulin,BMI,Diabetes_Pedigree_Function]])
	   
		my_prediction = clf.predict(data)
		return render_template('result.html', prediction=my_prediction)

if __name__ == '__main__':
    app.run(debug=True)