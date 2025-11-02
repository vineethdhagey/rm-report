# Comparative Study of SHAP and LIME in Explainable AI for Diabetes Risk Prediction

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Research](https://img.shields.io/badge/Research-XAI-orange.svg)](https://en.wikipedia.org/wiki/Explainable_artificial_intelligence)

## 📋 Overview

This research project conducts a comparative analysis of two prominent Explainable AI (XAI) techniques—**SHAP (SHapley Additive exPlanations)** and **LIME (Local Interpretable Model-agnostic Explanations)**—for predicting diabetes risk. The study focuses on evaluating feature importance, interpretability, and computational performance, with particular emphasis on the role of Body Mass Index (BMI) as a dominant factor in healthcare predictions.

The project implements machine learning models trained on real-world diabetes data, applies SHAP and LIME for model explanations, and visualizes the results to address gaps in model transparency within healthcare applications.

### 🎯 Key Objectives
- Compare SHAP and LIME in terms of accuracy, interpretability, and efficiency for diabetes risk prediction.
- Investigate BMI's relevance as a key predictor in healthcare models.
- Provide visualizations and insights to enhance model transparency.
- Contribute to the field of Explainable AI in medical decision-making.

### 🔍 Research Highlights
- **Dataset**: Diabetes dataset from the UCI Machine Learning Repository.
- **Model**: Random Forest Regressor for prediction.
- **Focus**: Feature importance analysis, especially BMI's impact.
- **Visualizations**: SHAP summary plots, LIME explanations, comparative bar charts, and heatmaps.

## 📁 Project Structure

```
rmreport/
├── lime_analysis.py          # LIME implementation and visualization
├── shap_analysis.py          # SHAP implementation and visualization
├── overall_analysis.py       # Comparative bar chart analysis
├── overall_analysis3.py      # Comparative heatmap analysis
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
├── report.pdf                # Detailed research report
├── rm final report.pdf       # Final research manuscript
├── archive/                  # Archived data and files
│   └── diabetes.tab.txt      # Diabetes dataset
├── references/               # Research papers and references
├── acmart-master/            # ACM LaTeX template (for report formatting)
└── *.png                     # Analysis visualizations (e.g., Figure_1.png, analysis 2.png)
```

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### 1. Clone the Repository
```bash
git clone https://github.com/vineethdhagey/rm-report.git
cd rm-report
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

**Key Dependencies:**
- `pandas==2.2.2` - Data manipulation
- `numpy==1.26.4` - Numerical computations
- `matplotlib==3.9.2` - Plotting and visualizations
- `seaborn==0.13.2` - Statistical data visualization
- `scikit-learn==1.5.2` - Machine learning algorithms
- `lime==0.2.0.1` - Local Interpretable Model-agnostic Explanations
- `shap==0.46.0` - SHapley Additive exPlanations

### 3. Dataset Setup
The project uses the diabetes dataset, which is included in the `archive/diabetes.tab.txt` file. No additional download is required.

## 🚀 Usage

### Running Individual Analyses

1. **LIME Analysis**:
   ```bash
   python lime_analysis.py
   ```
   - Generates LIME explanations for individual predictions.
   - Displays feature contributions for a specific test instance.

2. **SHAP Analysis**:
   ```bash
   python shap_analysis.py
   ```
   - Computes SHAP values for the test set.
   - Produces summary plots and force plots for feature importance.

3. **Overall Comparative Analysis (Bar Chart)**:
   ```bash
   python overall_analysis.py
   ```
   - Creates a bar chart comparing SHAP and LIME feature importance scores.

4. **Overall Comparative Analysis (Heatmap)**:
   ```bash
   python overall_analysis3.py
   ```
   - Generates a heatmap visualizing SHAP vs. LIME importance across features.

### Expected Output
- Interactive plots (SHAP force plots may require a Jupyter environment for full interactivity).
- Static images saved as PNG files (e.g., `Figure_1.png`, `analysis 2.png`).
- Console output with model performance metrics.

## 📊 Dataset Description

- **Source**: UCI Machine Learning Repository - Diabetes Dataset
- **Features**: 10 baseline variables (age, sex, BMI, average blood pressure, and six blood serum measurements)
- **Target**: Quantitative measure of disease progression one year after baseline
- **Samples**: 442 instances
- **File**: `archive/diabetes.tab.txt`

### Feature Details
- AGE: Age in years
- SEX: Biological sex
- BMI: Body Mass Index
- BP: Average blood pressure
- S1-S6: Six blood serum measurements (e.g., cholesterol, triglycerides)

## 📈 Results & Visualizations

### Key Findings
- **BMI Dominance**: Both SHAP and LIME consistently identify BMI as the most influential feature for diabetes risk prediction.
- **SHAP vs. LIME**: SHAP provides more consistent and globally interpretable results, while LIME offers localized explanations.
- **Computational Performance**: SHAP is more computationally intensive but offers better scalability for larger datasets.

### Sample Visualizations

#### SHAP Summary Plot
<img width="800" height="549" alt="Figure_1" src="https://github.com/user-attachments/assets/8d851944-ae79-4dd6-b841-a07f6ff753ae" />

*Figure 1: SHAP feature importance summary showing BMI as the top contributor.*

#### Heatmap Comparison
<img width="1536" height="754" alt="analysis 2" src="https://github.com/user-attachments/assets/f17ab453-3ae8-45b6-8e13-9e5478bac2a8" />

*Figure 3: Heatmap visualization comparing SHAP and LIME across features.*

## 📝 Scripts Overview

### `lime_analysis.py`
- Loads and preprocesses the diabetes dataset.
- Trains a Random Forest Regressor.
- Applies LIME to explain individual predictions.
- Generates LIME explanation plots.

### `shap_analysis.py`
- Loads and preprocesses the diabetes dataset.
- Trains a Random Forest Regressor.
- Uses SHAP TreeExplainer for efficient computation.
- Produces SHAP summary and force plots.

### `overall_analysis.py`
- Defines feature importance scores for SHAP and LIME.
- Creates a comparative bar chart.
- Annotates values for clarity.

### `overall_analysis3.py`
- Structures data into a DataFrame for heatmap visualization.
- Uses Seaborn to generate a feature importance heatmap.
- Compares SHAP and LIME side-by-side.

## 📚 References & Reports

- **Research Reports**:
  - `report.pdf`: Preliminary research findings
  - `rm final report.pdf`: Complete research manuscript

- **Reference Papers** (in `references/` folder):
  - Preventing Health Records Risk Analysis with Explainable AI
  - Additional academic papers on XAI and healthcare

- **Key Citations**:
  - Lundberg, S. M., & Lee, S. I. (2017). A unified approach to interpreting model predictions. *Advances in Neural Information Processing Systems*, 30.
  - Ribeiro, M. T., Singh, S., & Guestrin, C. (2016). "Why should I trust you?": Explaining the predictions of any classifier. *Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining*.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an Issue for:
- Bug fixes
- Feature enhancements
- Additional XAI techniques
- Improved visualizations

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Vineeth Dhagey**
- **Email**: dhageyvineeth@gmail.com

---

*This project was developed as part of a research study on Explainable AI applications in healthcare. For detailed methodology and results, refer to the full research reports included in the repository.*
