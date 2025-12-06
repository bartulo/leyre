import matplotlib.pyplot as plt
import numpy as np

def make_plot(ins, outs):
    z = ins['Z']
    x = ins['X']
    y = ins['Y']
    
    plt.hist(x, bins=30, color='green', edgecolor='black')

    plt.savefig(f"FINALES/TRANSECTOS/transecto_{pdalargs['vuelo']}_zona{pdalargs['zona']}.png")
    
    return True

