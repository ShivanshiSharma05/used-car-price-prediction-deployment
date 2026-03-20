import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Load dataset
df = pd.read_csv("car data.csv")

# Drop name column
df.drop("name", axis=1, inplace=True)

# Encode fuel_type
df["fuel_type"] = df["fuel_type"].map({
    "CNG": 0,
    "Diesel": 1,
    "Petrol": 2,
    "LPG": 3,
    "Electric": 4
})

# Encode seller_type
df["seller_type"] = df["seller_type"].map({
    "Dealer": 0,
    "Individual": 1,
    "Trustmark Dealer": 2
})

# Encode transmission
df["transmission"] = df["transmission"].map({
    "Automatic": 0,
    "Manual": 1
})

# Encode owner
df["owner"] = df["owner"].map({
    "First Owner": 0,
    "Second Owner": 1,
    "Third Owner": 2,
    "Fourth & Above Owner": 3,
    "Test Drive Car": 4
})

# Remove missing values
df.dropna(inplace=True)

# Features and target
X = df.drop("selling_price", axis=1)
y = df["selling_price"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

# Train
model.fit(X_train, y_train)

# Save model
pickle.dump(model, open("model.pkl", "wb"))

print("✅ Model trained successfully")