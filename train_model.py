import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Load dataset
df = pd.read_csv("car data.csv")

# 1. Clean column names (removes hidden spaces)
df.columns = df.columns.str.strip()

# 2. Remove car name column 
cols_to_drop = ['Name', 'Car_Name']
df.drop(columns=[c for c in cols_to_drop if c in df.columns], inplace=True)

# 3. Encode ALL categorical columns automatically
df = pd.get_dummies(df, drop_first=True)

# 4. Features and target
X = df.drop("Selling_Price", axis=1)
y = df["Selling_Price"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 5. Model
model = RandomForestRegressor(n_estimators=100)
model.fit(X_train, y_train)

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved as model.pkl successfully!")
