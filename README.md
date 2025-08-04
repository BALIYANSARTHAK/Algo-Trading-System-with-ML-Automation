# 📈 Algo-Trading System with ML & Automation

This project is a Python-based prototype that simulates algorithmic trading using both rule-based logic and machine learning. It fetches historical stock data, computes indicators, predicts future price movement, and optionally logs trades to Google Sheets securely.

---

## 🚀 Features

- 📊 **Stock Data Ingestion**: Uses `yfinance` to fetch NIFTY 50 stock data.
- 📈 **Technical Indicators**: Calculates RSI, 20-DMA, 50-DMA.
- ✅ **Rule-Based Strategy**: Generates BUY/SELL/HOLD signals based on RSI and DMA crossover.
- 🤖 **ML Model**: Logistic Regression model trained on historical features to predict next-day movement.
- 🧾 **Secure Google Sheets Integration**:
  - Logs trades using `gspread` and Google Sheets API.
  - Credentials handled via secure environment variables.

---

## 📁 Folder Structure

```

algo\_trading\_project/
├── data\_handler.py
├── strategy.py
├── ml\_model.py
├── sheets\_handler.py
├── main.py
├── secrets/
│   └── credentials.json     # Ignored by Git
├── .gitignore
├── requirements.txt
└── README.md

````

---

## ⚙️ How to Run

### 1. Create & Activate Virtual Environment

```bash
python -m venv .venv
# Activate on Windows
.venv\Scripts\activate
````

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Environment Variable for Google Credentials

```bash
$env:GOOGLE_CREDENTIALS_PATH="secrets/credentials.json"  # PowerShell
```

Or use a `.env` file:

```
GOOGLE_CREDENTIALS_PATH=secrets/credentials.json
```

And load it in `main.py` using:

```python
from dotenv import load_dotenv
load_dotenv()
```

### 4. Run the App

```bash
python main.py
```

---

## 📦 Dependencies

```
yfinance
pandas
numpy
scikit-learn
gspread
oauth2client
python-dotenv
```

---

## 🔐 Secure Credential Handling

To prevent accidental exposure:

* Do **not** commit `credentials.json` to GitHub.
* Ensure `.gitignore` contains:

```gitignore
credentials.json
secrets/
.env
```

If committed by mistake, **revoke the key** from your [Google Cloud Console](https://console.cloud.google.com/iam-admin/serviceaccounts).

---

## 📊 Output Example

```
          [*********************100%***********************]  1 of 1 completed
Price             Close        RSI        20DMA        50DMA Signal
Ticker           TCS.NS
Date
2025-07-29  3056.000000  12.081860  3250.163196  3358.266689   HOLD
2025-07-30  3053.600098  12.064336  3232.257117  3349.680337   HOLD
2025-07-31  3036.800049  15.801705  3214.632227  3341.722114   HOLD
2025-08-01  3003.000000  16.279099  3194.370544  3332.345039   HOLD
2025-08-04  3023.300049  13.715094  3175.527502  3322.925483   HOLD
Accuracy: 0.2

---
