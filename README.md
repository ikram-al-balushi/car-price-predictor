# Used Car Price Predictor

A Flask web app that predicts used car prices in Pakistan using Linear Regression.

## Live Demo

[car-price-predictor-git-main-muhammad-ikram-s-projects1.vercel.app](https://car-price-predictor-git-main-muhammad-ikram-s-projects1.vercel.app)

## Features

- Predicts used car prices in PKR
- 6 categorical inputs: Make, Model, Fuel Type, Transmission, Body Type, City
- 3 numeric inputs: Year, Mileage (km), Engine (cc)
- Dark themed responsive UI

## Tech Stack

- **Backend:** Flask, scikit-learn (Linear Regression), pandas
- **Frontend:** HTML, CSS, JavaScript
- **Deployment:** Vercel

## Dataset

Pakistan Used Cars dataset (`data/pakistan_used_cars.csv`) with features like make, model, year, mileage, engine cc, fuel type, transmission, body type, city, and price in PKR.

## How It Works

1. CSV data loads at startup
2. Missing values are dropped
3. Categorical columns are one-hot encoded
4. Linear Regression model trains on the full dataset
5. User selects car details on the frontend
6. Frontend sends JSON to `/predict` endpoint
7. Model predicts price and returns formatted PKR value

## Run Locally

```bash
pip install -r requirements.txt
python app.py
```

Open `http://localhost:5000` in browser.

## Project Structure

```
├── data/
│   └── pakistan_used_cars.csv
├── model/
│   └── car_price_model.joblib
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   └── script.js
├── app.py
├── train_model.py
├── requirements.txt
├── vercel.json
└── render.yaml
```
