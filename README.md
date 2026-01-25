# 🎮 Predictive Analysis of Global Video Game Sales (Linear Regression)

This project applies **Multiple Linear Regression** to predict **global video game sales** using historical industry data.  
The goal is to demonstrate how data-driven models can help publishers and developers make informed business decisions.

---

## 📌 Project Summary

The video game industry is highly competitive, and predicting a game's sales success is challenging.  
This project analyzes sales data from **1980 to 2020** and builds a regression model to estimate **global sales** based on regional performance, platform, genre, and release information.

---

## 🎯 Key Objectives

- Analyze historical video game sales trends  
- Identify important factors affecting global sales  
- Build an accurate and interpretable regression model  
- Evaluate model performance using standard metrics  

---

## 📊 Dataset Overview

- **Source:** Kaggle – Video Game Sales Dataset  
- **Records:** 16,598 games  
- **Time Span:** 1980–2020  
- **Target Variable:** Global_Sales (in million units) 

Main features include platform, genre, release year, and regional sales (NA, EU, JP, Others).

---

## 🧹 Data Processing (Brief)

- Removed records with missing values  
- Applied **one-hot encoding** for categorical features  
- Scaled numerical features using **StandardScaler**  
- Split data into **80% training** and **20% testing**

---

## 🤖 Model Used

- **Multiple Linear Regression**
- Chosen for:
  - Continuous output prediction
  - Interpretability
  - Fast training and evaluation
  - Business-friendly insights

---

## 📏 Model Performance

- **R² Score:** 0.99999  
- **MAE:** ~0.003  
- **RMSE:** ~0.005  

The model shows **excellent accuracy** on unseen test data.

---

## 💡 Key Insights

- Regional sales (especially **North America and Europe**) strongly influence global sales  
- Platform and genre play a significant role in sales performance  
- Linear regression can provide reliable predictions for business forecasting  

---

## 🛠️ Technologies Used

- Python  
- Pandas, NumPy  
- Scikit-learn  
- Matplotlib / Seaborn  
- Jupyter Notebook  

---

## 🚀 Applications

- Sales forecasting before game release  
- Market and platform analysis  
- Budget and marketing optimization  
- Data-driven decision support for publishers  

---

## 👥 Team Members

| Name | Contribution |
|----|----|
| **Sagar Datkhile** | Data Preprocessing, Model Development, Presentation |
| Ashutosh Kinage | Data Collection & Analysis, Presentation |
| Harshwardhan Ahire | Feature Engineering & Model Optimization |
| Aniket Mahajan | Testing, Evaluation & Visualization |

---

## ▶️ Steps to Use the Model

### Step 1: Clone the Repository
```bash
git clone https://github.com/your-username/video-game-sales-prediction.git
cd video-game-sales-prediction
```

### Step 2: Install Required Libraries
Ensure Python is installed, then run:
```bash
pip install pandas numpy scikit-learn matplotlib seaborn streamlit
```

### Step 3: Run the Notebook
- Open the .ipynb file in Jupyter Notebook or Google Colab
- Run all cells to load data, preprocess it, and train the model

### Step 4: Train and Save the Model
After training, the model is saved as:

```bash
text
model.pkl
```

### Step 5: Load the Model for Prediction
```bash
python
import pickle

model = pickle.load(open("model.pkl", "rb"))
prediction = model.predict(input_data)
print(prediction)
```

### Step 6: Deploy the Model (Optional)
- Push the complete repository to GitHub
- Create a UI using Streamlit
- Run or deploy the app

```bash
streamlit run app.py
```

### Step 7: Use the Application
- Enter game details such as platform, genre, and regional sales
- Get predicted Global Video Game Sales output
- You can copy this entire block and paste it directly into your `README.md` file!

---

## 📌 Conclusion

This project highlights how **simple regression models**, combined with proper preprocessing and analysis, can deliver highly accurate predictions and valuable business insights in the gaming industry.

---

⭐ If you like this project, consider starring the repository!
