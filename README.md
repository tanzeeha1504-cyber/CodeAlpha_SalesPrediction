# 🚀 SalesAI Pro: Smart Marketing Intelligence

An interactive Machine Learning web application that predicts future sales based on advertising spend across multiple channels.

This project combines data science with a modern web interface to help businesses make data-driven marketing decisions.


## 📌 Overview

SalesAI Pro uses a Linear Regression model to analyze how advertising budgets (TV, Radio, Newspaper) impact sales.  
It provides real-time predictions along with visual insights to guide marketing strategies.


## ✨ Features

- 📊 Predict sales based on advertising spend  
- 🎯 Interactive Streamlit web application  
- 📈 Visual analytics:
  - Bar chart (budget distribution)
  - Pie chart (spending ratio)
  - Trend graph (impact of TV ads on sales)
- 🧠 Business insights for marketing optimization  
- ⚡ Real-time predictions  



## 🧠 Machine Learning Workflow

## Algorithm Used: Linear Regression  
## Input Features:
  - TV Advertising Spend  
  - Radio Advertising Spend  
  - Newspaper Advertising Spend  
  ## Target Variable:
  - Sales  

### 🔹 Steps Involved:
1. Data Cleaning (removed unnecessary columns like index)
2. Feature Selection
3. Train-Test Split
4. Model Training
5. Model Evaluation (R² Score, MAE, MSE)


## 📊 Key Insights

- 📺 TV advertising has the strongest impact on sales  
- 📻 Radio ads contribute moderately  
- 📰 Newspaper ads have relatively lower influence  
- 📈 Increasing TV budget can significantly boost sales  



## 🛠️ Tech Stack

- Python 🐍  
- Pandas  
- NumPy  
- Scikit-learn  
- Matplotlib  
- Streamlit  



## 📁 Project Structure

CodeAlpha_SalesPrediction/
│
├── data/
│ └── advertising.csv
│
├── src/
│ ├── data_preprocessing.py
│ ├── train_model.py
│ └── evaluate_model.py
│
├── outputs/
│ ├── model.pkl
│ └── plots/
│
├── app/
│ └── app.py
│
├── main.py
├── requirements.txt
└── README.md




## ▶️ How to Run the Project

### 1️⃣ Clone the repository
git clone https://github.com/tanzeeha1504-cyber/CodeAlpha_SalesPrediction.git
cd CodeAlpha_SalesPrediction

## 2️⃣ Install dependencies
pip install -r requirements.txt

## 3️⃣ Train the model
python main.py

## 4️⃣ Run the Streamlit app
cd app
streamlit run app.py


## 🎯 Use Cases
📊 Marketing teams for budget planning
🧠 Data analysts for understanding ad impact
📈 Businesses for forecasting sales

## 👩‍💻 Author
Tanzee
Machine Learning Intern

## ⭐ Acknowledgment
Dataset inspired by advertising datasets commonly used in regression analysis.
