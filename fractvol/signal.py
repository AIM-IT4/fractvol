import numpy as np

def predict_volatility_spark(ts, window=100, threshold=0.4):
    """
    Predict short-term volatility spike if multifractality collapses.
    Returns score in [0,1]: 1 = high chance of spike.
    """
    scores = []
    for i in range(window, len(ts)):
        seg = ts[i-window:i]
        try:
            sig = fractal_signature(seg)
            width = sig['multifractal_width']
            # Lower width → less multifractal → more fragile → higher risk
            score = 1 - (width / 1.5)  # normalize empirically
            score = np.clip(score, 0, 1)
            scores.append(score)
        except:
            scores.append(0.0)
    return np.array(scores)