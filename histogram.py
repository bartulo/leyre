import matplotlib.pyplot as plt
import numpy as np

def make_plot(ins, outs):
    x = ins['HeightAboveGround']

    plt.hist(x, bins=30, color='green', edgecolor='black')

    plt.savefig(f"FINALES/HISTOGRAM/histogram_{pdalargs['vuelo']}_zona{pdalargs['zona']}.png")
    
    return True

def make_model_histogram(ins, outs):
    x = ins['HeightAboveGround']
    plt.hist(x, bins=30, weights=1 / pdalargs['m2'] * np.ones(len(x)), color='green', edgecolor='black')
    plt.ylim(0, 30)
    plt.savefig(f"histogram_{pdalargs['vuelo']}_zona{pdalargs['zona']}_modelo{pdalargs['modelo']}.png")
    plt.close()
    return True

def make_evol_histogram(ins, outs):
    x = ins['HeightAboveGround']
    plt.hist(x, bins=30, weights=1 / pdalargs['m2'] * np.ones(len(x)), color='green', edgecolor='black')
    plt.ylim(0, 30)
    plt.savefig(f"evolucion_histogram_{pdalargs['vuelo_pre']}_{pdalargs['vuelo_post']}_zona{pdalargs['zona']}_modelo{pdalargs['modelo']}.png")
    plt.close()
    return True