import numpy as np
from sklearn.cluster import KMeans

def detect_regime_change(signatures, n_regimes=3):
    """
    Cluster fractal signatures to detect regime changes.
    Input: list of dict outputs from fractal_signature
    Output: array of labels over time
    """
    X = np.array([[s['H_small'], s['H_large'], s['multifractal_width']] 
                  for s in signatures if isinstance(s, dict)])
    
    kmeans = KMeans(n_clusters=n_regimes, random_state=0).fit(X)
    labels = kmeans.labels_
    
    # Reconstruct full timeline with NaNs
    result = np.full(len(signatures), np.nan)
    valid_idx = [i for i, s in enumerate(signatures) if isinstance(s, dict)]
    for i, lbl in zip(valid_idx, labels):
        result[i] = lbl
    return result