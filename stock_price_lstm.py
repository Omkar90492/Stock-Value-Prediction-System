import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Read Data
prices = pd.read_csv('prices.csv')
securities = pd.read_csv('securities.csv')

# Merge with proper columns
merged_data = pd.merge(prices, securities, left_on='symbol', right_on='Ticker symbol')
merged_data = merged_data.rename(columns={'GICS Sector': 'Sector'})

# Filter for a sector
sector_name = 'Information Technology'
sector_data = merged_data[merged_data['Sector'] == sector_name]

# Pick a company
company_symbol = 'AAPL'  # Change this if you want
company_data = sector_data[sector_data['symbol'] == company_symbol].copy()

# Convert date
company_data['date'] = pd.to_datetime(company_data['date'])
company_data = company_data.sort_values('date')

# 1️⃣ Plot Closing Price Trend
plt.figure(figsize=(12, 5))
plt.plot(company_data['date'], company_data['close'], label='Closing Price')
plt.title(f'{company_symbol} - Closing Price Trend')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.legend()
plt.show()

# 2️⃣ Plot Moving Average (30 days)
company_data['30_MA'] = company_data['close'].rolling(window=30).mean()
plt.figure(figsize=(12, 5))
plt.plot(company_data['date'], company_data['close'], label='Closing Price')
plt.plot(company_data['date'], company_data['30_MA'], label='30 Day Moving Average', color='red')
plt.title(f'{company_symbol} - Moving Average')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()

# 3️⃣ Linear Regression Prediction
company_data['date_num'] = company_data['date'].map(pd.Timestamp.toordinal)
X = company_data[['date_num']]
y = company_data['close']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Evaluate
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))

# 3️⃣ Plot Actual vs Predicted Prices
plt.figure(figsize=(12, 5))
plt.plot(company_data['date'], company_data['close'], label='Actual Price')
plt.plot(X_test['date_num'].map(pd.to_datetime), y_pred, color='green', label='Predicted Price (Test)')
plt.title(f'{company_symbol} - Actual vs Predicted')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()
