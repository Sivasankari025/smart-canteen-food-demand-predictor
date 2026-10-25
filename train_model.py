import pandas as pd
import joblib

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# =========================================================
# 1. LOAD DATA
# =========================================================

print("Loading datasets...")

train = pd.read_csv("data/train.csv")
meal = pd.read_csv("data/meal_info.csv")
center = pd.read_csv("data/fulfilment_center_info.csv")

print("Original train shape:", train.shape)


# =========================================================
# 2. MERGE DATASETS
# =========================================================

df = train.merge(
    meal,
    on="meal_id",
    how="left"
)

df = df.merge(
    center,
    on="center_id",
    how="left"
)

print("Merged dataset shape:", df.shape)


# =========================================================
# 3. SAMPLE DATA TO REDUCE MEMORY
# =========================================================

# 100,000 rows are enough for a quick mini-project model.
# random_state makes the result reproducible.

if len(df) > 100000:
    df = df.sample(
        n=100000,
        random_state=42
    ).reset_index(drop=True)

print("Training dataset used:", df.shape)


# =========================================================
# 4. REMOVE DUPLICATES
# =========================================================

df = df.drop_duplicates()


# =========================================================
# 5. HANDLE MISSING VALUES
# =========================================================

# Numerical columns
numeric_columns = df.select_dtypes(
    include=["number"]
).columns

for col in numeric_columns:
    df[col] = df[col].fillna(
        df[col].median()
    )


# Categorical columns
categorical_columns = df.select_dtypes(
    include=["object", "string"]
).columns

for col in categorical_columns:
    df[col] = df[col].fillna(
        df[col].mode()[0]
    )


# =========================================================
# 6. FEATURE ENGINEERING
# =========================================================

# Difference between original and selling price

df["price_difference"] = (
    df["base_price"]
    - df["checkout_price"]
)


# Discount percentage

df["discount_percent"] = (
    (
        df["base_price"]
        - df["checkout_price"]
    )
    / df["base_price"].replace(0, 1)
) * 100


# =========================================================
# 7. SELECT FEATURES
# =========================================================

features = [
    "week",
    "center_id",
    "meal_id",
    "checkout_price",
    "base_price",
    "emailer_for_promotion",
    "homepage_featured",
    "category",
    "cuisine",
    "center_type",
    "op_area",
    "price_difference",
    "discount_percent"
]

X = df[features]

y = df["num_orders"]


# =========================================================
# 8. DEFINE COLUMNS
# =========================================================

categorical = [
    "category",
    "cuisine",
    "center_type"
]

numerical = [
    "week",
    "center_id",
    "meal_id",
    "checkout_price",
    "base_price",
    "emailer_for_promotion",
    "homepage_featured",
    "op_area",
    "price_difference",
    "discount_percent"
]


# =========================================================
# 9. PREPROCESSING
# =========================================================

preprocessor = ColumnTransformer(
    transformers=[
        (
            "cat",
            OneHotEncoder(
                handle_unknown="ignore"
            ),
            categorical
        )
    ],
    remainder="passthrough"
)


# =========================================================
# 10. RANDOM FOREST
# =========================================================

model = RandomForestRegressor(
    n_estimators=50,
    max_depth=15,
    random_state=42,
    n_jobs=2
)


pipeline = Pipeline([
    (
        "preprocessor",
        preprocessor
    ),
    (
        "model",
        model
    )
])


# =========================================================
# 11. TRAIN / TEST SPLIT
# =========================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Training rows:", len(X_train))
print("Testing rows:", len(X_test))


# =========================================================
# 12. TRAIN MODEL
# =========================================================

print("\nTraining Random Forest...")

pipeline.fit(
    X_train,
    y_train
)

print("Training completed!")


# =========================================================
# 13. EVALUATE MODEL
# =========================================================

predictions = pipeline.predict(X_test)

mae = mean_absolute_error(
    y_test,
    predictions
)

rmse = mean_squared_error(
    y_test,
    predictions
) ** 0.5

r2 = r2_score(
    y_test,
    predictions
)


print("\n==============================")
print("BASE MODEL RESULTS")
print("==============================")

print("MAE  :", round(mae, 2))
print("RMSE :", round(rmse, 2))
print("R2   :", round(r2, 4))


# =========================================================
# 14. HYPERPARAMETER TUNING
# =========================================================

print("\nStarting Grid Search...")

parameters = {
    "model__n_estimators": [30, 50],
    "model__max_depth": [10, 15]
}


grid = GridSearchCV(
    pipeline,
    parameters,
    cv=2,
    scoring="neg_mean_absolute_error",
    n_jobs=2
)


grid.fit(
    X_train,
    y_train
)


# =========================================================
# 15. BEST MODEL
# =========================================================

best_model = grid.best_estimator_

print("\n==============================")
print("BEST PARAMETERS")
print("==============================")

print(grid.best_params_)


# =========================================================
# 16. EVALUATE OPTIMIZED MODEL
# =========================================================

optimized_predictions = best_model.predict(
    X_test
)

optimized_mae = mean_absolute_error(
    y_test,
    optimized_predictions
)

optimized_rmse = mean_squared_error(
    y_test,
    optimized_predictions
) ** 0.5

optimized_r2 = r2_score(
    y_test,
    optimized_predictions
)


print("\n==============================")
print("OPTIMIZED MODEL RESULTS")
print("==============================")

print(
    "MAE  :",
    round(optimized_mae, 2)
)

print(
    "RMSE :",
    round(optimized_rmse, 2)
)

print(
    "R2   :",
    round(optimized_r2, 4)
)


# =========================================================
# 17. SAVE MODEL
# =========================================================

joblib.dump(
    best_model,
    "model.pkl"
)

print("\nModel saved successfully!")
print("File: model.pkl")