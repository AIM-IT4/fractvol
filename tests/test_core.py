import numpy as np
from fractvol.core import mfdfa, rolling_hurst, fractal_signature

def test_mfdfa():
    ts = np.random.randn(500)
    scales, F = mfdfa(ts, scales=range(10, 100, 10))
    assert len(scales) > 0
    assert len(F) == len(scales)

def test_rolling_hurst():
    ts = np.random.randn(300)
    h = rolling_hurst(ts, window=100)
    assert len(h) == 200

def test_fractal_signature():
    ts = np.random.randn(200)
    sig = fractal_signature(ts)
    assert isinstance(sig, dict)
    assert 'multifractal_width' in sig