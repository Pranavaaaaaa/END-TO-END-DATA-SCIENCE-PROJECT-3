from flask import Flask, request, jsonify
import pickle

# Load the model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    # Get data from the POST request
    data = request.get_json()
    features = data['features']  # Example: {"features": [5.1, 3.5, 1.4, 0.2]}
    prediction = model.predict([features])
    return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
