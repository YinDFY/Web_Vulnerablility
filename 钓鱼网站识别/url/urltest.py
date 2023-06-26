from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import joblib
# Load the fitted vectorizer
vectorizer = joblib.load('vectorizer.pkl')

# Prepare the input URL
input_url = 'http://example.com'

# Transform the input URL using the fitted vectorizer
input_vector = vectorizer.transform([input_url])

# Load the trained model
loaded_model = joblib.load('model.pkl')

# Use the loaded model for prediction
prediction = loaded_model.predict(input_vector)

# Output the prediction result
print('Prediction:', prediction)
