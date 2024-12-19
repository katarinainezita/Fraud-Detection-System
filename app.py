import pandas as pd
import sklearn
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from flask import Flask, request, render_template
import os

app = Flask(__name__)

model_filename = 'random_forest_model.pkl'
if os.path.exists(model_filename):
    with open(model_filename, 'rb') as model_file:
        rf_model = pickle.load(model_file)
else:
    rf_model = None
    print("Model not found! Train the model first.")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return "No file part"
    file = request.files['file']
    if file.filename == '':
        return "No selected file"
    if file:
        data = pd.read_csv(file)
        try:
            predictions = rf_model.predict(data)
            output = ["Fraud" if pred == 1 else "Bukan Fraud" for pred in predictions]
            return render_template("index.html", predictions=output)
        except Exception as e:
            return f"Error: {str(e)}"
    return "Something went wrong!"

if __name__ == "__main__":
    app.run(debug=True)
