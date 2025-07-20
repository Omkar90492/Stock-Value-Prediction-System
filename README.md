# 📈 Stock Price Prediction Using Historical Data

## 📝 Project Description  
This project focuses on analyzing and predicting stock prices using historical price data combined with company information.  
It merges financial datasets, performs trend analysis, and applies a simple regression model to forecast future prices.  
The project includes meaningful visualizations and performance evaluation.

---

## ⚙️ Features

- 📊 Visualize historical stock price trends
- 📉 Calculate and plot moving averages
- 🤖 Predict stock prices using Linear Regression
- 📑 Analyze company data based on sector
- 🗃️ Works on real datasets (prices.csv & securities.csv)
- 📈 Mean Squared Error calculation for model accuracy

---

📁 Project Structure
-------------------
Stock Prediction Project/
- prices.csv               # Historical stock price data
- securities.csv           # Company information data
- stock_price_lstm.py      # Python script with code
- README.md                # Project description (you can add this)

  ---


## 🧠 Tech Stack

- Python 3.x
- Pandas — Data Handling
- Matplotlib — Data Visualization
- Scikit-Learn — Machine Learning (Linear Regression)
  
---

## 🚀 How to Run the Project

**Step 1✅ Clone the repository or download the folder**

**Step 2✅ Install required libraries:**

  pip install pandas matplotlib scikit-learn
**Step 3✅ Make sure prices.csv and securities.csv are in the same folder:**

**Step 4✅ Run the Python script:**

python stock_price_lstm.py
**Step 5✅ View the generated graphs & check console output for Mean Squared Error**

---

## 📌 Results

## 📈 Accuracy Chart
![Accuracy](images/accuracy_comparison.png)

## 🧪 Confusion Matrix - XGBoost
![XGBoost](images/confusion_matrix_xgboost.png)

## 🌲 Confusion Matrix - Random Forest
![RandomForest](images/confusion_matrix_randomforest.png)

## 💻 Confusion Matrix - SVC
![SVC](images/confusion_matrix_svc.png)

---

##🚀 Quick Tips
-------------
- Filter by any sector or company symbol inside the code
- Use .head() on DataFrames for faster testing
- Adjust moving average window if needed

---

## ✅ 📦 Prerequisites

- Python 3.8+ installed
- Basic knowledge of Python and Pandas
- VS Code or any Python IDE



---

## ✅ 📌 Conclusion

This project demonstrates how historical data combined with company metadata can help visualize trends and make basic stock predictions. Though simple, it forms a solid base for understanding data analysis and machine learning concepts applied to finance.

---

## ✅ 📌 Key outcomes

- Merged multi-source datasets for analysis
- Visualized trends and moving averages
- Applied Linear Regression for price prediction
- Evaluated prediction with Mean Squared Error


