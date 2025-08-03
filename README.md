# fractvol – Fractal Volatility Signatures

Detect hidden market regimes using **multifractal scaling** and **Hurst dynamics**.  
`fractvol` brings advanced physics-based time series analysis to finance.

```python
import fractvol as fv
import yfinance as yf

data = yf.download("SPY")['Close'].pct_change().dropna()

# Rolling fractal analysis
hursts = fv.rolling_hurst(data, window=100)

# Detect regime shifts
sigs = [fv.fractal_signature(data[i:i+200]) for i in range(0, len(data)-200, 50)]
regimes = fv.detect_regime_change(sigs)

# Predict volatility spikes
risk_score = fv.predict_volatility_spark(data)

# Visualize
fv.plot_multifractal(data[-150:])