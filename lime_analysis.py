import lime.lime_tabular
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor  # Using Regressor, update if needed
from sklearn.model_selection import train_test_split

# Load dataset
file_path = "diabetes.tab.txt"
df = pd.read_csv(file_path, delimiter="\t")

# Define features and target
X = df.drop(columns=["Y"])
y = df["Y"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# Create LIME Explainer
lime_explainer = lime.lime_tabular.LimeTabularExplainer(
    training_data=X_train.values,  
    feature_names=X.columns.tolist(),
    mode="regression"  # Change to "classification" if using a classifier
)

# Explain a single prediction
instance_index = 1  # Change this index to analyze different cases
lime_exp = lime_explainer.explain_instance(X_test.iloc[instance_index].values, rf_model.predict)

# LIME Explanation Plot
lime_exp.as_pyplot_figure()
plt.show()
