from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load trained ML model
model = joblib.load("model.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    try:
        data = request.get_json()

        # Create dataframe
        df = pd.DataFrame([{
            "week": float(data["week"]),
            "center_id": float(data["center_id"]),
            "meal_id": float(data["meal_id"]),
            "checkout_price": float(data["checkout_price"]),
            "base_price": float(data["base_price"]),
            "emailer_for_promotion": float(
                data["promotion"]
            ),
            "homepage_featured": float(
                data["featured"]
            ),
            "category": data["category"],
            "cuisine": data["cuisine"],
            "center_type": data["center_type"],
            "op_area": float(data["op_area"])
        }])

        # Feature engineering
        df["price_difference"] = (
            df["base_price"]
            - df["checkout_price"]
        )

        df["discount_percent"] = (
            (
                df["base_price"]
                - df["checkout_price"]
            )
            / df["base_price"].replace(0, 1)
        ) * 100

        # Prediction
        prediction = model.predict(df)[0]

        prediction = max(
            0,
            round(prediction)
        )

        # Add small preparation buffer
        recommended = round(
            prediction * 1.05
        )

        return jsonify({
            "success": True,
            "prediction": prediction,
            "recommended": recommended
        })

    except Exception as e:

        return jsonify({
            "success": False,
            "error": str(e)
        }), 400

import os
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))

    app.run(
        host="0.0.0.0",
        port=port,
        debug=False
    )