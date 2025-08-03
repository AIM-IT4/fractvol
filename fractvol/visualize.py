import matplotlib.pyplot as plt
import numpy as np

def plot_multifractal(ts, scales=None, q_list=None, figsize=(10, 6)):
    if scales is None:
        scales = [10, 20, 30, 50, 80]
    if q_list is None:
        q_list = [-3, -1, 1, 3]

    plt.figure(figsize=figsize)

    log_taus = []
    log_Fqs = []

    for q in q_list:
        s, F = mfdfa(ts, q=q, scales=scales)
        if len(F) == 0:
            continue
        log_s = np.log(s)
        log_F = np.log(F)
        log_taus.append(log_s)
        log_Fqs.append(log_F)
        plt.plot(log_s, log_F, label=f'q={q}', marker='o')

    plt.xlabel("log(Scale)")
    plt.ylabel("log(F(q))")
    plt.title("Multifractal DFA: Fluctuation vs Scale")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

    # Optional: singularity spectrum
    try:
        sig = fractal_signature(ts, scales=scales, q_list=q_list)
        hq = sig['full_hq']
        plt.figure(figsize=(6, 4))
        plt.plot(q_list, hq, 'ro-')
        plt.xlabel("Moment order q")
        plt.ylabel("H(q)")
        plt.title("Multifractal Spectrum H(q)")
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()
    except:
        pass