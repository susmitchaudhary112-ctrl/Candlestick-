import subprocess, sys
path = r"/content/Quote-Equity-NESTLEIND-EQ-30-11-2024-30-11-2025.csv"
def install(pkg):
    subprocess.call([sys.executable, "-m", "pip", "install", pkg])
for p in ["pandas", "matplotlib", "mplfinance"]:
    try:
        __import__(p)
    except ImportError:
        install(p)
import pandas as pd
import mplfinance as mpl
import matplotlib.pyplot as plt
df = pd.read_csv(path)
date_col = [c for c in df.columns if c.lower().startswith('date')][0]
df[date_col] = pd.to_datetime(df[date_col])
df.set_index(date_col, inplace=True)
# Rename columns to match mplfinance expectations
df.rename(columns={'OPEN': 'Open', 'HIGH': 'High', 'LOW': 'Low', 'CLOSE': 'Close', 'VOLUME': 'Volume'}, inplace=True)

# Convert relevant columns to numeric, handling commas and coercing errors
for col in ['Open', 'High', 'Low', 'Close', 'Volume']:
    df[col] = pd.to_numeric(df[col].astype(str).str.replace(',', ''), errors='coerce')

mpl.plot(df, type='candle', style='yahoo', volume=True, title='Nestle Ltd Candlestick Chart')
plt.show()
