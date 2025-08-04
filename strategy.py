def generate_signals(df):
    signals = []
    for i in range(len(df)):
        if df['RSI'].iloc[i] < 30 and df['20DMA'].iloc[i] > df['50DMA'].iloc[i]:
            signals.append("BUY")
        elif df['RSI'].iloc[i] > 70 and df['20DMA'].iloc[i] < df['50DMA'].iloc[i]:
            signals.append("SELL")
        else:
            signals.append("HOLD")
    df['Signal'] = signals
    return df