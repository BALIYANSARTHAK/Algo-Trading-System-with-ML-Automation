# 📈 Algo-Trading System with ML & Automation

This project is a Python-based prototype that demonstrates how algorithmic trading strategies can be enhanced with Machine Learning, Google Sheets integration, and automation tools. It uses historical stock data from Yahoo Finance and applies both rule-based and ML-based logic to generate trading signals.

---

## 🚀 Features

- 📊 **Live Data Ingestion**: Pulls daily stock data using `yfinance` for selected NIFTY 50 companies.
- 📈 **Technical Indicators**: Computes RSI, Moving Averages (20-DMA, 50-DMA), MACD, and volume.
- ✅ **Rule-Based Trading Logic**:
  - **BUY**: RSI < 30 and 20-DMA > 50-DMA
  - **SELL**: RSI > 70 and 20-DMA < 50-DMA
- 🤖 **Machine Learning Prediction**:
  - Logistic Regression model using RSI, MACD, volume, etc.
  - Predicts next-day movement and shows probability of "Up".
- 🧾 **Google Sheets Integration**:
  - Logs trades and signals in real time using `gspread`
  - Includes P&L summary, win ratio, and audit trail

