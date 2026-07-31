import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
import joblib
import os

# Load data
df = pd.read_csv(os.path.join(os.path.dirname(__file__), "data", "pakistan_used_cars.csv"))

# Drop duplicates
df.drop_duplicates(inplace=True)

# Fill missing mileage_km with median instead of dropping rows
df["mileage_km"] = df["mileage_km"].fillna(df["mileage_km"].median())

# Drop any remaining nulls in other columns
df.dropna(inplace=True)

# Save unique values for each categorical column (for Streamlit dropdowns)
categorical_cols = ["make", "model", "fuel_type", "transmission", "body_type", "city"]
dropdown_options = {col: sorted(df[col].unique().tolist()) for col in categorical_cols}

# One-hot encode categorical columns
data = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

# Split features and target
feature_columns = [col for col in data.columns if col != "price_pkr"]
X = data[feature_columns]
y = data["price_pkr"]

# Train/test split (80/20, reproducible)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Ridge Regression (fixes negative predictions + overfitting)
model = Ridge(alpha=1.0)
model.fit(X_train, y_train)

# Evaluate
predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)
negative_count = (predictions < 0).sum()

print(f"MAE: {mae:,.0f} PKR")
print(f"R2 Score: {r2:.4f}")
print(f"Negative predictions: {negative_count} / {len(predictions)}")

# Save model, feature columns, and dropdown options
model_dir = os.path.join(os.path.dirname(__file__), "model")
os.makedirs(model_dir, exist_ok=True)

joblib.dump({
    "model": model,
    "feature_columns": feature_columns,
    "dropdown_options": dropdown_options
}, os.path.join(model_dir, "car_price_model.joblib"))

print(f"\nModel saved to model/car_price_model.joblib")
