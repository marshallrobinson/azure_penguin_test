from flask import Flask, request, jsonify
import numpy as np
from sklearn.linear_model import LogisticRegression

# --- Sample Model Training ---
# In a real app, you'd load a pre-trained model file (e.g., a .pkl).
# For simplicity, we'll "train" a dummy model on startup.
# Features: culmen_length_mm, culmen_depth_mm, flipper_length_mm
X_train = np.array([
    [39.1, 18.7, 181], # Adelie
    [49.1, 14.8, 220], # Gentoo
    [45.8, 18.9, 197], # Chinstrap
    [37.2, 18.1, 178], # Adelie
    [50.0, 16.3, 230], # Gentoo
])
y_train = np.array([0, 1, 2, 0, 1]) # 0: Adelie, 1: Gentoo, 2: Chinstrap
species_map = {0: "Adelie", 1: "Gentoo", 2: "Chinstrap"}

model = LogisticRegression()
model.fit(X_train, y_train)
# --- End Model Training ---

app = Flask(__name__)

@app.route("/")
def home():
    return "Penguin Species Prediction API"

@app.route("/predict", methods=['POST'])
def predict():
    try:
        # Get data from the POST request
        data = request.get_json(force=True)
        features = np.array(data['features']).reshape(1, -1)

        # Make prediction
        prediction = model.predict(features)
        predicted_species = species_map[prediction[0]]

        return jsonify({
            'prediction': predicted_species,
            'class_id': int(prediction[0])
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == "__main__":
    # Port 8000 is common for cloud deployments
    app.run(host="0.0.0.0", port=8000)
