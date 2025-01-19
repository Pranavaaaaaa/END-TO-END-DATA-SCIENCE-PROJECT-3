import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import pickle

# Load preprocessed data
X_train = pd.read_csv('X_train.csv')
y_train = pd.read_csv('y_train.csv').squeeze()

# Train the model
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Save the trained model
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model training complete. Model saved as 'model.pkl'.")
