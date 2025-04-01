import shap
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.ensemble import RandomForestRegressor  # Use Regressor instead of Classifier
from sklearn.model_selection import train_test_split

# Load dataset
file_path = "diabetes.tab.txt"
df = pd.read_csv(file_path, delimiter="\t")

# Define features and target
X = df.drop(columns=["Y"])  # 'Y' is the target column
y = df["Y"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest model
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# Use TreeExplainer for efficiency
explainer = shap.TreeExplainer(rf_model)
shap_values = explainer.shap_values(X_test)

# SHAP Summary Plot
shap.summary_plot(shap_values, X_test)

# SHAP Force Plot for a single instance
shap.initjs()
shap.force_plot(explainer.expected_value, shap_values[0], X_test.iloc[0])
