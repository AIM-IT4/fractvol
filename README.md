# fractvol – Fractal Volatility Signatures

📊 **Detect hidden market regimes using multifractal scaling and volatility geometry.**  
`fractvol` is a lightweight Python package that applies **physics-inspired fractal analysis** to financial time series, revealing hidden structures in volatility that traditional models miss.

Unlike standard volatility tools (e.g., GARCH, rolling std), `fractvol` analyzes how price fluctuations **scale across time horizons** — capturing memory, persistence, and market fragility through the lens of **multifractal dynamics**.

Perfect for quants, algo traders, and researchers exploring **non-linear market behavior**, early warning signals, and regime shifts.

---

## 🔍 What It Does

Financial markets aren’t random — they exhibit **long memory**, **volatility clustering**, and sudden **regime transitions** (e.g., calm → crash). These are signatures of **fractal geometry** in price dynamics.

`fractvol` uses **Multifractal Detrended Fluctuation Analysis (MFDFA)** to:
- Measure **scale-dependent persistence** (via Hurst exponent)
- Extract **fractal volatility signatures** — compact fingerprints of market state
- Detect **regime shifts** (e.g., efficient → turbulent)
- Predict **volatility spikes** before they happen
- Visualize the **multifractal spectrum** of returns

This allows you to:
✅ Identify when the market becomes "fragile"  
✅ Anticipate volatility breakouts  
✅ Adapt strategies to current market geometry  
✅ Move beyond linear assumptions in risk modeling

---

## 🚀 Quick Start

```python
import fractvol as fv
import yfinance as yf

# Fetch SPY returns
data = yf.download("SPY")['Close'].pct_change().dropna()

# 1. Rolling Hurst exponent (measure persistence over time)
hursts = fv.rolling_hurst(data, window=100, scales=[10, 20, 50])
print("Recent Hurst:", hursts[-5:])

# 2. Extract fractal signatures (market state fingerprints)
sigs = [fv.fractal_signature(data[i:i+200]) for i in range(0, len(data)-200, 50)]

# 3. Detect regime changes (e.g., stable vs. turbulent)
regimes = fv.detect_regime_change(sigs, n_regimes=3)

# 4. Predict volatility spikes (early warning system)
risk_score = fv.predict_volatility_spark(data, window=200)
print("Max risk score:", risk_score.max())

# 5. Visualize multifractal scaling
fv.plot_multifractal(data[-150:])```

📈 Key Insights You Can Gain
rolling_hurst()
Rising Hurst → trending market; Falling Hurst → mean-reverting or unstable
fractal_signature()
Width of multifractality measures market complexity. Narrowing = fragility
predict_volatility_spark()
High score = elevated risk of volatility spike (e.g., pre-crash signal)
detect_regime_change()
Uncover hidden states (e.g., "low-volatility trap" before a sell-off)
plot_multifractal()
See how returns scale across time — a fingerprint of market dynamics

💡 Example Insight:
Before major drawdowns (e.g., 2020 crash, 2022 bear market), the multifractal structure of markets often collapses — becoming less complex and more fragile.
fractvol detects this loss of multifractality as a rising risk score, giving you an early heads-up.

pip install fractvol

pip install fractvol[viz]      # for plotting
pip install fractvol[detect]   # for regime detection (scikit-learn)
pip install fractvol[all]      # both



📚 References
Kantelhardt et al. (2002). Multifractal DFA
Calvet & Fisher (2002). Multifractality in Asset Returns
Ivanov et al. (1999). Fractal analysis in physiology and finance
🛠️ License
MIT — Use freely in research and production.

🌐 Source
GitHub: https://github.com/AIM-IT4/fractvol?spm=a2ty_o01.29997173.0.0.42ecc9213D8d6X
PyPI: https://pypi.org/project/fractvol/?spm=a2ty_o01.29997173.0.0.42ecc9213D8d6X

Made with ❤️ for market explorers.
