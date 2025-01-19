import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load dataset
data = pd.read_csv('house-prices.csv')  # Replace with your dataset

# Handle missing values for numeric columns
numeric_data = data.select_dtypes(include=['number'])
data[numeric_data.columns] = numeric_data.fillna(numeric_data.mean())

# One-hot encode categorical columns
data = pd.get_dummies(data, columns=['location'], drop_first=True)

# Feature scaling
scaler = StandardScaler()
scaled_features = ['area', 'bedrooms', 'bathrooms']  # Update based on your dataset
data[scaled_features] = scaler.fit_transform(data[scaled_features])

# Train-test split
X = data.drop('price', axis=1)  # 'price' is the target column
y = data['price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Save processed data
X_train.to_csv('X_train.csv', index=False)
y_train.to_csv('y_train.csv', index=False)
X_test.to_csv('X_test.csv', index=False)
y_test.to_csv('y_test.csv', index=False)

print("Preprocessing complete. Files saved!")
