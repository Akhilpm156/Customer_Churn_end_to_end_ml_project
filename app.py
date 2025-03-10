from flask import Flask, render_template, request
import os
import numpy as np
import pandas as pd
from Customer_Churn_Prediction.pipeline.prediction import PredictionPipeline

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/train', methods=['GET'])
def train():
    os.system('python main.py')
    return "Training Successful..."

@app.route('/predict', methods=['POST'])  # Only POST method needed for form submissions
def index():
    if request.method == 'POST':
        try:
            # Debug: print request.form to check data sent by the user
            print(request.form)  # Debug Line 🔥

            # Read the input data from the form
            Geography_Germany = int(request.form.get('Geography_Germany'))
            Geography_Spain = int(request.form.get('Geography_Spain'))
            Gender_Male = int(request.form.get('Gender_Male'))
            Card_Type_GOLD = int(request.form.get('Card_Type_GOLD'))
            Card_Type_PLATINUM = int(request.form.get('Card_Type_PLATINUM'))
            Card_Type_SILVER = int(request.form.get('Card_Type_SILVER'))
            CreditScore = int(request.form.get('CreditScore'))
            Age = int(request.form.get('Age'))
            Tenure = int(request.form.get('Tenure'))
            Balance = float(request.form.get('Balance'))
            NumOfProducts = int(request.form.get('NumOfProducts'))
            HasCrCard = int(request.form.get('HasCrCard'))
            IsActiveMember = int(request.form.get('IsActiveMember'))
            EstimatedSalary = float(request.form.get('EstimatedSalary'))
            Complain = int(request.form.get('Complain'))
            SatisfactionScore = int(request.form.get('SatisfactionScore'))
            PointEarned = int(request.form.get('PointEarned'))


            # Prepare the data for prediction
            data = [Geography_Germany, Geography_Spain, Gender_Male, Card_Type_GOLD, Card_Type_PLATINUM, Card_Type_SILVER,
                    CreditScore, Age, Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary, 
                    Complain, SatisfactionScore, PointEarned]
            
            # Reshape the data for model input
            data = np.array(data).reshape(1, 17)

            # Create the prediction object and make the prediction
            obj = PredictionPipeline()
            predict = obj.predict(data)

            # Render the results page with prediction
            class_name = ['Customer will not Exit','Customer will Exit']
            return render_template('results.html', prediction=class_name[int(predict[0])])

        except Exception as e:
            print('The Exception message is: ', e)
            return 'Something went wrong'
    else:
        return render_template('index.html')

if __name__ == "__main__":
    
    app.run(host="0.0.0.0", port=8080) # for deployement
    #app.run(host="127.0.0.1", port=8080,debug=True) # for local run