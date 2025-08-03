from .core import rolling_hurst, fractal_signature, mfdfa
from .detect import detect_regime_change
from .signal import predict_volatility_spark
from .visualize import plot_multifractal

__version__ = "0.1.0"
__author__ = "Amit Kumar Jha"
__email__ = "jha.8@alumni.iitj.ac.in"

__all__ = [
    "rolling_hurst",
    "fractal_signature",
    "mfdfa",
    "detect_regime_change",
    "predict_volatility_spark",
    "plot_multifractal",
]