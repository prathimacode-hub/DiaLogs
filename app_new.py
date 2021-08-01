from flask import Flask,request,render_template
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import pickle

#pip freeze > requirements.txt
app=Flask(__name__)

@app.route('/kidneydisease',methods=['GET','POST'])
def kidney():
	if request.method=='GET':
		return render_template('kidney_disease_form.html')
	else:
		with open('kidney_disease_prediction','rb') as f:
			model=pickle.load(f)
		Age=int(request.form['Age'])
		Blood_Pressure=int(request.form['Blood_Pressure'])
		Specific_Gravity=float(request.form['Specific_Gravity'])
		Albumin=int(request.form['Albumin'])
		Sugar=int(request.form['Sugar'])
		Red_Blood_Cells=int(request.form['Red_Blood_Cells'])
		new=np.array([[Age,Blood_Pressure,Specific_Gravity,Albumin,Sugar,Red_Blood_Cells]])
		y_pred=model.predict(new)
		return render_template('result.html',y_pred=y_pred)
	
@app.route('/kidneystone',methods=['GET','POST'])
def kidney():
	if request.method=='GET':
		return render_template('kidney_stone_prediction.html')
	else:
		with open('kidney_stone_prediction','rb') as f:
			model=pickle.load(f)
		Age=int(request.form['Age'])
		Blood_Pressure=int(request.form['Blood_Pressure'])
		Specific_Gravity=float(request.form['Specific_Gravity'])
		Albumin=int(request.form['Albumin'])
		Sugar=int(request.form['Sugar'])
		Red_Blood_Cells=int(request.form['Red_Blood_Cells'])
		new=np.array([[Age,Blood_Pressure,Specific_Gravity,Albumin,Sugar,Red_Blood_Cells]])
		y_pred=model.predict(new)
		return render_template('result1.html',y_pred=y_pred)

@app.route('/about')
def about():
	return render_template('about.html')


@app.route('/')
def home():
	return render_template('home.html')


if __name__ == '__main__':
	app.run(debug=True)
	
## if __name__ == '__main__':
##       app.run(host='0.0.0.0', port=5000)


