import matplotlib.pyplot as plt
import numpy as np

# Example data for SHAP and LIME feature importance
features = ['BMI', 'S5', 'BP', 'AGE', 'S6', 'S1', 'S4', 'SEX', 'S2']
shap_importance = [0.45, 0.35, 0.30, 0.25, 0.20, 0.15, 0.10, 0.08, 0.05]  # SHAP values
lime_importance = [0.40, 0.30, 0.25, 0.20, 0.18, 0.12, 0.10, 0.07, 0.04]  # LIME values

# Create bar graph
x = np.arange(len(features))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots(figsize=(10, 6))
rects1 = ax.bar(x - width/2, shap_importance, width, label='SHAP', color='blue')
rects2 = ax.bar(x + width/2, lime_importance, width, label='LIME', color='orange')

# Add labels, title, and legend
ax.set_xlabel('Features')
ax.set_ylabel('Importance Score')
ax.set_title('Comparison of SHAP and LIME Feature Importance')
ax.set_xticks(x)
ax.set_xticklabels(features, rotation=45)
ax.legend()

# Add value labels on top of bars
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height:.2f}',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

plt.tight_layout()
plt.show()