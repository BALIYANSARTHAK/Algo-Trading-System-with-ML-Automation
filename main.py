from data_handler import download_data, add_indicators
from strategy import generate_signals
from ml_model import prepare_ml_data, train_model
from dotenv import load_dotenv
load_dotenv()  # Load variables from .env

# from sheets_handler import connect_to_sheets, log_trade

ticker = "TCS.NS"
df = download_data(ticker)
df = add_indicators(df)
df = generate_signals(df)

print(df[['Close', 'RSI', '20DMA', '50DMA', 'Signal']].tail())

# ML
X, y = prepare_ml_data(df)
model = train_model(X, y)

# Google Sheets (Uncomment to use)
# sheet = connect_to_sheets("credentials.json", "TradeLogs")
# for idx, row in df.tail(5).iterrows():
#     log_trade(sheet, row.name, row['Signal'], row['Close'])