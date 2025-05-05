import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

# Sample training data
df = pd.read_csv('loan_amount_prediction_dataset_v2.csv')

X = df.drop('loan_amount', axis=1)
y = df['loan_amount']

# Train model
model = RandomForestRegressor()
model.fit(X, y)

# Save model to file
joblib.dump(model, 'loan_model.pkl')
print("Model saved as loan_model.pkl")
