from flask import Flask, render_template, request, jsonify
import pandas as pd
from sklearn import linear_model

app = Flask(__name__)


# DATA LOADING

df = pd.read_csv("C:\\Users\\pc\\Desktop\\python, sir zfar iqbal\\simple_linearRegression\\data\\pakistan_used_cars.csv")

print("Data loaded successfully")

print(df)



df.dropna(inplace=True)



categorical_cols = ["make", "model", "fuel_type", "transmission", "body_type", "city"]

# Save unique values for dropdowns before encoding
dropdown_options = {col: sorted(df[col].unique().tolist()) for col in categorical_cols}

data = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

feature = data.drop("price_pkr", axis=1)

Target = data["price_pkr"]

# Model banao aur train karo
lr = linear_model.LinearRegression()
lr.fit(feature, Target)

feature_columns = feature.columns.tolist()

print("Model traine ho gia ")
print("Coefficients:", lr.coef_)
print("Intercept:", lr.intercept_)


# Home page — frontend dikhao
@app.route("/")
def home():
    return render_template("index.html", options=dropdown_options)


# Predict API — frontend yahan 9 values bhejta hai (JSON)
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    year = int(data["year"])
    mileage_km = int(data["mileage_km"])
    engine_cc = int(data["engine_cc"])

    # Build input row with all feature columns set to 0
    input_data = pd.DataFrame([{col: 0 for col in feature_columns}])

    # Set numeric values
    input_data["year"] = year
    input_data["mileage_km"] = mileage_km
    input_data["engine_cc"] = engine_cc

    # Set one-hot encoded categorical values
    for col_name in ["make", "model", "fuel_type", "transmission", "body_type", "city"]:
        dummy_col = f"{col_name}_{data[col_name]}"
        if dummy_col in feature_columns:
            input_data[dummy_col] = 1

    # Model se price predict karo
    price = lr.predict(input_data)[0]

    # Negative price ko 0 rakho
    price = max(0, round(price))

    # Format price as PKR with commas
    formatted_price = f"PKR {price:,}"

    return jsonify({"price": formatted_price})


if __name__ == "__main__":
    app.run(debug=True)
