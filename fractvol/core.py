import numpy as np
from scipy.optimize import curve_fit

def _polynomial_detrend(ts, window_size, order=1):
    x = np.arange(window_size)
    coeffs = np.polyfit(x, ts, order)
    poly = np.poly1d(coeffs)
    return ts - poly(x)

def mfdfa(ts, q=2, scales=range(10, 100, 10), order=1):
    """
    Multifractal DFA: Returns F(q, scale) and Hurst-like exponents.
    """
    ts = np.array(ts)
    ts = ts - np.mean(ts)
    cumsum_ts = np.cumsum(ts - np.mean(ts))

    Fq = []
    for scale in scales:
        if len(ts) < scale * 2:
            continue
        F = []
        for start in range(0, len(ts) - scale + 1, scale):
            segment = cumsum_ts[start:start+scale]
            detrended = _polynomial_detrend(segment, len(segment), order)
            F.append(np.mean(detrended ** 2))
        Fq.append(np.mean(np.array(F) ** (q/2)) ** (1/q) if q != 0 else 
                  np.mean(np.log(np.array(F))) / 2)
    return np.array(scales[:len(Fq)]), np.array(Fq)

def rolling_hurst(ts, window=100, scales=None, q=2):
    if scales is None:
        scales = [10, 20, 30, 50]
    ts = np.array(ts)
    hursts = []
    for i in range(window, len(ts)):
        window_ts = ts[i-window:i]
        try:
            s, F = mfdfa(window_ts, q=q, scales=scales)
            log_s = np.log(s)
            log_F = np.log(F)
            slope, _ = curve_fit(lambda x, a, b: a * x + b, log_s, log_F)[0]
            hursts.append(slope)
        except:
            hursts.append(np.nan)
    return np.array(hursts)

def fractal_signature(ts, scales=None, q_list=None):
    if scales is None:
        scales = [10, 20, 50]
    if q_list is None:
        q_list = [-3, -1, 0, 1, 3]

    Fqs = []
    for q in q_list:
        _, Fq = mfdfa(ts, q=q, scales=scales)
        log_Fq = np.log(np.clip(Fq, 1e-10, None))
        log_s = np.log(scales[:len(Fq)])
        slope, _ = curve_fit(lambda x, a, b: a * x + b, log_s, log_Fq)[0]
        Fqs.append(slope)
    
    # Width of singularity spectrum ≈ multifractality strength
    h_old = np.polyfit(q_list, Fqs, 2, full=True)
    width = np.ptp(Fqs)  # rough proxy
    return {
        'H_small': Fqs[0],      # response at small q (volatile moments)
        'H_large': Fqs[-1],     # response at large q (persistent trends)
        'multifractal_width': width,
        'full_hq': Fqs
    }