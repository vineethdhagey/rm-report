import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Define the features and their SHAP/LIME importance scores
features = ['BMI', 'S5', 'BP', 'AGE', 'S6', 'S1', 'S4', 'SEX', 'S2']  # List of features
shap_importance = [0.45, 0.35, 0.30, 0.25, 0.20, 0.15, 0.10, 0.08, 0.05]  # SHAP values
lime_importance = [0.40, 0.30, 0.25, 0.20, 0.18, 0.12, 0.10, 0.07, 0.04]  # LIME values

# Create a DataFrame for the heatmap
data = {
    'Feature': features,
    'SHAP': shap_importance,
    'LIME': lime_importance
}
df = pd.DataFrame(data)

# Set 'Feature' as the index for the heatmap
df.set_index('Feature', inplace=True)

# Create the heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(df, annot=True, cmap='viridis', fmt='.2f', cbar=True)
plt.title('SHAP vs. LIME Feature Importance')
plt.show()