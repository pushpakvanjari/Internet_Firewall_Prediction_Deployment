import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import math

app = Flask(__name__,template_folder="template")  # assign Flask = app
model = pickle.load(open('dt_df.pkl', 'rb'))  ### import model 

@app.route('/')  
def home():
    return render_template('Index.html')  ## read index.html file 

@app.route('/predict',methods=['POST'])  # transfer data from html to python / server
def predict():
	int_features = [int(x) for x in request.form.values()]  # Request for data values
	final_features = [np.array(int_features)]  # convert into aaray
	prediction = model.predict(final_features) # Predict
	if prediction ==0:
		return render_template('Index.html',prediction_text="Firewall is allowed".format(prediction))
	elif prediction ==1:
		return render_template('Index.html', prediction_text="Firewall is Denied".format(prediction))
	elif prediction ==2:
		return render_template('Index.html', prediction_text="Firewall is Dropped".format(prediction))
	elif prediction ==3:
		return render_template('Index.html', prediction_text="Both Reset".format(prediction))
	
	
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080)