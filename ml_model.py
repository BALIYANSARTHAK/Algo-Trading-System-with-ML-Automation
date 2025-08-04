from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

def prepare_ml_data(df):
    df = df.dropna().copy()
    df['Target'] = np.where(df['Close'].shift(-1) > df['Close'], 1, 0)
    features = ['RSI', '20DMA', '50DMA']
    X = df[features]
    y = df['Target']
    return X, y

def train_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
    model = LogisticRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
    return model